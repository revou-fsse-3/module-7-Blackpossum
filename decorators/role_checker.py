from flask_login import current_user
from functools import wraps 


def role_required(role_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user.is_authenticated and current_user.role == role_name:
                # continue the request if function run smooth 
                return func(*args ,**kwargs)
            else:
                return {"message": "need permmission to accessing prodyct data"}
        return wrapper
    return decorator
