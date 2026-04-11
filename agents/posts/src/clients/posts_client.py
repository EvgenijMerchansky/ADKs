import requests


class PostsClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get_posts(self, limit: int = 10, user_id=None) -> list[dict]:
        if user_id is not None:
            url = f"{self.BASE_URL}/posts?userId={user_id}&_limit={limit}"
        else:
            url = f"{self.BASE_URL}/posts?_limit={limit}"

        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.json()

    def get_post(self, post_id: int) -> dict | None:
        response = requests.get(f"{self.BASE_URL}/posts/{post_id}", timeout=15)
        if response.status_code == 404:
            return None

        response.raise_for_status()
        return response.json()
