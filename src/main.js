// Theme Toggle Logic
const toggleThemeBtn = document.getElementById('toggle-theme-btn');
toggleThemeBtn.addEventListener('click', () => {
  document.body.classList.toggle('dark-theme');
  localStorage.setItem('theme', document.body.classList.contains('dark-theme') ? 'dark' : 'light');
});

// Load saved theme
if (localStorage.getItem('theme') === 'light') {
  document.body.classList.remove('dark-theme');
} else {
  document.body.classList.add('dark-theme');
}

// Topic metadata
const topicNames = {
  1: "Introduction to Arduino & Hardware",
  2: "Arduino C Programming Basics",
  3: "Basic I/O Components",
  4: "Character LCD & I2C Interface",
  5: "LDR Light Sensors",
  6: "PIR Motion Sensors",
  7: "DHT11 Temperature & Humidity Sensor",
  8: "LM35 & HIH4030 Analog Sensors",
  9: "DS1302 Real-Time Clock",
  10: "SD Cards & Data Logging"
};

const topicDescs = {
  1: "Official boards, Arduino UNO specifications, pinout architecture, clock, and memory.",
  2: "C syntax, setup/loop, variables, memory data types, operators, and constants.",
  3: "Interfacing push buttons, piezo buzzers, electromagnetic relays, and transistor drivers.",
  4: "1602 Character LCD, I2C backplane interface, and LiquidCrystal_I2C libraries.",
  5: "Light Dependent Resistors (LDR), voltage dividers, analogRead resolution, and map().",
  6: "Passive Infrared (PIR) sensors, Fresnel lenses, range, and delay time adjustments.",
  7: "DHT11 temperature & humidity composite sensor, custom single-wire 40-bit protocol.",
  8: "LM35 linear temperature sensor, HIH4030 analog humidity, and compensation math.",
  9: "DS1302 Real-Time Clock, crystal oscillators, 3-wire interfaces, and Burst Mode.",
  10: "SPI bus protocol (MOSI/MISO/SCK/CS), SD card formatting, SD library, and CSV logging."
};

// Global App State
let allQuestions = [];
let activeQuizQuestions = [];
let userAnswers = {}; // questionIndex -> selectedOption/Text
let flaggedQuestions = {}; // questionIndex -> boolean
let activeQuestionIndex = 0;

// Fetch quiz data
async function loadQuizData() {
  try {
    const response = await fetch('/quiz_data.json');
    if (!response.ok) throw new Error("Failed to fetch quiz data.");
    const data = await response.json();
    
    // Flatten all questions into a single array for easier manipulation
    allQuestions = [
      ...data.mcqs.map(q => ({ ...q, type: 'mcq' })),
      ...data.tfs.map(q => ({ ...q, type: 'tf' })),
      ...data.scenarios.map(q => ({ ...q, type: 'scenario' })),
      ...data.shorts.map(q => ({ ...q, type: 'short' }))
    ];
    
    initializeDashboard();
    initializeConfigOptions();
  } catch (error) {
    console.error("Error loading quiz data:", error);
    alert("Could not load quiz questions. Please ensure you run Vite server correctly.");
  }
}

// Populate dashboard with Syllabus Units
function initializeDashboard() {
  const unitsList = document.getElementById('units-list');
  unitsList.innerHTML = '';
  
  for (let id = 1; id <= 10; id++) {
    const unitCard = document.createElement('div');
    unitCard.className = 'unit-item';
    unitCard.innerHTML = `
      <span class="unit-badge">Unit ${id}</span>
      <h4>${topicNames[id]}</h4>
      <p>${topicDescs[id]}</p>
    `;
    unitsList.appendChild(unitCard);
  }
}

// Populate Config Topic Dropdown
function initializeConfigOptions() {
  const configTopic = document.getElementById('config-topic');
  configTopic.innerHTML = '<option value="all">All Units</option>';
  
  for (let id = 1; id <= 10; id++) {
    const option = document.createElement('option');
    option.value = id.toString();
    option.textContent = `Unit ${id}: ${topicNames[id]}`;
    configTopic.appendChild(option);
  }
}

// Helper to shuffle arrays
function shuffleArray(array) {
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

// Screen navigation helper
function showScreen(screenId) {
  document.querySelectorAll('.screen').forEach(screen => {
    screen.classList.remove('active');
  });
  document.getElementById(screenId).classList.add('active');
  window.scrollTo(0, 0);
}

// Initialize active quiz state
function startQuiz(questions) {
  if (questions.length === 0) {
    alert("No questions match the selected filters. Please adjust your criteria.");
    return;
  }
  
  activeQuizQuestions = questions;
  userAnswers = {};
  flaggedQuestions = {};
  activeQuestionIndex = 0;
  
  updateSidebarProgress();
  buildSidebarNav();
  renderActiveQuestion();
  showScreen('screen-quiz');
}

// Build Sidebar question navigator buttons
function buildSidebarNav() {
  const navGrid = document.getElementById('question-nav-grid');
  navGrid.innerHTML = '';
  
  activeQuizQuestions.forEach((_, idx) => {
    const btn = document.createElement('button');
    btn.className = `q-nav-btn ${idx === 0 ? 'active' : ''}`;
    btn.textContent = idx + 1;
    btn.id = `q-nav-${idx}`;
    btn.addEventListener('click', () => {
      navigateToQuestion(idx);
    });
    navGrid.appendChild(btn);
  });
}

function navigateToQuestion(index) {
  // Update class of previous active
  const prevBtn = document.getElementById(`q-nav-${activeQuestionIndex}`);
  if (prevBtn) {
    prevBtn.classList.remove('active');
    // Set answered state
    if (userAnswers[activeQuestionIndex] !== undefined && userAnswers[activeQuestionIndex] !== '') {
      prevBtn.classList.add('answered');
    } else {
      prevBtn.classList.remove('answered');
    }
  }
  
  activeQuestionIndex = index;
  
  const currentBtn = document.getElementById(`q-nav-${activeQuestionIndex}`);
  if (currentBtn) {
    currentBtn.classList.add('active');
  }
  
  renderActiveQuestion();
  updateSidebarProgress();
}

function updateSidebarProgress() {
  const fill = document.getElementById('quiz-progress-fill');
  const text = document.getElementById('quiz-progress-text');
  
  const total = activeQuizQuestions.length;
  const answered = Object.keys(userAnswers).filter(k => userAnswers[k] !== undefined && userAnswers[k] !== '').length;
  
  const percentage = (answered / total) * 100;
  fill.style.width = `${percentage}%`;
  text.textContent = `Question ${activeQuestionIndex + 1} of ${total} (${answered} answered)`;
  
  // Disable/enable nav buttons
  document.getElementById('prev-question-btn').disabled = activeQuestionIndex === 0;
  document.getElementById('next-question-btn').disabled = activeQuestionIndex === total - 1;
}

// Render active question details
function renderActiveQuestion() {
  const container = document.getElementById('active-question-card');
  container.innerHTML = '';
  
  const q = activeQuizQuestions[activeQuestionIndex];
  if (!q) return;
  
  // Header with badges and flags
  const header = document.createElement('div');
  header.className = 'question-header';
  
  const badges = document.createElement('div');
  badges.className = 'question-badges';
  badges.innerHTML = `
    <span class="badge badge-topic">Unit ${q.topic_id}</span>
    <span class="badge badge-diff-${q.difficulty.toLowerCase()}">${q.difficulty}</span>
    <span class="badge" style="background-color: var(--border-color); color: var(--text-main); text-transform: uppercase; font-size: 0.7rem;">${q.type}</span>
  `;
  
  const flagBtn = document.createElement('button');
  flagBtn.className = `flag-question-btn ${flaggedQuestions[activeQuestionIndex] ? 'flagged' : ''}`;
  flagBtn.innerHTML = `
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"></path>
      <line x1="4" y1="22" x2="4" y2="15"></line>
    </svg>
    <span>${flaggedQuestions[activeQuestionIndex] ? 'Flagged' : 'Flag Question'}</span>
  `;
  flagBtn.addEventListener('click', () => {
    flaggedQuestions[activeQuestionIndex] = !flaggedQuestions[activeQuestionIndex];
    flagBtn.classList.toggle('flagged');
    flagBtn.querySelector('span').textContent = flaggedQuestions[activeQuestionIndex] ? 'Flagged' : 'Flag Question';
    
    const navBtn = document.getElementById(`q-nav-${activeQuestionIndex}`);
    if (navBtn) {
      navBtn.classList.toggle('flagged', flaggedQuestions[activeQuestionIndex]);
    }
  });
  
  header.appendChild(badges);
  header.appendChild(flagBtn);
  container.appendChild(header);
  
  // Scenario description if Scenario question
  if (q.type === 'scenario') {
    const scenarioBox = document.createElement('div');
    scenarioBox.className = 'scenario-block';
    scenarioBox.innerHTML = `<strong>Scenario Case Study</strong>${q.scenario}`;
    container.appendChild(scenarioBox);
  }
  
  // Question text
  const questionText = document.createElement('div');
  questionText.className = 'question-text-area';
  questionText.innerHTML = `<h3>${q.question}</h3>`;
  container.appendChild(questionText);
  
  // Options / Inputs area
  if (q.type === 'mcq' || q.type === 'tf') {
    const optionsList = document.createElement('div');
    optionsList.className = 'options-list';
    
    Object.entries(q.options).forEach(([key, val]) => {
      const optionItem = document.createElement('div');
      optionItem.className = `option-item ${userAnswers[activeQuestionIndex] === key ? 'selected' : ''}`;
      optionItem.innerHTML = `
        <span class="option-prefix">${key}</span>
        <span class="option-val">${val}</span>
      `;
      optionItem.addEventListener('click', () => {
        selectOption(key);
      });
      optionsList.appendChild(optionItem);
    });
    
    container.appendChild(optionsList);
  } else if (q.type === 'scenario' || q.type === 'short') {
    // Textarea input
    const inputContainer = document.createElement('div');
    inputContainer.className = 'short-answer-input-container';
    
    const textarea = document.createElement('textarea');
    textarea.placeholder = q.type === 'scenario' ? "Explain your analysis, troubleshooting diagnosis, and proposed resolution..." : "Write your explanation in your own words...";
    textarea.value = userAnswers[activeQuestionIndex] || '';
    textarea.addEventListener('input', (e) => {
      saveTextAnswer(e.target.value);
    });
    
    inputContainer.appendChild(textarea);
    container.appendChild(inputContainer);
  }
}

function selectOption(key) {
  userAnswers[activeQuestionIndex] = key;
  
  // Update UI selection state
  document.querySelectorAll('.option-item').forEach(item => {
    item.classList.remove('selected');
    if (item.querySelector('.option-prefix').textContent === key) {
      item.classList.add('selected');
    }
  });
  
  updateSidebarProgress();
  
  const navBtn = document.getElementById(`q-nav-${activeQuestionIndex}`);
  if (navBtn) {
    navBtn.classList.add('answered');
  }
}

function saveTextAnswer(text) {
  userAnswers[activeQuestionIndex] = text;
  updateSidebarProgress();
  
  const navBtn = document.getElementById(`q-nav-${activeQuestionIndex}`);
  if (navBtn) {
    if (text.trim() !== '') {
      navBtn.classList.add('answered');
    } else {
      navBtn.classList.remove('answered');
    }
  }
}

// Event Listeners for Nav buttons
document.getElementById('prev-question-btn').addEventListener('click', () => {
  if (activeQuestionIndex > 0) {
    navigateToQuestion(activeQuestionIndex - 1);
  }
});

document.getElementById('next-question-btn').addEventListener('click', () => {
  if (activeQuestionIndex < activeQuizQuestions.length - 1) {
    navigateToQuestion(activeQuestionIndex + 1);
  }
});

// Configure Custom Practice Screen triggers
document.getElementById('custom-quiz-btn').addEventListener('click', () => {
  showScreen('screen-config');
});

document.getElementById('config-back-btn').addEventListener('click', () => {
  showScreen('screen-dashboard');
});

// Handle config form submission
document.getElementById('config-form').addEventListener('submit', (e) => {
  e.preventDefault();
  
  const formData = new FormData(e.target);
  const selectedTypes = formData.getAll('type');
  const selectedDiffs = formData.getAll('difficulty');
  const selectedTopic = formData.get('topic');
  const limitValue = formData.get('limit');
  
  // Filter questions
  let filtered = allQuestions.filter(q => {
    // Check type
    if (!selectedTypes.includes(q.type)) return false;
    // Check difficulty
    if (!selectedDiffs.includes(q.difficulty)) return false;
    // Check unit
    if (selectedTopic !== 'all' && q.topic_id.toString() !== selectedTopic) return false;
    return true;
  });
  
  // Shuffle for variety
  filtered = shuffleArray(filtered);
  
  // Apply limit
  if (limitValue !== 'all') {
    const limit = parseInt(limitValue);
    filtered = filtered.slice(0, limit);
  }
  
  startQuiz(filtered);
});

// Direct Start Full Quiz Button
document.getElementById('start-quiz-btn').addEventListener('click', () => {
  // Select all 330 questions, shuffle them
  const shuffled = shuffleArray(allQuestions);
  startQuiz(shuffled);
});

// Submit Quiz Trigger
document.getElementById('submit-quiz-btn').addEventListener('click', () => {
  const total = activeQuizQuestions.length;
  const answered = Object.keys(userAnswers).filter(k => userAnswers[k] !== undefined && userAnswers[k] !== '').length;
  
  if (answered < total) {
    const confirmSubmit = confirm(`You have answered ${answered} of ${total} questions. Are you sure you want to submit the quiz?`);
    if (!confirmSubmit) return;
  }
  
  evaluateQuizResults();
});

// Results calculation & rendering
function evaluateQuizResults() {
  let score = 0;
  const total = activeQuizQuestions.length;
  
  // Breakdown statistics
  const breakdown = {
    mcq: { correct: 0, total: 0 },
    tf: { correct: 0, total: 0 },
    scenario: { correct: 0, total: 0 },
    short: { correct: 0, total: 0 }
  };
  
  // Topic incorrect tracking for Gap Analysis
  const topicStats = {}; // topic_id -> { correct: 0, total: 0 }
  for (let i = 1; i <= 10; i++) {
    topicStats[i] = { correct: 0, total: 0 };
  }
  
  const wrongQuestions = [];
  
  activeQuizQuestions.forEach((q, idx) => {
    const userAns = userAnswers[idx];
    const type = q.type;
    
    breakdown[type].total++;
    topicStats[q.topic_id].total++;
    
    let isCorrect = false;
    if (type === 'mcq' || type === 'tf') {
      if (userAns && userAns.toLowerCase() === q.answer.toLowerCase()) {
        isCorrect = true;
      }
    } else {
      // For scenario/short text questions, since it's client-side, we score as 'correct'
      // if they write anything substantial (length > 10 chars), but mark it for self-review.
      if (userAns && userAns.trim().length > 10) {
        isCorrect = true;
      }
    }
    
    if (isCorrect) {
      score++;
      breakdown[type].correct++;
      topicStats[q.topic_id].correct++;
    } else {
      wrongQuestions.push({
        questionObj: q,
        userAnswer: userAns || "No answer provided",
        questionNum: idx + 1
      });
    }
  });
  
  // Calculate percentage
  const percent = total > 0 ? Math.round((score / total) * 100) : 0;
  
  // Update Results Page Elements
  document.getElementById('result-score-percent').textContent = `${percent}%`;
  document.getElementById('result-score-fraction').textContent = `${score}/${total} Points`;
  
  // Animate score ring
  const circle = document.getElementById('score-ring-fill');
  const strokeDash = 282.7; // 2 * pi * r (r=45)
  const offset = strokeDash - (percent / 100) * strokeDash;
  circle.style.strokeDashoffset = offset;
  
  const isPassed = percent >= 80;
  
  if (isPassed) {
    document.getElementById('result-status-title').textContent = "Congratulations! You Passed!";
    document.getElementById('result-message').textContent = "Excellent work! You demonstrated solid proficiency in Arduino principles, hardware limits, and data logging.";
    document.getElementById('result-badge-passing').style.display = 'inline-block';
    document.getElementById('result-badge-failed').style.display = 'none';
  } else {
    document.getElementById('result-status-title').textContent = "Keep Studying!";
    document.getElementById('result-message').textContent = "You did not achieve the required 80% passing mark. Review your knowledge gaps and try again.";
    document.getElementById('result-badge-failed').style.display = 'inline-block';
    document.getElementById('result-badge-passing').style.display = 'none';
  }
  
  // Render Section breakdown
  const breakdownList = document.getElementById('score-breakdown-list');
  breakdownList.innerHTML = '';
  
  const labelNames = { mcq: "Multiple Choice", tf: "True / False", scenario: "Scenarios", short: "Short Answers" };
  
  Object.entries(breakdown).forEach(([type, stats]) => {
    if (stats.total === 0) return;
    const typePercent = Math.round((stats.correct / stats.total) * 100);
    
    const item = document.createElement('div');
    item.className = 'breakdown-item';
    item.innerHTML = `
      <span class="breakdown-lbl">${labelNames[type]}</span>
      <div class="breakdown-bar">
        <div class="breakdown-bar-fill" style="width: ${typePercent}%"></div>
      </div>
      <span class="breakdown-val">${stats.correct}/${stats.total} (${typePercent}%)</span>
    `;
    breakdownList.appendChild(item);
  });
  
  // Render Knowledge Gap Analysis
  const gapContent = document.getElementById('gap-analysis-content');
  gapContent.innerHTML = '';
  
  let gapCount = 0;
  Object.entries(topicStats).forEach(([id, stats]) => {
    if (stats.total === 0) return;
    const topicPercent = (stats.correct / stats.total) * 100;
    
    if (topicPercent < 80) {
      gapCount++;
      const topicId = parseInt(id);
      const isCritical = topicPercent < 50;
      
      const gapItem = document.createElement('div');
      gapItem.className = `gap-topic-item ${isCritical ? 'critical' : 'warning'}`;
      gapItem.innerHTML = `
        <div class="gap-header">
          <span>Unit ${topicId}: ${topicNames[topicId]}</span>
          <span>Score: ${Math.round(topicPercent)}% (${isCritical ? 'CRITICAL REVIEW' : 'WEAK AREA'})</span>
        </div>
        <div class="gap-desc">${topicDescs[topicId]}</div>
      `;
      gapContent.appendChild(gapItem);
    }
  });
  
  if (gapCount === 0) {
    gapContent.innerHTML = '<div class="alert alert-success" style="color: var(--success)">Excellent! No significant knowledge gaps detected. You have a well-rounded understanding of the material.</div>';
  }
  
  // Render review questions list
  const reviewList = document.getElementById('review-questions-list');
  reviewList.innerHTML = '';
  
  if (wrongQuestions.length === 0) {
    reviewList.innerHTML = '<p class="text-muted">No incorrect answers to review. Perfect score!</p>';
  } else {
    wrongQuestions.forEach(item => {
      const q = item.questionObj;
      const reviewItem = document.createElement('div');
      reviewItem.className = 'review-item';
      
      let answerDetail = '';
      if (q.type === 'mcq' || q.type === 'tf') {
        const userChoiceText = q.options[item.userAnswer] || item.userAnswer;
        const correctChoiceText = q.options[q.answer];
        
        answerDetail = `
          <div class="review-answers-compare">
            <div class="review-answer-box answer-box-wrong">
              <strong>Your Answer (${item.userAnswer})</strong>
              ${userChoiceText}
            </div>
            <div class="review-answer-box answer-box-correct">
              <strong>Correct Answer (${q.answer})</strong>
              ${correctChoiceText}
            </div>
          </div>
        `;
      } else {
        answerDetail = `
          <div class="review-answers-compare">
            <div class="review-answer-box answer-box-wrong">
              <strong>Your Response</strong>
              ${item.userAnswer}
            </div>
            <div class="review-answer-box answer-box-correct">
              <strong>Reference/Expected Answer</strong>
              ${q.answer}
            </div>
          </div>
        `;
      }
      
      reviewItem.innerHTML = `
        <div class="question-badges" style="margin-bottom: 0.75rem;">
          <span class="badge badge-topic">Unit ${q.topic_id}</span>
          <span class="badge badge-diff-${q.difficulty.toLowerCase()}">${q.difficulty}</span>
        </div>
        <h4>Q${item.questionNum}: ${q.question}</h4>
        ${q.type === 'scenario' ? `<p class="scenario-block" style="font-size: 0.85rem;"><strong>Scenario</strong>${q.scenario}</p>` : ''}
        ${answerDetail}
        ${q.explanation ? `
          <div class="review-explanation">
            <strong>Explanation</strong>
            ${q.explanation}
          </div>
        ` : ''}
      `;
      reviewList.appendChild(reviewItem);
    });
  }
  
  showScreen('screen-results');
}

// Restart Quiz and Dashboard triggers
document.getElementById('restart-quiz-btn').addEventListener('click', () => {
  // Restart with same questions
  const shuffled = shuffleArray(activeQuizQuestions);
  startQuiz(shuffled);
});

document.getElementById('dashboard-btn').addEventListener('click', () => {
  showScreen('screen-dashboard');
});

// Initialize on load
loadQuizData();
