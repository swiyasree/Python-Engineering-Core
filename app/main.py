from app.api.routes import get_user_route


def main():
    response = get_user_route(1)
    print(response)


if __name__ == "__main__":
    main()