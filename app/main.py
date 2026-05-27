
from app.api.order_routes import get_order_delivery_info
from app.api.order_routes import display_payment_msg

def main():
    delivery_info = get_order_delivery_info(1)
    print(delivery_info)

    payment_msg = display_payment_msg(1)
    print(payment_msg)


if __name__ == "__main__":
    main()