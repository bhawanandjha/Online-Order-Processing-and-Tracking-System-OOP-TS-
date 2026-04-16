from scripts.week1_basics import welcome
from scripts.week2_io import get_order_input
from scripts.week3_conditions import validate_input
from scripts.week4_loops import display_orders
from scripts.week5_functions import generate_id
from scripts.week7_data_structures import create_order
from scripts.week8_advanced_ds import find_order
from scripts.week10_files import load, save
from scripts.week11_exceptions import safe_input
from scripts.week12_analytics import report

def main():
    welcome()
    data = load()

    while True:
        print("\n1. Place Order")
        print("2. View Orders")
        print("3. Update Status")
        print("4. Report")
        print("5. Exit")

        choice = safe_input()

        if choice == 1:
            name, item = get_order_input()
            if validate_input(name, item):
                oid = generate_id(data)
                order = create_order(oid, name, item)
                data.append(order)
                save(data)

        elif choice == 2:
            display_orders(data)

        elif choice == 3:
            oid = int(input("Order ID: "))
            order = find_order(data, oid)
            if order:
                order['status'] = input("New Status: ")
                save(data)

        elif choice == 4:
            report(data)

        elif choice == 5:
            break

if __name__ == "__main__":
    main()
