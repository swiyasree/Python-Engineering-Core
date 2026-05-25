from app.services.user_service import get_user


def get_user_route(user_id: int):
    user = get_user(user_id)

    return {
        "id": user.user_id,
        "name": user.name,
        "email": user.email
    }