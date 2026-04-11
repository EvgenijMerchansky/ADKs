from typing import Any, Union, Dict, Any

from users.src.clients.users_client import UsersClient

_client = UsersClient()


def get_users(limit: int = 10) -> list[dict[str, Any]]:
    """
    Fetch users.

    Args:
        limit: Number of users to return.
    """
    return _client.get_users(limit=limit)


def get_user(user_id: int) -> dict[str, Any] | None:
    """
    Fetch a single user by user_id.

    Args:
        user_id: User identifier.
    """
    return _client.get_user(user_id)
