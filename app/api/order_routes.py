from fastapi import FastAPI
from app.services.order_service import get_order
from app.services.order_service import get_payment_msg

app = FastAPI()

@app.get("/")
def get_order_delivery_info(order_id: int):
    order = get_order(order_id)

    return {
        "id": order.order_id,
        "name": order.name,
        "email": order.email,
        "contact": order.contact,
        "items": order.items,
        "Purchase_total": order.total,
        "location": order.location,
        "payment_status": order.payment_status
    }

@app.post("/payment_msg")
def display_payment_msg(order_id: int):
    payment_msg = get_payment_msg(order_id)

    return {
        "message": payment_msg
        }


