import requests


class CommentsClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get_comments(self, limit: int = 5, post_id=None) -> list[dict]:
        if post_id is not None:
            url = f"{self.BASE_URL}/comments?postId={post_id}&_limit={limit}"
        else:
            url = f"{self.BASE_URL}/comments?_limit={limit}"

        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.json()

    def get_comment(self, comment_id: int) -> dict | None:
        response = requests.get(f"{self.BASE_URL}/comments/{comment_id}", timeout=15)
        if response.status_code == 404:
            return None

        response.raise_for_status()
        return response.json()
