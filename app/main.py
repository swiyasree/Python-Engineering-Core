from app.api.routes import get_user_route
from app.api.routes import get_order_delivery_info

def main():
    response = get_user_route(1)
    print(response)

    delivery_info = get_order_delivery_info(1)
    print(delivery_info)


if __name__ == "__main__":
    main()