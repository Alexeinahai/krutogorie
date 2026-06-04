from fastapi import Request


def get_current_user_optional(request: Request):
    return request.session.get("user")
