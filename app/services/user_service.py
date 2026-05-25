from app.models.user import User


def get_user(user_id: int) -> User:
    return User(
        user_id=user_id,
        name="Sree",
        email="sree@example.com"
    )