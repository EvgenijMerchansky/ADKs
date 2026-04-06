from typing import Any
from ..clients.jsonplaceholder_client import JsonPlaceholderClient

_client = JsonPlaceholderClient()

def get_posts(limit: int = 10, user_id = None) -> list[dict[str, Any]]:
    """
    Fetch posts from JSONPlaceholder.

    Args:
        limit: Number of posts to return.
        user_id: Users posts to return.
    """
    return _client.get_posts(limit=limit, user_id=user_id)

def get_post(post_id: int) -> dict[str, Any] | None:
    """
    Fetch a single post from JSONPlaceholder by id.

    Args:
        post_id: Post identifier.
    """
    return _client.get_post(post_id)