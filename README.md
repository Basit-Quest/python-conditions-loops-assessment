# Python Functions and Lists Assessment

This repository contains two independent, interactive Python command-line programs for an assessment on **functions, strings, lists, and loops**. Both programs validate user input and show clear, readable results. No additional Python packages are required.

## Project structure

```text
python-functions-lists-assessment/
├── result_card_generator.py
├── class_marks_analyzer.py
└── README.md
```

## Program 1: Student Result Card Generator

`result_card_generator.py` asks for one student's name, roll number, and marks in five subjects: English, Mathematics, Science, Computer, and Economics. It displays the marks for each subject, total marks out of 500, overall percentage, letter grade, and final Pass/Fail status.

- The name is cleaned with `.strip()` and `.title()`.
- The roll number must contain **digits only**, verified using `.isdigit()`.
- Every subject mark must be between **0 and 100**.
- Percentage is calculated to **two decimal places**.
- A final result is **Fail** if **any subject mark is below 40**, even when the overall percentage is 50 or more.
- If all subject marks are at least 40, an overall percentage of at least 50 is required to pass.

### Grading policy

| Percentage | Grade |
|---|---|
| 90 and above | A+ |
| 80 to below 90 | A |
| 70 to below 80 | B |
| 60 to below 70 | C |
| 50 to below 60 | D |
| Below 50 | Fail |

**Important:** The final displayed letter grade is `Fail` whenever the student fails the subject-minimum rule or the overall percentage rule.

### Sample input

```text
Enter student name:   aLi  khan  
Enter roll number (digits only): 1024
Enter marks for English (0-100): 85
Enter marks for Mathematics (0-100): 90
Enter marks for Science (0-100): 78
Enter marks for Computer (0-100): 92
Enter marks for Economics (0-100): 80
```

### Sample output (main results)

```text
Student Name : Ali  Khan
Roll Number  : 1024
English                  85.00
Mathematics              90.00
Science                  78.00
Computer                 92.00
Economics                80.00
Total Marks  : 425.00 / 500
Percentage   : 85.00%
Letter Grade : A
Final Status : Pass
```

## Program 2: Class Marks Analyzer

`class_marks_analyzer.py` asks how many students are in the class, then collects one name and one mark per student. It uses the required **two separate lists** (`student_names` and `student_marks`) and `.append()` to store the data.

It reports the class average, highest and lowest marks (including **all** students tied at either extreme), number passing (**50 or above**), number failing (**below 50**), students scoring strictly above average, and all marks sorted from highest to lowest.

### Sample input

```text
How many students are in the class? 4
Enter name of student 1: Ali
Enter marks for Ali (0-100): 80
Enter name of student 2: Sara
Enter marks for Sara (0-100): 60
Enter name of student 3: Hamza
Enter marks for Hamza (0-100): 80
Enter name of student 4: Ayesha
Enter marks for Ayesha (0-100): 40
```

### Sample output (main results)

```text
Number of students : 4
Class average      : 65.00
Highest marks      : 80.00
Top student(s)     : Ali, Hamza
Lowest marks       : 40.00
Lowest student(s)  : Ayesha
Passing students   : 3
Failing students   : 1

Students above class average:
  Ali: 80.00
  Hamza: 80.00

All marks, highest to lowest:
  80.00
  80.00
  60.00
  40.00
```

## Python concepts and functions used

- **Functions:** `def`, parameters, `return`, and descriptive function names.
- **String handling:** `.strip()`, `.title()`, `.isdigit()`, and f-string formatting.
- **Lists:** creation with `[]`, `.append()`, `len()`, `sum()`, `max()`, `min()`, and `sorted()`.
- **Loops and conditions:** `for`, `while`, `if`, `elif`-style conditional decisions, and comparisons.
- **Input validation:** `try`/`except ValueError`, range checks, and repeated input prompts.
- **Extra useful functions:** `any()` and `zip()` in the result card, and `', '.join()` for class rankings.

Examples of custom functions include `get_valid_marks(subject)`, `calculate_percentage(total, max_total)`, `get_grade(percentage)`, `format_name(name)`, `get_valid_mark(student_name)`, and `show_class_analysis(student_names, student_marks)`.

## How to run

1. Install **Python 3** and make sure the `python` command works in your terminal.
2. Download or clone this repository and open a terminal in its folder.
3. Run either file independently:

```bash
python result_card_generator.py
```

```bash
python class_marks_analyzer.py
```

On some systems, use `python3` instead of `python`.

## Suggested test scenarios

| Program | Inputs to test | Expected behavior |
|---|---|---|
| Result card | Five marks of 95 | Grade A+, Pass |
| Result card | 100, 100, 100, 100, 39 | Fail (subject below 40) |
| Result card | Five marks of 40 | Fail (overall percentage 40%) |
| Result card | Invalid roll number such as `abc` | Re-prompts for digits |
| Result card | Invalid marks such as `-1`, `101`, or `hello` | Re-prompts for valid marks |
| Class analyzer | 80, 60, 80, 40 | Reports both students tied at highest marks |
| Class analyzer | 50, 49 | One pass, one fail |
| Class analyzer | 70, 70, 70 | No student above average; all tied for highest/lowest |
| Class analyzer | Class size `0` or invalid marks | Re-prompts without crashing |

## How to upload to GitHub

After creating a new **public** GitHub repository named `python-functions-lists-assessment`, open the project folder in VS Code's terminal and run:

```bash
git init
git add result_card_generator.py class_marks_analyzer.py README.md
git commit -m "Complete Python functions and lists assessment"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/python-functions-lists-assessment.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username. If you already cloned an empty repository from GitHub, `git remote add origin` may be unnecessary; verify using `git remote -v`.

## LMS submission checklist

- [ ] GitHub repository URL (publicly accessible)
- [ ] `result_card_generator.py`
- [ ] `class_marks_analyzer.py`
- [ ] `README.md`

Both programs are written as original, standalone examples and include comments for the important logic.
