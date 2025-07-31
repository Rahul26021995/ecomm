from models import Order, Product, Customer
from rules import apply_business_rules
from inventory import update_inventory
from reports import generate_report

def main():
    # Sample data
    customer = Customer("Alice", is_premium=True)
    products = [
        Product("Laptop", 1000.00, stock=5),
        Product("Mouse", 50.00, stock=10)
    ]
    order = Order(customer, products)

    # Apply business rules
    apply_business_rules(order)

    # Update inventory
    update_inventory(order)

    # Generate final report
    generate_report(order)

if __name__ == "__main__":
    main()
