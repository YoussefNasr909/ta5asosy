import json
import os
import sys

from generate_networking import networking_questions
from generate_database import database_questions
from generate_sql import sql_questions

# Load original questions
with open('data/original_questions.json', 'r', encoding='utf-8') as f:
    original_questions = json.load(f)

print(f"Loaded {len(original_questions)} original questions.")
print(f"Loaded {len(networking_questions)} generated networking questions.")
print(f"Loaded {len(database_questions)} generated database questions.")
print(f"Loaded {len(sql_questions)} generated SQL questions.")

all_questions = original_questions + networking_questions + database_questions + sql_questions

os.makedirs('data', exist_ok=True)
os.makedirs('src/data', exist_ok=True)

with open('data/question_bank.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

with open('src/data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f"\nSuccessfully built combined question bank with {len(all_questions)} questions!")
