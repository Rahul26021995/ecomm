def update_inventory(order):
    print("Updating inventory...")
    for product in order.items:
        if product.stock <= 0:
            print(f"ERROR: {product.name} is out of stock!")
        else:
            product.stock -= 1
            print(f"{product.name} stock reduced to {product.stock}")
