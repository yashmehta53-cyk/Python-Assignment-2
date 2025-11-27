"""
Gradebook Analyzer
Author: Yash Mehta
Date: 27-11-2025
"""

import csv

PASS_MARK = 40

def get_marks_manual():
    marks = {}
    while True:
        name = input("Student name (Enter to stop): ").strip()
        if not name:
            break
        try:
            score = float(input(f"Marks for {name}: "))
            marks[name] = score
        except:
            print("Invalid marks, try again.")
    return marks

def get_marks_csv():
    marks = {}
    filename = input("CSV filename: ").strip()
    try:
        with open(filename, newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 2:
                    continue
                try:
                    marks[row[0]] = float(row[1])
                except:
                    continue
    except FileNotFoundError:
        print("File not found.")
    return marks

def average(marks): return sum(marks.values()) / len(marks) if marks else 0

def median(marks):
    vals = sorted(marks.values())
    n = len(vals)
    if n == 0: return 0
    mid = n // 2
    return vals[mid] if n % 2 == 1 else (vals[mid-1] + vals[mid]) / 2

def assign_grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else: return "F"

def main():
    print("1) Manual Entry  2) Load CSV  3) Exit")
    choice = input("Choice: ").strip()
    if choice == "1":
        marks = get_marks_manual()
    elif choice == "2":
        marks = get_marks_csv()
    else:
        print("Goodbye!")
        return

    if not marks:
        print("No marks entered.")
        return

    print(f"Average: {average(marks):.2f}")
    print(f"Median: {median(marks):.2f}")

    grades = {name: assign_grade(score) for name, score in marks.items()}

    dist = {g: list(grades.values()).count(g) for g in "ABCDF"}
    print("Grades distribution:", dist)

    passed = [n for n, s in marks.items() if s >= PASS_MARK]
    failed = [n for n, s in marks.items() if s < PASS_MARK]

    print(f"Passed ({len(passed)}): {', '.join(passed)}")
    print(f"Failed ({len(failed)}): {', '.join(failed)}")

    print("Name\tMarks\tGrade")
    print("-------------------------")
    for name, score in marks.items():
        print(f"{name}\t{score}\t{grades[name]}")

if __name__ == "__main__":
    main()