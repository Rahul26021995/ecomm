def generate_report(order):
    print("\n--- Order Summary Report ---")
    print(f"Customer: {order.customer.name}")
    print("Items:")
    for product in order.items:
        print(f"- {product.name}: ${product.price:.2f}")
    print(f"Subtotal: ${order.total:.2f}")
    print(f"Discount: -${order.discount:.2f}")
    print(f"Shipping: ${order.shipping_fee:.2f}")
    print(f"Final Total: ${order.final_total:.2f}")
    print("----------------------------")
