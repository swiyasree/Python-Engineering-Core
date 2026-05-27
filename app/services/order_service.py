
from app.models.orders import Order

def get_order(order_id: int) -> Order:
    return Order(
        order_id=order_id,
        name="Max",
        email="max@example.com",
        contact="213-789-3721",
        items=["Avocados", "Milk", "Bread", "Nutella"],
        total=22.75,
        location="2604 Augusta Dr, Denton, TX",
        payment_status="Paid"
    )

def get_payment_msg(order_id: int):
    order = get_order(order_id)
    if order.order_id == order_id:
        if order.payment_status == "Paid":
            return "Thankyou for your payment! Visit again!"
        else:
            return "Thankyou for your payment! Visit again!"

