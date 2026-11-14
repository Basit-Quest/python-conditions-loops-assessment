"""Evaluate a student's scholarship eligibility using conditional statements."""

import math


def get_nonempty_text(prompt):
    """Keep asking until the user enters meaningful text."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Invalid input: this field cannot be empty.")


def get_number(prompt, minimum=0, maximum=None):
    """Validate a numerical input and its permitted range."""
    while True:
        try:
            number = float(input(prompt).strip())
            if not math.isfinite(number):
                print("Invalid input: enter a finite number.")
            elif number < minimum or (maximum is not None and number > maximum):
                if maximum is None:
                    print(f"Invalid input: enter a number of at least {minimum:g}.")
                else:
                    print(f"Invalid input: enter a number between {minimum:g} and {maximum:g}.")
            else:
                return number
        except ValueError:
            print("Invalid input: please enter a valid number.")


def main():
    print("=" * 50)
    print("       STUDENT SCHOLARSHIP ELIGIBILITY SYSTEM")
    print("=" * 50)

    student_name = get_nonempty_text("Student name: ")
    academic_marks = get_number("Academic marks (%): ", 0, 100)
    attendance = get_number("Attendance (%): ", 0, 100)
    family_income = get_number("Monthly family income (Rs.): ", 0)

    # Each disqualifying condition is checked so the report explains all issues.
    reasons = []
    if academic_marks < 80:
        reasons.append("Academic marks are below 80%.")
    if attendance < 85:
        reasons.append("Attendance is below 85%.")
    if family_income > 50000:
        reasons.append("Monthly family income exceeds Rs. 50,000.")

    # Scholarship level depends on marks only after all requirements pass.
    if reasons:
        scholarship = "Not Eligible"
    elif academic_marks >= 90:
        scholarship = "Full Scholarship"
    elif academic_marks >= 80:
        scholarship = "Partial Scholarship"
    else:
        scholarship = "Not Eligible"

    print("\n" + "=" * 50)
    print("              SCHOLARSHIP EVALUATION REPORT")
    print("=" * 50)
    print(f"Student Name        : {student_name}")
    print(f"Academic Marks      : {academic_marks:.2f}%")
    print(f"Attendance          : {attendance:.2f}%")
    print(f"Monthly Family Income: Rs. {family_income:,.2f}")
    print(f"Scholarship Decision: {scholarship}")
    if reasons:
        print("Reason(s) for ineligibility:")
        for reason in reasons:
            print(f"  - {reason}")
    else:
        print("Reason              : All eligibility criteria satisfied.")
    print("=" * 50)


if __name__ == "__main__":
    main()
