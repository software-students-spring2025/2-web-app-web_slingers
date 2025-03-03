from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from bson.objectid import ObjectId

# Lazy import to prevent circular import issues
def get_mongo():
    from app import mongo
    return mongo

class User(UserMixin):
    def __init__(self, user_id, username, password_hash):
        self.id = str(user_id)  # Flask-Login requires string IDs
        self.username = username
        self.password_hash = password_hash

    def verify_password(self, password):
        """Check if the provided password matches the stored hash."""
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def find_by_username(username):
        """Find a user by username."""
        return get_mongo().db.users.find_one({"username": username})

    @staticmethod
    def find_by_email(email):
        """Find a user by email (Used for password reset)."""
        return get_mongo().db.users.find_one({"email": email})

    @staticmethod
    def find_by_id(user_id):
        """Find a user by ID."""
        return get_mongo().db.users.find_one({"_id": ObjectId(user_id)})

    @staticmethod
    def create_user(username, password, email=None):
        """Create a new user with hashed password."""
        password_hash = generate_password_hash(password)
        user_data = {"username": username, "password_hash": password_hash}
        
        if email:  # Store email if provided
            user_data["email"] = email

        user_id = get_mongo().db.users.insert_one(user_data).inserted_id
        return User(user_id, username, password_hash)

