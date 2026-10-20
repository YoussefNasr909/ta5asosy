import json
import sys

def validate():
    file_path = 'data/question_bank.json'
    with open(file_path, 'r', encoding='utf-8') as f:
        questions = json.load(f)

    print(f"--- Running Comprehensive Question Bank Validation ---")
    print(f"Total questions loaded: {len(questions)}")

    errors = []
    warnings = []

    valid_topics = {"Computer Networking", "Database Fundamentals", "SQL"}
    valid_difficulties = {"easy", "medium", "hard"}
    valid_source_types = {"pdf", "generated"}

    seen_ids = set()
    seen_questions = {}

    topic_counts = {t: 0 for t in valid_topics}
    source_counts = {"pdf": 0, "generated": 0}
    difficulty_counts = {d: 0 for d in valid_difficulties}

    for i, q in enumerate(questions):
        idx_label = f"Item #{i+1} (ID: {q.get('id', 'MISSING')})"

        # 1. Check ID
        qid = q.get('id')
        if not qid or not isinstance(qid, str) or not qid.strip():
            errors.append(f"{idx_label}: Missing or invalid 'id'")
        elif qid in seen_ids:
            errors.append(f"{idx_label}: Duplicate 'id' detected: {qid}")
        else:
            seen_ids.add(qid)

        # 2. Check Question text
        q_text = q.get('question')
        if not q_text or not isinstance(q_text, str) or not q_text.strip():
            errors.append(f"{idx_label}: Missing or empty 'question' text")
        else:
            norm_q = " ".join(q_text.strip().lower().split())
            if norm_q in seen_questions:
                warnings.append(f"{idx_label}: Potential duplicate question text matches {seen_questions[norm_q]}")
            else:
                seen_questions[norm_q] = qid

        # 3. Check Topic
        topic = q.get('topic')
        if topic not in valid_topics:
            errors.append(f"{idx_label}: Invalid topic '{topic}'. Must be one of {valid_topics}")
        else:
            topic_counts[topic] += 1

        # 4. Check Subtopic
        subtopic = q.get('subtopic')
        if not subtopic or not isinstance(subtopic, str) or not subtopic.strip():
            errors.append(f"{idx_label}: Missing or empty 'subtopic'")

        # 5. Check Options
        options = q.get('options')
        if not isinstance(options, list) or len(options) != 4:
            errors.append(f"{idx_label}: Must have exactly 4 options. Found: {len(options) if isinstance(options, list) else type(options)}")
        else:
            option_ids = set()
            for opt_idx, opt in enumerate(options):
                if not isinstance(opt, dict):
                    errors.append(f"{idx_label}: Option #{opt_idx+1} is not an object")
                    continue
                opt_id = opt.get('id')
                opt_text = opt.get('text')
                if opt_id not in {'A', 'B', 'C', 'D'}:
                    errors.append(f"{idx_label}: Invalid option id '{opt_id}'")
                if opt_id in option_ids:
                    errors.append(f"{idx_label}: Duplicate option id '{opt_id}'")
                option_ids.add(opt_id)

                if not opt_text or not isinstance(opt_text, str) or not opt_text.strip():
                    errors.append(f"{idx_label}: Option '{opt_id}' has empty text")

        # 6. Check Correct Answer
        correct = q.get('correctAnswer')
        if correct not in {'A', 'B', 'C', 'D'}:
            errors.append(f"{idx_label}: Invalid correctAnswer '{correct}'. Must be A, B, C, or D")
        elif isinstance(options, list):
            valid_opt_ids = {opt.get('id') for opt in options if isinstance(opt, dict)}
            if correct not in valid_opt_ids:
                errors.append(f"{idx_label}: correctAnswer '{correct}' not found in available options {valid_opt_ids}")

        # 7. Check Explanation
        explanation = q.get('explanation')
        if not explanation or not isinstance(explanation, str) or not explanation.strip():
            errors.append(f"{idx_label}: Missing or empty 'explanation'")

        # 8. Check Difficulty
        diff = q.get('difficulty')
        if diff not in valid_difficulties:
            errors.append(f"{idx_label}: Invalid difficulty '{diff}'. Must be one of {valid_difficulties}")
        else:
            difficulty_counts[diff] += 1

        # 9. Check Source Type
        source_type = q.get('sourceType')
        if source_type not in valid_source_types:
            errors.append(f"{idx_label}: Invalid sourceType '{source_type}'. Must be 'pdf' or 'generated'")
        else:
            source_counts[source_type] += 1

        # 10. Check Source File
        source_file = q.get('sourceFile')
        if source_type == 'pdf':
            if not source_file or not isinstance(source_file, str) or not source_file.endswith('.pdf'):
                errors.append(f"{idx_label}: PDF source requires a valid sourceFile ending with .pdf, got: '{source_file}'")

    print("\n--- Validation Statistics ---")
    print(f"Total Questions: {len(questions)}")
    print(f"By Source Type:")
    for st, c in source_counts.items():
        print(f"  - {st}: {c}")
    print(f"By Topic:")
    for t, c in topic_counts.items():
        print(f"  - {t}: {c}")
    print(f"By Difficulty:")
    for d, c in difficulty_counts.items():
        print(f"  - {d}: {c}")

    if warnings:
        print(f"\n[!] Warnings ({len(warnings)}):")
        for w in warnings[:10]:
            print(f"  - {w}")

    if errors:
        print(f"\n[X] Validation FAILED with {len(errors)} errors:")
        for e in errors[:20]:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("\n[OK] All validation checks PASSED successfully! 0 errors detected.")

if __name__ == '__main__':
    validate()
