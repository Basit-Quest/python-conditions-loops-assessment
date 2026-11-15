<p align="center"><img src="assets/banner.svg" alt="banner" width="100%"></p>

# Python Conditions & Loops Assessment

## 1. Project Overview

Two independent command-line applications solve scholarship decision-making and pharmacy sales reporting problems. Both use standard-library Python and validate their inputs.

| Task | File | Topic |
| --- | --- | --- |
| 1 — Student Scholarship Eligibility | `student_scholarship_system.py` | Conditional statements (`if`, `elif`, `else`) |
| 2 — Smart Pharmacy Inventory & Sales | `pharmacy_inventory_system.py` | `for` loops, `range()`, counters, accumulators |

![Project overview](assets/overview.svg)

## 2. Folder Structure

```text
python-conditions-loops-assessment/
├── student_scholarship_system.py
├── pharmacy_inventory_system.py
├── README.md
└── assets/                         # Documentation SVG diagrams
    ├── banner.svg
    ├── overview.svg
    ├── student_scholarship_system_flow.svg
    ├── pharmacy_inventory_system_flow.svg
    └── uml_diagram.svg
```

## 3. Task 1 — Student Scholarship Eligibility System

### Summary

The program collects one student's details, applies three mandatory scholarship conditions, and prints a complete evaluation report. It independently records **all** eligibility failures rather than stopping at the first.

### Rules / Requirements

- Valid academic marks: **0–100%**; scholarship minimum: **80%**.
- Valid attendance: **0–100%**; scholarship minimum: **85%**.
- Monthly family income must be **Rs. 50,000 or less** and never negative.
- If all requirements pass: **Full Scholarship** for marks **≥90%**, otherwise **Partial Scholarship** for marks **80% to below 90%**.
- If a requirement fails: **Not Eligible**, with every reason shown.

### Program Flow

![Scholarship program flow](assets/student_scholarship_system_flow.svg)

### Code Methods Description

| Function | Purpose |
| --- | --- |
| `get_nonempty_text()` | Reads and normalizes a nonblank student name. |
| `get_decimal_in_range()` | Validates percentages and nonnegative income. |
| `get_ineligibility_reasons()` | Builds a list of every unmet scholarship rule. |
| `get_scholarship_type()` | Selects full, partial, or no scholarship. |
| `print_evaluation_report()` | Prints details, classification, and reasons. |
| `main()` | Collects values and coordinates evaluation. |

### Input Validation

Empty names, invalid numeric text, `NaN`, infinity, out-of-range percentages, and negative income trigger clear errors and a repeat prompt. Numeric calculations use `decimal.Decimal`.

### Expected Results

- **Eligible, 90–100% marks:** Full Scholarship (if attendance and income also pass).
- **Eligible, 80–below 90% marks:** Partial Scholarship (if attendance and income also pass).
- **Any failed criterion:** Not Eligible with one to three explicit reasons.

## 4. Task 2 — Smart Pharmacy Inventory & Sales Management System

### Summary

A `for` loop processes the entered number of distinct medicines. For each medicine, the program validates a stock-and-sale record, rejects sales above available stock, updates remaining stock, and accumulates successful revenue.

### Rules / Requirements

- Ask for the number of medicines (**0 or more**); process each using `for` and `range()`.
- Collect name, available stock, unit price, and requested quantity sold.
- **Reject sales exceeding stock** without changing that medicine's stock or increasing revenue.
- Show revenue and remaining stock for an accepted sale; show remaining stock for a rejected sale.
- Warn and count restocking needs when **remaining stock < 10**. A rejected sale may still leave a low-stock warning.
- Print medicine count, total accepted sales revenue, and number of distinct medicines needing restock.

### Program Flow

![Pharmacy program flow](assets/pharmacy_inventory_system_flow.svg)

### Code Methods Description

| Function | Purpose |
| --- | --- |
| `get_nonnegative_integer()` | Validates medicine count, stock, and sold quantities. |
| `get_medicine_name()` | Rejects blank and case-insensitive duplicate names. |
| `get_unit_price()` | Validates a nonnegative price to two decimal places. |
| `process_medicine()` | Accepts or rejects one sale, computes remaining stock and restock flag. |
| `print_final_report()` | Prints processed count, total revenue, and restock count. |
| `main()` | Uses `range()`, the revenue accumulator, and restock counter. |

### Input Validation

Medicine counts, stock, and sale quantities must be whole numbers ≥0. Blank/duplicate medicine names, negative or nonnumeric prices, nonfinite values, and prices with more than two nonzero decimal places are rejected with repeat prompts. Zero price and zero sold quantity are permitted.

### Expected Results

- **Accepted sale:** Amount = price × quantity; remaining stock = original stock − quantity.
- **Rejected sale:** Revenue = Rs. 0.00 for that medicine; original stock stays unchanged.
- **Under 10 units left:** Low-stock warning and one addition to the restock count.
- **Zero medicines:** A final report with zero processed, revenue, and restocking needs.

## 5. UML Diagram

A **UML-style module diagram** is appropriate because both applications are procedural rather than class-based; it groups each source file with its constants, functions, and `main()`-initiated call chain.

![Procedural module diagram](assets/uml_diagram.svg)

## 6. Concepts and Techniques Used

- `if`, `elif`, `else` with inclusive and exclusive boundary conditions.
- `for` and `range()` for repeated medicine processing.
- Counters and revenue accumulators; arithmetic and comparison operators.
- `input()`, `print()`, helper functions, and formatted reports.
- `while`-based re-prompting for invalid inputs.
- `decimal.Decimal` for exact decimal arithmetic, money, and percentages.
- Lists for multiple scholarship rejection reasons; a set for unique medicine names.
- Named constants instead of embedded business thresholds.
- Standard library only; no external installation required.

## 7. How to Run

**Requirements:** Python **3.9+**; any Windows, macOS, or Linux terminal. No third-party packages.

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/python-conditions-loops-assessment.git
cd python-conditions-loops-assessment
```

Replace `YOUR_GITHUB_USERNAME` in the clone command and the author link with your actual GitHub username after publishing the repository.

```bash
# Task 1: scholarship evaluation
python student_scholarship_system.py

# Task 2: pharmacy sales
python pharmacy_inventory_system.py
```

**Alternate Python commands:** `python3 student_scholarship_system.py` and `python3 pharmacy_inventory_system.py` (macOS/Linux), or `py student_scholarship_system.py` and `py pharmacy_inventory_system.py` (Windows).

## 8. Sample Execution

The following outputs were captured from actual CLI runs with scripted standard input. Because the test runner supplies input without echoing it, consecutive prompts appear on the same line.

### Task 1 — Full scholarship (success)

**Inputs in order:** `Ali Khan`, `95`, `90`, `30000`

```text
UNIVERSITY SCHOLARSHIP ELIGIBILITY SYSTEM
Student name: Academic marks (%): Attendance (%): Monthly family income (Rs.): 
=================================================
           SCHOLARSHIP EVALUATION REPORT
=================================================
Student name          : Ali Khan
Academic marks        : 95.00%
Attendance            : 90.00%
Monthly family income : Rs. 30,000.00
-------------------------------------------------
Decision              : Full Scholarship
All mandatory eligibility criteria are satisfied.
=================================================
```

### Task 1 — Three unmet conditions (failure)

**Inputs in order:** `Noor`, `70`, `72`, `60000`

```text
UNIVERSITY SCHOLARSHIP ELIGIBILITY SYSTEM
Student name: Academic marks (%): Attendance (%): Monthly family income (Rs.): 
=================================================
           SCHOLARSHIP EVALUATION REPORT
=================================================
Student name          : Noor
Academic marks        : 70.00%
Attendance            : 72.00%
Monthly family income : Rs. 60,000.00
-------------------------------------------------
Decision              : Not Eligible
Reason(s) for ineligibility:
  1. Academic marks are below 80%.
  2. Attendance is below 85%.
  3. Monthly family income exceeds Rs. 50,000.
=================================================
```

### Task 2 — Accepted sale, rejected sale, and boundary case

**Inputs in order:** `3`; Paracetamol (`20`, `25.50`, `12`); Ibuprofen (`15`, `40`, `20`); Vitamin C (`10`, `15`, `0`).

```text
SMART PHARMACY INVENTORY & SALES SYSTEM
How many different medicines? 
--- Medicine 1 ---
Medicine name: Available stock (units): Price per unit (Rs.): Quantity sold (units): SALE ACCEPTED: Paracetamol | Sold: 12 | Amount: Rs. 306.00
Remaining stock: 8 unit(s)
LOW STOCK WARNING: Paracetamol is below 10 units.

--- Medicine 2 ---
Medicine name: Available stock (units): Price per unit (Rs.): Quantity sold (units): SALE REJECTED: Only 15 unit(s) of Ibuprofen available.
Remaining stock: 15 unit(s)

--- Medicine 3 ---
Medicine name: Available stock (units): Price per unit (Rs.): Quantity sold (units): SALE ACCEPTED: Vitamin C | Sold: 0 | Amount: Rs. 0.00
Remaining stock: 10 unit(s)

================================================
           PHARMACY DAILY SALES REPORT
================================================
Medicines processed         : 3
Total pharmacy revenue      : Rs. 306.00
Medicines requiring restock : 1
================================================
```

### Task 2 — Zero medicines (edge case)

**Input:** `0`

```text
SMART PHARMACY INVENTORY & SALES SYSTEM
How many different medicines? 
================================================
           PHARMACY DAILY SALES REPORT
================================================
Medicines processed         : 0
Total pharmacy revenue      : Rs. 0.00
Medicines requiring restock : 0
================================================
```

## 9. Test Cases

All **22** cases below were run against the actual Python scripts using standard input. Each completed with exit code 0 and the asserted output.

### Task 1 — Scholarship Tests

| # | Scenario | Inputs | Expected and verified result |
| --- | --- | --- | --- |
| 1 | Full scholarship | Ali Khan; 95, 90, 30000 | Full Scholarship |
| 2 | Partial scholarship / income cap | Sara Ahmed; 85, 90, 50000 | Partial Scholarship |
| 3 | Marks just below minimum | Ayesha; 79.99, 85, 50000 | Reject: marks below 80% |
| 4 | Attendance alone fails | Hamza; 90, 84.99, 50000 | Reject: attendance below 85% |
| 5 | Income alone fails | Fatima; 90, 85, 50000.01 | Reject: income above Rs. 50,000 |
| 6 | All three conditions fail | Noor; 70, 72, 60000 | All three rejection reasons |
| 7 | Two failed conditions | Umar; 75, 90, 70000 | Marks + income reasons |
| 8 | Exact full threshold | Zain; 90, 85, 50000 | Full Scholarship |
| 9 | Exact partial threshold | Hina; 80, 85, 50000 | Partial Scholarship |
| 10 | Upper percentages, zero income | Bilal; 100, 100, 0 | Full Scholarship |
| 11 | Invalid input recovery | Blank name; `abc`; 101; -1; `NaN`; -5; `Infinity`, then valid data | Validation errors; eventually Full Scholarship |
| 12 | Zero percentages + high income | Ahmed; 0, 0, 100000 | All three rejection reasons |

### Task 2 — Pharmacy Tests

| # | Scenario | Inputs | Expected and verified result |
| --- | --- | --- | --- |
| 1 | Mixed accepted/rejected sales | 3 medicines: Paracetamol, Ibuprofen, Vitamin C | Rs. 306.00; 1 restock; rejected oversell |
| 2 | Zero medicines | Count 0 | 0 processed; Rs. 0.00; 0 restocks |
| 3 | Exact restock threshold | 10 in stock; sell 0 | Remaining 10; no warning |
| 4 | Below restock threshold | 9 in stock; sell 0 | Remaining 9; 1 restock |
| 5 | Sell all available units | 10 in stock; sell 10 at Rs. 3 | Rs. 30.00; remaining 0; 1 restock |
| 6 | Rejected sale still low stock | 3 in stock; request 4 | Sale rejected; Rs. 0.00; 1 restock |
| 7 | Invalid values corrected | Count `x`, -1, 2.5; blank name; invalid stock/price/sold entries | Errors; final revenue Rs. 36.50 |
| 8 | Duplicate name corrected | `Zinc` then `zinc`, corrected to Vitamin D | Duplicate error; revenue Rs. 46.00 |
| 9 | Zero-priced medicine | 5 units at Rs. 0.00; sell 5 | Accepted; Rs. 0.00; 1 restock |
| 10 | Two low-stock medicines | A: 4 stock, sell 1; B: 5 stock, sell 1; price Rs. 10 each | Rs. 20.00; 2 restocks |

---

