import requests

class JsonPlaceholderClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get_users(self, limit: int = 10) -> list[dict]:
        response = requests.get(f"{self.BASE_URL}/users?_limit={limit}", timeout=15)
        response.raise_for_status()
        return response.json()

    def get_user(self, user_id: int) -> dict | None:
        response = requests.get(f"{self.BASE_URL}/users/{user_id}", timeout=15)
        if response.status_code == 404:
            return None

        response.raise_for_status()
        return response.json()

    def get_posts(self, limit: int = 10) -> list[dict]:
        response = requests.get(f"{self.BASE_URL}/posts?_limit={limit}", timeout=15)
        response.raise_for_status()
        return response.json()

    def get_post(self, post_id: int) -> dict | None:
        response = requests.get(f"{self.BASE_URL}/posts/{post_id}", timeout=15)
        if response.status_code == 404:
            return None

        response.raise_for_status()
        return response.json()
