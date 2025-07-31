def apply_business_rules(order):
    print("Applying business rules...")

    # Rule 1: Premium customers get 10% discount
    if order.customer.is_premium:
        order.discount = order.total * 0.10
        print(f"Applied 10% discount for premium customer: -${order.discount:.2f}")
    
    # Rule 2: Free shipping for orders over $500
    if order.total > 500:
        order.shipping_fee = 0
        print("Free shipping applied.")
    else:
        order.shipping_fee = 20
        print("Shipping fee applied: $20")

    # Update final total
    order.final_total = order.total - order.discount + order.shipping_fee
