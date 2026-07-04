// State Management
const state = {
  mode: null,          // 'full', 'practice', 'quick'
  questions: [],       // Current active question list
  currentIndex: 0,     // Current question index
  answers: {},         // Chosen answers { questionId: answer }
  bookmarks: new Set(),// Flagged question IDs
  timeElapsed: 0,      // Seconds elapsed
  timerInterval: null, // Timer interval reference
  isReviewMode: false, // Review mode flag
  quizData: null       // Complete quiz data loaded from JSON
};

// DOM Elements
const elements = {
  themeToggle: document.getElementById('theme-toggle'),
  timerBox: document.getElementById('timer-box'),
  examTimer: document.getElementById('exam-timer'),
  dashboardView: document.getElementById('dashboard-view'),
  examView: document.getElementById('exam-view'),
  resultsView: document.getElementById('results-view'),
  qTopic: document.getElementById('q-topic'),
  qDiff: document.getElementById('q-diff'),
  bookmarkBtn: document.getElementById('bookmark-btn'),
  qObjective: document.getElementById('q-objective'),
  questionText: document.getElementById('question-text'),
  scenarioBox: document.getElementById('scenario-box'),
  scenarioText: document.getElementById('scenario-text'),
  optionsBlock: document.getElementById('options-block'),
  shortAnswerBlock: document.getElementById('short-answer-block'),
  shortAnswerInput: document.getElementById('short-answer-input'),
  prevBtn: document.getElementById('prev-btn'),
  nextBtn: document.getElementById('next-btn'),
  questionProgress: document.getElementById('question-progress'),
  submitExamBtn: document.getElementById('submit-exam-btn'),
  questionNavGrid: document.getElementById('question-nav-grid'),
  scoreRing: document.getElementById('score-ring'),
  scoreNum: document.getElementById('score-num'),
  scoreMax: document.getElementById('score-max'),
  scorePercentage: document.getElementById('score-percentage'),
  timeSpent: document.getElementById('time-spent'),
  resultStatusTitle: document.getElementById('result-status-title'),
  resultStatusDesc: document.getElementById('result-status-desc'),
  topicBreakdownList: document.getElementById('topic-breakdown-list'),
  gapAnalysisList: document.getElementById('gap-analysis-list'),
  revisionTopicsList: document.getElementById('revision-topics-list'),
  reviewBar: document.getElementById('review-bar')
};

// Initialize Application
document.addEventListener('DOMContentLoaded', () => {
  // Load Quiz Data
  fetch('quiz_data.json')
    .then(response => {
      if (!response.ok) {
        throw new Error('Failed to load quiz data');
      }
      return response.json();
    })
    .then(data => {
      state.quizData = data;
      console.log('Quiz data loaded successfully:', data);
      checkResumableState();
    })
    .catch(error => {
      alert('เกิดข้อผิดพลาดในการโหลดข้อสอบ กรุณาติดต่อผู้พัฒนา: ' + error.message);
    });

  // Event Listeners
  elements.themeToggle.addEventListener('click', toggleTheme);
  elements.bookmarkBtn.addEventListener('click', toggleBookmark);
  elements.prevBtn.addEventListener('click', goToPreviousQuestion);
  elements.nextBtn.addEventListener('click', goToNextQuestion);
  elements.submitExamBtn.addEventListener('click', submitExam);

  // Setup Short Answer Input Auto-Save
  elements.shortAnswerInput.addEventListener('input', (e) => {
    if (state.questions.length > 0) {
      const q = state.questions[state.currentIndex];
      state.answers[q.id] = e.target.value;
      updateSidebarButton(state.currentIndex);
      saveStateToLocalStorage();
    }
  });

  // Keyboard navigation support
  document.addEventListener('keydown', handleKeyboardNavigation);
});

// Keyboard Navigation Handler
function handleKeyboardNavigation(e) {
  if (state.questions.length === 0 || state.isReviewMode) return;

  // Arrow Left: Previous, Arrow Right: Next
  if (e.key === 'ArrowLeft') {
    goToPreviousQuestion();
  } else if (e.key === 'ArrowRight') {
    goToNextQuestion();
  }

  // A, B, C, D to select options for MCQ/Scenario questions
  const q = state.questions[state.currentIndex];
  if (q.options && q.options.length === 4) {
    let optIndex = -1;
    if (e.key.toLowerCase() === 'a') optIndex = 0;
    if (e.key.toLowerCase() === 'b') optIndex = 1;
    if (e.key.toLowerCase() === 'c') optIndex = 2;
    if (e.key.toLowerCase() === 'd') optIndex = 3;

    if (optIndex !== -1) {
      const optLetter = ["A", "B", "C", "D"][optIndex];
      selectOption(optLetter);
    }
  }
}

// Dark/Light Theme Toggle
function toggleTheme() {
  const body = document.body;
  const icon = elements.themeToggle.querySelector('i');
  
  if (body.classList.contains('dark-mode')) {
    body.classList.remove('dark-mode');
    body.classList.add('light-mode');
    icon.className = 'fa-solid fa-sun';
  } else {
    body.classList.remove('light-mode');
    body.classList.add('dark-mode');
    icon.className = 'fa-solid fa-moon';
  }
}

// Start Exam Mode
function startExam(mode) {
  state.mode = mode;
  state.currentIndex = 0;
  state.answers = {};
  state.bookmarks.clear();
  state.timeElapsed = 0;
  state.isReviewMode = false;
  elements.reviewBar.classList.add('hide');

  // Filter Questions based on Mode
  const sectionA = state.quizData.sections.A.questions;
  const sectionB = state.quizData.sections.B.questions;
  const sectionC = state.quizData.sections.C.questions;
  const sectionD = state.quizData.sections.D.questions;

  if (mode === 'full') {
    // All 330 questions
    state.questions = [...sectionA, ...sectionB, ...sectionC, ...sectionD];
    elements.timerBox.classList.remove('hide');
    startTimer();
  } else if (mode === 'practice') {
    // All 330 questions but no timer
    state.questions = [...sectionA, ...sectionB, ...sectionC, ...sectionD];
    elements.timerBox.classList.add('hide');
  } else if (mode === 'quick') {
    // 10 Random questions from Section A & C
    const combinedPool = [...sectionA, ...sectionC];
    state.questions = getRandomSubset(combinedPool, 10);
    elements.timerBox.classList.remove('hide');
    startTimer();
  }

  // Show Exam View
  elements.dashboardView.classList.add('hide');
  elements.resultsView.classList.add('hide');
  elements.examView.classList.remove('hide');

  // Generate Navigation Grid
  generateNavGrid();
  
  // Render First Question
  renderQuestion();
  saveStateToLocalStorage();
}

// Start Timer Interval
function startTimer() {
  if (state.timerInterval) clearInterval(state.timerInterval);
  state.timerInterval = setInterval(() => {
    state.timeElapsed++;
    elements.examTimer.textContent = formatTime(state.timeElapsed);
    if (state.timeElapsed % 10 === 0) {
      saveStateToLocalStorage(); // Auto-save elapsed time
    }
  }, 1000);
}

// Format Seconds to HH:MM:SS
function formatTime(seconds) {
  const hrs = Math.floor(seconds / 3600);
  const mins = Math.floor((seconds % 3600) / 60);
  const secs = seconds % 60;
  return [
    hrs.toString().padStart(2, '0'),
    mins.toString().padStart(2, '0'),
    secs.toString().padStart(2, '0')
  ].join(':');
}

// Generate Random Subset of Questions
function getRandomSubset(arr, size) {
  const shuffled = [...arr].sort(() => 0.5 - Math.random());
  return shuffled.slice(0, size);
}

// Generate Question Navigation Sidebar Grid
function generateNavGrid() {
  elements.questionNavGrid.innerHTML = '';
  state.questions.forEach((q, idx) => {
    const btn = document.createElement('button');
    btn.className = 'nav-btn';
    btn.id = `nav-btn-${idx}`;
    btn.textContent = idx + 1;
    btn.addEventListener('click', () => {
      state.currentIndex = idx;
      renderQuestion();
    });
    elements.questionNavGrid.appendChild(btn);
    updateSidebarButton(idx);
  });
}

// Update Sidebar Button CSS Class States
function updateSidebarButton(idx) {
  const btn = document.getElementById(`nav-btn-${idx}`);
  if (!btn) return;

  const q = state.questions[idx];
  
  // Clear all classes except base
  btn.className = 'nav-btn';

  if (state.currentIndex === idx) {
    btn.classList.add('active');
  }

  if (state.isReviewMode) {
    // Review Mode: Correct or Incorrect color
    const isCorrect = checkAnswerCorrectness(q);
    if (q.id.startsWith('SHORT')) {
      btn.classList.add('answered');
    } else if (isCorrect) {
      btn.classList.add('correct');
    } else {
      btn.classList.add('incorrect');
    }
  } else {
    // Test Taking Mode: Answered and Flagged
    if (state.answers[q.id] !== undefined && state.answers[q.id] !== '') {
      btn.classList.add('answered');
    }
    if (state.bookmarks.has(q.id)) {
      btn.classList.add('flagged');
    }
  }
}

// Check Correctness of a Question
function checkAnswerCorrectness(q) {
  const userAnswer = state.answers[q.id];
  if (userAnswer === undefined || userAnswer === '') return false;
  
  if (q.id.startsWith('MCQ') || q.id.startsWith('SCENARIO') || q.id.startsWith('TF')) {
    return userAnswer === q.correct_answer;
  }
  
  // Short answers are not mathematically auto-graded but let's count them if they are filled in
  if (q.id.startsWith('SHORT')) {
    return userAnswer.trim().length >= 3;
  }
  
  return false;
}

// Render Current Question Details
function renderQuestion() {
  const q = state.questions[state.currentIndex];
  
  // Update Meta
  elements.qTopic.textContent = q.topic;
  elements.qDiff.textContent = q.difficulty === 'Easy' ? 'ง่าย' : q.difficulty === 'Medium' ? 'ปานกลาง' : 'ยาก';
  elements.qDiff.className = 'diff-tag ' + q.difficulty.toLowerCase();
  
  // Update Bookmark state
  if (state.bookmarks.has(q.id)) {
    elements.bookmarkBtn.classList.add('active');
    elements.bookmarkBtn.querySelector('i').className = 'fa-solid fa-bookmark';
  } else {
    elements.bookmarkBtn.classList.remove('active');
    elements.bookmarkBtn.querySelector('i').className = 'fa-regular fa-bookmark';
  }

  elements.qObjective.textContent = `หัวข้อย่อย/วัตถุประสงค์: ${q.learning_objective}`;
  
  // Update Navigation buttons
  elements.prevBtn.disabled = state.currentIndex === 0;
  elements.nextBtn.disabled = state.currentIndex === state.questions.length - 1;
  elements.questionProgress.textContent = `ข้อที่ ${state.currentIndex + 1} จาก ${state.questions.length}`;

  // Reset Scenario Box
  if (q.scenario) {
    elements.scenarioBox.classList.remove('hide');
    elements.scenarioText.textContent = q.scenario;
  } else {
    elements.scenarioBox.classList.add('hide');
  }

  // Render Question Text
  elements.questionText.textContent = q.question;

  // Render Answers blocks depending on type
  if (q.options) {
    elements.optionsBlock.classList.remove('hide');
    elements.shortAnswerBlock.classList.add('hide');
    renderOptions(q);
  } else {
    // Short Answer
    elements.optionsBlock.classList.add('hide');
    elements.shortAnswerBlock.classList.remove('hide');
    elements.shortAnswerInput.value = state.answers[q.id] || '';
    
    // Read only in review mode
    if (state.isReviewMode) {
      elements.shortAnswerInput.disabled = true;
      renderShortAnswerExplanation(q);
    } else {
      elements.shortAnswerInput.disabled = false;
      const exp = elements.shortAnswerBlock.querySelector('.explanation-box');
      if (exp) exp.remove();
    }
  }

  // Highlight active sidebar navigation
  state.questions.forEach((_, idx) => updateSidebarButton(idx));
}

// Render Option Cards
function renderOptions(q) {
  elements.optionsBlock.innerHTML = '';
  
  const letters = ["A", "B", "C", "D"];

  q.options.forEach((optText, idx) => {
    const optLetter = letters[idx];
    const card = document.createElement('div');
    card.className = 'option-card';
    
    const badge = document.createElement('span');
    badge.className = 'option-index';
    badge.textContent = optLetter;
    
    const textSpan = document.createElement('span');
    textSpan.textContent = optText;
    
    card.appendChild(badge);
    card.appendChild(textSpan);
    
    const isSelected = state.answers[q.id] === optLetter;
    if (isSelected) {
      card.classList.add('selected');
    }

    if (state.isReviewMode) {
      const isCorrectOption = optLetter === q.correct_answer;
      if (isCorrectOption) {
        card.classList.add('correct');
      } else if (isSelected) {
        card.classList.add('incorrect');
      }
    } else {
      card.addEventListener('click', () => selectOption(optLetter));
    }
    
    elements.optionsBlock.appendChild(card);
  });

  // Render Explanation if in Review Mode
  if (state.isReviewMode) {
    const expBox = document.createElement('div');
    expBox.className = 'explanation-box';
    
    const isCorrect = state.answers[q.id] === q.correct_answer;
    const headerHtml = isCorrect 
      ? '<h4><i class="fa-solid fa-circle-check"></i> ตอบถูกต้อง</h4>'
      : '<h4><i class="fa-solid fa-circle-xmark"></i> ตอบผิด (คำตอบที่ถูกต้องคือ ' + q.correct_answer + ')</h4>';
    
    expBox.innerHTML = headerHtml + '<p>' + q.explanation + '</p>';
    elements.optionsBlock.appendChild(expBox);
  }
}

// Render Short Answer expected explanation in review mode
function renderShortAnswerExplanation(q) {
  const existing = elements.shortAnswerBlock.querySelector('.explanation-box');
  if (existing) existing.remove();

  const expBox = document.createElement('div');
  expBox.className = 'explanation-box';
  
  expBox.innerHTML = `
    <h4><i class="fa-solid fa-lightbulb"></i> แนวทางคำตอบที่ถูกต้อง</h4>
    <p><strong>คำตอบแนวทาง:</strong> ${q.expected_answer}</p>
    <div style="margin-top:12px; font-size:0.9rem; color:var(--text-secondary)">
      * ระบบจะตรวจเช็คว่าท่านได้กรอกข้อมูลหรือไม่ กรุณาทบทวนความรู้ของท่านกับแนวทางคำตอบด้านบน
    </div>
  `;
  elements.shortAnswerBlock.appendChild(expBox);
}

// Select MCQ option
function selectOption(letter) {
  const q = state.questions[state.currentIndex];
  state.answers[q.id] = letter;
  renderQuestion();
  saveStateToLocalStorage();
}

// Toggle Bookmark Flag
function toggleBookmark() {
  const q = state.questions[state.currentIndex];
  if (state.bookmarks.has(q.id)) {
    state.bookmarks.delete(q.id);
  } else {
    state.bookmarks.add(q.id);
  }
  renderQuestion();
  saveStateToLocalStorage();
}

// Navigate to Previous Question
function goToPreviousQuestion() {
  if (state.currentIndex > 0) {
    state.currentIndex--;
    renderQuestion();
    saveStateToLocalStorage();
  }
}

// Navigate to Next Question
function goToNextQuestion() {
  if (state.currentIndex < state.questions.length - 1) {
    state.currentIndex++;
    renderQuestion();
    saveStateToLocalStorage();
  }
}

// Submit Exam and Calculate Score
function submitExam() {
  const totalQuestions = state.questions.length;
  const answeredCount = Object.keys(state.answers).filter(k => state.answers[k] !== '').length;
  const unansweredCount = totalQuestions - answeredCount;

  let confirmMsg = 'คุณต้องการส่งข้อสอบเพื่อประเมินผลคะแนนใช่หรือไม่?';
  if (unansweredCount > 0) {
    confirmMsg = `คุณยังมีคำถามที่ไม่ได้ตอบอีก ${unansweredCount} ข้อ ต้องการส่งข้อสอบเลยหรือไม่?`;
  }

  if (confirm(confirmMsg)) {
    if (state.timerInterval) clearInterval(state.timerInterval);
    calculateResults();
  }
}

// Calculate score breakdown, gaps, and render Results
function calculateResults() {
  let score = 0;
  const maxScore = state.questions.length;
  
  const topicStats = {};

  state.questions.forEach(q => {
    if (!topicStats[q.topic]) {
      topicStats[q.topic] = { total: 0, correct: 0 };
    }
    topicStats[q.topic].total++;

    const isCorrect = checkAnswerCorrectness(q);
    if (isCorrect) {
      score++;
      topicStats[q.topic].correct++;
    }
  });

  const percentage = Math.round((score / maxScore) * 100);
  const passThreshold = 80;
  const isPassed = percentage >= passThreshold;

  // Render Scores text
  elements.scoreNum.textContent = score;
  elements.scoreMax.textContent = maxScore;
  elements.scorePercentage.textContent = `${percentage}%`;
  
  // Format and show time spent
  elements.timeSpent.textContent = formatTime(state.timeElapsed);

  // Circular progress ring calculation
  const circle = elements.scoreRing;
  const radius = circle.r.baseVal.value;
  const circumference = radius * 2 * Math.PI;
  const offset = circumference - (percentage / 100) * circumference;
  circle.style.strokeDasharray = `${circumference} ${circumference}`;
  circle.style.strokeDashoffset = offset;

  // Style the Ring and Titles according to Passing State
  if (isPassed) {
    circle.style.stroke = 'var(--success-color)';
    elements.resultStatusTitle.textContent = 'ยินดีด้วย! คุณผ่านการประเมิน';
    elements.resultStatusTitle.style.color = 'var(--success-color)';
    elements.resultStatusDesc.textContent = `ยอดเยี่ยม! คุณสอบผ่านเกณฑ์ ${passThreshold}% และมีความรู้ความแม่นยำเนื้อหาของ Arduino เบื้องต้นเป็นอย่างดี`;
  } else {
    circle.style.stroke = 'var(--error-color)';
    elements.resultStatusTitle.textContent = 'พยายามอีกครั้ง! คุณยังไม่ผ่านเกณฑ์';
    elements.resultStatusTitle.style.color = 'var(--error-color)';
    elements.resultStatusDesc.textContent = `คะแนนของคุณยังไม่ถึงเกณฑ์ขั้นต่ำ 80% (ต้องการ 264 คะแนนจาก 330) แนะนำให้กลับไปทบทวนหัวข้อที่พบช่องว่างความรู้`;
  }

  // Populate Topic Breakdown
  elements.topicBreakdownList.innerHTML = '';
  Object.keys(topicStats).forEach(topic => {
    const stats = topicStats[topic];
    const topicPercent = Math.round((stats.correct / stats.total) * 100);
    const fillClass = topicPercent >= 80 ? 'high' : topicPercent >= 50 ? 'med' : 'low';
    
    // Custom inline style for colors on progress fill
    let colorStyle = 'background-color: var(--error-color);';
    if (topicPercent >= 80) colorStyle = 'background-color: var(--success-color);';
    else if (topicPercent >= 50) colorStyle = 'background-color: var(--warning-color);';

    const item = document.createElement('div');
    item.className = 'topic-bar-item';
    item.innerHTML = `
      <div class="topic-bar-meta">
        <span class="topic-bar-title">${topic}</span>
        <span class="topic-bar-val">${stats.correct}/${stats.total} (${topicPercent}%)</span>
      </div>
      <div class="progress-track">
        <div class="progress-fill" style="width: ${topicPercent}%; ${colorStyle}"></div>
      </div>
    `;
    elements.topicBreakdownList.appendChild(item);
  });

  // Generate Knowledge Gap Analysis (Dynamic based on topic scores)
  elements.gapAnalysisList.innerHTML = '';
  const failedTopics = [];

  Object.keys(topicStats).forEach(topic => {
    const stats = topicStats[topic];
    const topicPercent = (stats.correct / stats.total) * 100;
    if (topicPercent < 80) {
      failedTopics.push({ topic, percent: topicPercent });
    }
  });

  const gapDescriptions = {
    "Sketch Structure & Control Flow": "สับสนวงจรการทำงานของ setup() และ loop(), ลำดับโครงสร้าง loop ต่างๆ, หรือการทำงานแบบเงื่อนไขและ scope ตัวแปร",
    "Data Types & Variables": "สับสนความแตกต่างระหว่าง String class กับ C-strings, ขนาดการจองหน่วยความจำ RAM ของตัวแปรประเภทต่างๆ และการใช้คีย์เวิร์ด volatile",
    "Digital & Analog I/O": "สับสนการตั้งค่า INPUT_PULLUP, ค่าจำกัดกระแสของพิน I/O หรือความละเอียดสเกลแรงดันไฟฟ้าที่ได้จาก ADC",
    "Time & Timing": "สับสนการทำงานแบบ Blocking ของ delay() และการเขียนโค้ดจับเวลาด้วย millis() และ micros() เพื่อแก้ปัญหา rollover",
    "Serial Communication": "สับสนขนาดบัฟเฟอร์ 64 ไบต์ของ UART, การแบ่งความต่างของ print กับ write หรือขีดจำกัดความเร็วของ SoftwareSerial",
    "I2C & SPI Protocols": "สับสนการแชร์บัสแบบ multi-device, ความต้านทาน pull-up บัส I2C, หรือสายควบคุม CS/SS บนโปรโตคอล SPI",
    "External Interrupts": "สับสนเงื่อนไข trigger แบบ RISING/FALLING/CHANGE, ข้อจำกัดในการเขียน ISR และการป้องกันปัญหา Race Condition",
    "Standard Libraries": "สับสนไลบรารี Servo ขา 9-10 (Timer 1), ขีดจำกัดชื่อไฟล์แบบ 8.3 ของ SD Card หรือความหน่วงในการตอบสนองจอ Character LCD",
    "MicroPython on Arduino": "สับสนการตั้งค่าโมดูล machine, ความแตกต่างของไวยากรณ์ Python Dynamic Typing และข้อจำกัดในการห้าม allocate dynamic memory ใน ISR",
    "Arduino IoT Cloud & API": "สับสนกลไกการซิงก์ตัวแปรแบบ On Change / Periodic, หน้าที่ของ callback function และการทำงานระบบรักษาความปลอดภัยบน cryptochip"
  };

  if (failedTopics.length === 0) {
    elements.gapAnalysisList.innerHTML = '<li><strong>ไม่พบช่องว่างความรู้ที่สำคัญ!</strong> คุณตอบคำถามหัวข้อต่างๆ ได้ถูกต้องและผ่านเกณฑ์ในทุกหมวดหมู่อย่างดีเยี่ยม</li>';
  } else {
    failedTopics.forEach(item => {
      const desc = gapDescriptions[item.topic] || "ต้องการทบทวนเนื้อหาและความเข้าใจเพิ่มเติม";
      const li = document.createElement('li');
      li.innerHTML = `<strong>หัวข้อ: ${item.topic} (ความแม่นยำ ${Math.round(item.percent)}%):</strong> ${desc}`;
      elements.gapAnalysisList.appendChild(li);
    });
  }

  // Populate Revision Topics (Top 5)
  elements.revisionTopicsList.innerHTML = '';
  const sortedFailed = [...failedTopics].sort((a,b) => a.percent - b.percent);
  
  const revisionSuggestions = [
    "หลีกเลี่ยงการใช้ String class ใน Uno/AVR ที่มี RAM น้อย เพื่อลดปัญหา RAM fragmentation และระบบแฮงก์",
    "ทบทวนการเขียนโค้ดแบบ non-blocking timing โดยเปรียบเทียบผลต่างของ millis() เพื่อป้องกันบั๊กเวลา rollover",
    "ศึกษาการแยกความต่างระหว่าง Serial.print() (ASCII) และ Serial.write() (Binary) เพื่อส่งค่าข้อมูลได้ถูกต้อง",
    "ทบทวนการประกาศ volatile สำหรับตัวแปรแชร์ระหว่าง ISR และ main loop เพื่อป้องกันคอมไพเลอร์ข้ามการอ่านค่าในแรม",
    "หลีกเลี่ยงการ allocate memory หรือจัดรูปแบบ String ภายใน ISR ของ MicroPython เพื่อเลี่ยงความเสียหายของ runtime"
  ];

  if (sortedFailed.length > 0) {
    for (let i = 0; i < Math.min(5, sortedFailed.length); i++) {
      const li = document.createElement('li');
      li.textContent = `ทบทวนและฝึกทำแบบทดสอบในหัวข้อ "${sortedFailed[i].topic}" ซ้ำเพิ่มเติมอย่างละเอียด`;
      elements.revisionTopicsList.appendChild(li);
    }
    let idx = 0;
    while (elements.revisionTopicsList.children.length < 5 && idx < revisionSuggestions.length) {
      const li = document.createElement('li');
      li.textContent = revisionSuggestions[idx];
      elements.revisionTopicsList.appendChild(li);
      idx++;
    }
  } else {
    revisionSuggestions.forEach(s => {
      const li = document.createElement('li');
      li.textContent = s;
      elements.revisionTopicsList.appendChild(li);
    });
  }

  // Show Results View
  elements.examView.classList.add('hide');
  elements.resultsView.classList.remove('hide');
  clearSavedState();
}

// Enter Review Mode to inspect correct answers and explanations
function toggleReviewMode() {
  state.isReviewMode = true;
  state.currentIndex = 0;
  
  elements.resultsView.classList.add('hide');
  elements.examView.classList.remove('hide');
  elements.reviewBar.classList.remove('hide');
  
  generateNavGrid();
  renderQuestion();
}

// Exit Review Mode and go back to results
function exitReviewMode() {
  state.isReviewMode = false;
  elements.reviewBar.classList.add('hide');
  elements.examView.classList.add('hide');
  elements.resultsView.classList.remove('hide');
}

// Restart App back to Dashboard
function restartApp() {
  state.mode = null;
  state.questions = [];
  state.currentIndex = 0;
  state.answers = {};
  state.bookmarks.clear();
  state.timeElapsed = 0;
  if (state.timerInterval) clearInterval(state.timerInterval);
  
  elements.resultsView.classList.add('hide');
  elements.examView.classList.add('hide');
  elements.timerBox.classList.add('hide');
  elements.dashboardView.classList.remove('hide');
  
  clearSavedState();
}

// Local Storage Helper functions
function saveStateToLocalStorage() {
  const data = {
    mode: state.mode,
    questionsIds: state.questions.map(q => q.id),
    currentIndex: state.currentIndex,
    answers: state.answers,
    bookmarks: Array.from(state.bookmarks),
    timeElapsed: state.timeElapsed
  };
  localStorage.setItem('arduino_learn_exam_state', JSON.stringify(data));
}

function clearSavedState() {
  localStorage.removeItem('arduino_learn_exam_state');
}

// Check if there is an uncompleted exam state in localStorage and ask to resume
function checkResumableState() {
  const saved = localStorage.getItem('arduino_learn_exam_state');
  if (!saved) return;

  try {
    const data = JSON.parse(saved);
    if (!data.mode || !data.questionsIds || data.questionsIds.length === 0) return;

    if (confirm('ระบบพบข้อสอบเดิมที่กำลังทำค้างอยู่ ต้องการกลับไปทำต่อหรือไม่?')) {
      state.mode = data.mode;
      state.currentIndex = data.currentIndex;
      state.answers = data.answers || {};
      state.bookmarks = new Set(data.bookmarks || []);
      state.timeElapsed = data.timeElapsed || 0;

      const allQs = [
        ...state.quizData.sections.A.questions,
        ...state.quizData.sections.B.questions,
        ...state.quizData.sections.C.questions,
        ...state.quizData.sections.D.questions
      ];

      state.questions = data.questionsIds.map(id => allQs.find(q => q.id === id)).filter(Boolean);

      elements.dashboardView.classList.add('hide');
      elements.resultsView.classList.add('hide');
      elements.examView.classList.remove('hide');

      if (state.mode !== 'practice') {
        elements.timerBox.classList.remove('hide');
        startTimer();
      } else {
        elements.timerBox.classList.add('hide');
      }

      generateNavGrid();
      renderQuestion();
    } else {
      clearSavedState();
    }
  } catch (e) {
    console.error('Error resuming state:', e);
    clearSavedState();
  }
}

// Expose public API
window.app = {
  startExam,
  toggleReviewMode,
  exitReviewMode,
  restartApp
};
