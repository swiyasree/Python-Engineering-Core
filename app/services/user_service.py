from app.models.user import User
from app.models.user import Order

def get_user(user_id: int) -> User:
    return User(
        user_id=user_id,
        name="Sree",
        email="sree@example.com"
    )

def get_order(order_id: int) -> User:
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