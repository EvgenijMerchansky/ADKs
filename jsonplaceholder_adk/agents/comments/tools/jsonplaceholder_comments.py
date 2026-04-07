from typing import Any

from jsonplaceholder_adk.shared.clients.jsonplaceholder_client import JsonPlaceholderClient

_client = JsonPlaceholderClient()


def get_comments(limit: int = 5, post_id=None) -> list[dict[str, Any]]:
    """
    Fetch comments from JSONPlaceholder.

    Args:
        limit: Number of comments to return.
        post_id: Post comments to return.
    """
    return _client.get_comments(limit=limit, post_id=post_id)


def get_comment(comment_id: int) -> dict[str, Any] | None:
    """
    Fetch a single comment from JSONPlaceholder by id.

    Args:
        comment_id: Comment identifier.
    """
    return _client.get_comment(comment_id)
