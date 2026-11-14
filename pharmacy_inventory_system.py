"""Record medicine sales, track remaining stock, and summarize revenue."""

import math


def get_name(prompt):
    """Reject blank names."""
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print("Invalid input: medicine name cannot be empty.")


def get_whole_number(prompt, minimum=0):
    """Read a nonnegative integer (or a positive integer when required)."""
    while True:
        try:
            value = int(input(prompt).strip())
            if value < minimum:
                print(f"Invalid input: enter a whole number of at least {minimum}.")
            else:
                return value
        except ValueError:
            print("Invalid input: enter a whole number.")


def get_price(prompt):
    """Read a valid, finite price greater than zero."""
    while True:
        try:
            price = float(input(prompt).strip())
            if not math.isfinite(price) or price <= 0:
                print("Invalid input: price must be a positive, finite number.")
            else:
                return price
        except ValueError:
            print("Invalid input: enter a valid price.")


def main():
    print("=" * 52)
    print("       SMART PHARMACY INVENTORY & SALES")
    print("=" * 52)
    medicine_count = get_whole_number("Number of different medicines: ", 1)
    total_revenue = 0.0  # Accumulator
    restocking_count = 0  # Counter
    successful_sales = 0

    # range() processes exactly the requested number of medicines.
    for medicine_number in range(1, medicine_count + 1):
        print(f"\n--- Medicine {medicine_number} of {medicine_count} ---")
        medicine_name = get_name("Medicine name: ")
        available_stock = get_whole_number("Available stock (units): ")
        unit_price = get_price("Price per unit (Rs.): ")
        quantity_sold = get_whole_number("Quantity to sell (units): ")

        if quantity_sold > available_stock:
            print(f"Sale rejected: only {available_stock} unit(s) in stock.")
            remaining_stock = available_stock
            sale_amount = 0.0
        else:
            sale_amount = unit_price * quantity_sold
            remaining_stock = available_stock - quantity_sold
            total_revenue += sale_amount
            if quantity_sold > 0:
                successful_sales += 1
            print(f"Sale amount: Rs. {sale_amount:,.2f}")

        print(f"Medicine: {medicine_name}")
        print(f"Remaining stock: {remaining_stock} unit(s)")
        if remaining_stock < 10:
            print("LOW-STOCK WARNING: Restocking required (below 10 units).")
            restocking_count += 1

    print("\n" + "=" * 52)
    print("                  DAILY PHARMACY REPORT")
    print("=" * 52)
    print(f"Total medicines processed : {medicine_count}")
    print(f"Successful medicine sales : {successful_sales}")
    print(f"Total pharmacy revenue    : Rs. {total_revenue:,.2f}")
    print(f"Medicines needing restock : {restocking_count}")
    print("=" * 52)


if __name__ == "__main__":
    main()
