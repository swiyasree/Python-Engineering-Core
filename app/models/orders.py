
class Order:
    def __init__(self, order_id: int, name: str, email: str,contact: str, items: list[str], total: float, location: str, payment_status: str):
        self.order_id = order_id
        self.name = name
        self.email = email
        self.contact = contact
        self.items = items
        self.total = total
        self.location = location
        self.payment_status = payment_status
        