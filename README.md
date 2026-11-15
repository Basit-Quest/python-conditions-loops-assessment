# Python Conditions & Loops Assessment

Two independent, terminal-based Python 3 applications demonstrate the use of conditional statements, loops, counters, accumulators, arithmetic, input validation, and clear reporting.

## Repository contents

```text
python-conditions-loops-assessment/
├── student_scholarship_system.py
├── pharmacy_inventory_system.py
└── README.md
```

No third-party libraries are required.

## Task 1 — Student Scholarship Eligibility System

Prompts for a student's name, academic marks (0–100%), attendance (0–100%), and monthly family income (Rs., nonnegative). The scholarship is awarded **only when all three** conditions hold:

- Marks **at least 80%**
- Attendance **at least 85%**
- Family income **at most Rs. 50,000** per month

Eligible students with marks **90% or above** receive a **Full Scholarship**; otherwise eligible students receive a **Partial Scholarship**. For ineligible students, the report lists **every** failed condition.

**Techniques:** `if` / `elif` / `else`, relational operators, lists to gather rejection reasons, and `while` loops with `try` / `except ValueError` for input validation.

### Sample execution: eligible

```text
Student name: Ayesha Khan
Academic marks (%): 93
Attendance (%): 90
Monthly family income (Rs.): 45000

SCHOLARSHIP EVALUATION REPORT
Student Name        : Ayesha Khan
Academic Marks      : 93.00%
Attendance          : 90.00%
Monthly Family Income: Rs. 45,000.00
Scholarship Decision: Full Scholarship
Reason              : All eligibility criteria satisfied.
```

### Sample execution: ineligible

```text
Student name: Ali Raza
Academic marks (%): 75
Attendance (%): 82
Monthly family income (Rs.): 65000

Scholarship Decision: Not Eligible
Reason(s) for ineligibility:
  - Academic marks are below 80%.
  - Attendance is below 85%.
  - Monthly family income exceeds Rs. 50,000.
```

## Task 2 — Smart Pharmacy Inventory & Sales Management System

Processes a specified number of different medicines with a `for` loop and `range()`. For each medicine, the user enters its name, starting stock, unit price, and desired quantity sold. If the requested quantity exceeds available stock, the sale is **rejected** and the stock stays unchanged; otherwise the program calculates its sale amount and subtracts the sold units. A **low-stock warning** appears whenever remaining stock is fewer than 10 units (including after a rejected sale). A counter tracks how many processed medicine entries require restocking. Finally, a daily report shows medicines processed, successful sales, total revenue, and medicines requiring restocking.

**Techniques:** `for`, `range()`, `if` / `else`, `while` for validated inputs, integers for stock/quantity, floats for unit prices, a revenue **accumulator** (`total_revenue += sale_amount`), and a restock **counter** (`restocking_count += 1`). Only accepted sales add revenue; quantity zero is permitted but not counted as a successful sale.

### Sample execution

```text
Number of different medicines: 2

--- Medicine 1 of 2 ---
Medicine name: Paracetamol
Available stock (units): 20
Price per unit (Rs.): 15
Quantity to sell (units): 12
Sale amount: Rs. 180.00
Medicine: Paracetamol
Remaining stock: 8 unit(s)
LOW-STOCK WARNING: Restocking required (below 10 units).

--- Medicine 2 of 2 ---
Medicine name: Vitamin C
Available stock (units): 6
Price per unit (Rs.): 25
Quantity to sell (units): 9
Sale rejected: only 6 unit(s) in stock.
Medicine: Vitamin C
Remaining stock: 6 unit(s)
LOW-STOCK WARNING: Restocking required (below 10 units).

DAILY PHARMACY REPORT
Total medicines processed : 2
Successful medicine sales : 1
Total pharmacy revenue    : Rs. 180.00
Medicines needing restock : 2
```

## Running the programs

1. Install **Python 3** and open this repository's folder in a terminal (or VS Code's integrated terminal).
2. Run the scholarship app:
   ```bash
   python student_scholarship_system.py
   ```
3. Run the pharmacy app:
   ```bash
   python pharmacy_inventory_system.py
   ```
   On some systems the command is `python3` instead of `python`.

Each script runs independently and needs no additional files or network connection.

## Validation and test scenarios

| Program | Scenario | Expected behavior |
|---|---|---|
| Scholarship | Marks 90, attendance 85, income 50000 | Full Scholarship (boundary values accepted) |
| Scholarship | Marks 80, attendance 85, income 50000 | Partial Scholarship |
| Scholarship | Marks 79, attendance 84, income 50001 | Not Eligible; three reasons |
| Scholarship | Blank name, text for marks, marks 110, negative income | Prompt again for the invalid entry |
| Pharmacy | 20 units, sell 12 at Rs. 15 | Rs. 180 revenue, 8 left, low-stock warning |
| Pharmacy | 6 units, request 9 | Sale rejected, 6 units left, no revenue, warning |
| Pharmacy | 10 units, sell 0 | Rs. 0 revenue, 10 left, no warning |
| Pharmacy | Negative stock, decimal quantity, invalid price | Prompt again for the invalid entry |


