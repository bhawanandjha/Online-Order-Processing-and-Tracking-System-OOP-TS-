def find_order(data, order_id):
    for order in data:
        if order['id'] == order_id:
            return order
    return None
