# -*- coding: utf-8 -*-
import json
import sys

def main():
    try:
        with open("quiz_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading JSON: {e}")
        sys.exit(1)

    print("--- Verifying Arduino Quiz Data ---")
    
    sections = data.get("sections", {})
    mcqs = sections.get("A", {}).get("questions", [])
    tfs = sections.get("B", {}).get("questions", [])
    scenarios = sections.get("C", {}).get("questions", [])
    shorts = sections.get("D", {}).get("questions", [])

    print(f"MCQs: {len(mcqs)}")
    print(f"True/False: {len(tfs)}")
    print(f"Scenarios: {len(scenarios)}")
    print(f"Short Answers: {len(shorts)}")
    
    errors = []

    # Check counts
    if len(mcqs) != 150:
        errors.append(f"Expected 150 MCQs, got {len(mcqs)}")
    if len(tfs) != 60:
        errors.append(f"Expected 60 T/Fs, got {len(tfs)}")
    if len(scenarios) != 60:
        errors.append(f"Expected 60 Scenarios, got {len(scenarios)}")
    if len(shorts) != 60:
        errors.append(f"Expected 60 Short Answers, got {len(shorts)}")

    # Check MCQ difficulty distribution
    easy_count = sum(1 for q in mcqs if q.get("difficulty") == "Easy")
    medium_count = sum(1 for q in mcqs if q.get("difficulty") == "Medium")
    hard_count = sum(1 for q in mcqs if q.get("difficulty") == "Hard")

    print(f"MCQ Difficulty Distribution: Easy={easy_count}, Medium={medium_count}, Hard={hard_count}")

    if easy_count != 45:
        errors.append(f"Expected 45 Easy MCQs, got {easy_count}")
    if medium_count != 75:
        errors.append(f"Expected 75 Medium MCQs, got {medium_count}")
    if hard_count != 30:
        errors.append(f"Expected 30 Hard MCQs, got {hard_count}")

    # Check fields for MCQs
    for idx, q in enumerate(mcqs):
        q_id = q.get("id", f"MCQ_INDEX_{idx}")
        required_fields = ["id", "topic", "learning_objective", "difficulty", "question", "options", "correct_answer", "explanation"]
        for field in required_fields:
            if field not in q or not q[field]:
                errors.append(f"{q_id} is missing field: {field}")
        if len(q.get("options", [])) != 4:
            errors.append(f"{q_id} does not have exactly 4 options")
        if q.get("correct_answer") not in ["A", "B", "C", "D"]:
            errors.append(f"{q_id} has invalid correct_answer: {q.get('correct_answer')}")

    # Check fields for T/Fs
    for idx, q in enumerate(tfs):
        q_id = q.get("id", f"TF_INDEX_{idx}")
        required_fields = ["id", "topic", "learning_objective", "difficulty", "question", "correct_answer", "explanation"]
        for field in required_fields:
            if field not in q or not q[field]:
                errors.append(f"{q_id} is missing field: {field}")
        if q.get("correct_answer") not in ["True", "False"]:
            errors.append(f"{q_id} has invalid correct_answer: {q.get('correct_answer')}")

    # Check fields for Scenarios
    for idx, q in enumerate(scenarios):
        q_id = q.get("id", f"SCENARIO_INDEX_{idx}")
        required_fields = ["id", "topic", "learning_objective", "difficulty", "scenario", "question", "options", "correct_answer", "explanation"]
        for field in required_fields:
            if field not in q or not q[field]:
                errors.append(f"{q_id} is missing field: {field}")
        if len(q.get("options", [])) != 4:
            errors.append(f"{q_id} does not have exactly 4 options")
        if q.get("correct_answer") not in ["A", "B", "C", "D"]:
            errors.append(f"{q_id} has invalid correct_answer: {q.get('correct_answer')}")

    # Check fields for Short Answers
    for idx, q in enumerate(shorts):
        q_id = q.get("id", f"SHORT_INDEX_{idx}")
        required_fields = ["id", "topic", "learning_objective", "difficulty", "question", "expected_answer"]
        for field in required_fields:
            if field not in q or not q[field]:
                errors.append(f"{q_id} is missing field: {field}")

    if errors:
        print("\nVerification FAILED with the following errors:")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)
    else:
        print("\nVerification PASSED! All conditions met.")

if __name__ == "__main__":
    main()
