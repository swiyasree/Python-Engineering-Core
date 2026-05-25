from app.services.user_service import get_user
from app.services.user_service import get_order

def get_user_route(user_id: int):
    user = get_user(user_id)

    return {
        "id": user.user_id,
        "name": user.name,
        "email": user.email
    }

def get_order_delivery_info(order_id: int):
    order = get_order(order_id)

    return {
        "id": order.order_id,
        "name": order.name,
        "email": order.email,
        "contact": order.contact,
        "items": order.items,
        "Purchase:total": order.total,
        "location": order.location,
        "payment status": order.payment_status
    }