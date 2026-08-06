from database.database import SessionLocal
from models import User
from schemas import UserCreate, UserLogin
from utils import hash_password,verify_password,create_access_token,verify_access_token

def create_user(user: UserCreate):
    session = SessionLocal()

    try:
        new_user = User(
            username=user.username,
            email=user.email,
            password=hash_password(user.password)
        )

        session.add(new_user)
        session.commit()
        session.refresh(new_user)

        return new_user

    except Exception as e:
        session.rollback()
        raise e

    finally:
        session.close()


def get_user_by_username(username: str):
    session = SessionLocal()

    try:
        user = session.query(User).filter(
            User.username == username
        ).first()

        return user

    finally:
        session.close()


def login_user(user: UserLogin):
    db_user = get_user_by_username(user.username)

    if db_user is None:
        return {
            "success": False,
            "message": "User not found"
        }

    if not verify_password(user.password, db_user.password):
        return {
            "success": False,
            "message": "Invalid password"
        }

    token = create_access_token(
        {
            "sub": db_user.username
        }
    )

    return {
        "success": True,
        "message": "Login successful",
        "access_token": token,
        "token_type": "Bearer"
    }


def get_current_user(token: str):
    try:
        payload = verify_access_token(token)

        username = payload.get("sub")

        if username is None:
            return None

        return get_user_by_username(username)

    except Exception:
        return None