# ecommerce/order.py

import uuid

def generate_order_id():
    return str(uuid.uuid4())
