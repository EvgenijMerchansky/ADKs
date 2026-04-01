from typing import Any
from ..clients.jsonplaceholder_client import JsonPlaceholderClient

_client = JsonPlaceholderClient()

def get_users(limit: int = 10) -> list[dict[str, Any]]:
    """
    Fetch users from JSONPlaceholder.

    Args:
        limit: Number of users to return.
    """
    return _client.get_users(limit=limit)

def get_user(user_id: int) -> dict[str, Any] | None:
    """
    Fetch a single user from JSONPlaceholder by id.

    Args:
        user_id: User identifier.
    """
    return _client.get_user(user_id)