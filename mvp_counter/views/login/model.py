import flet as ft
from flet.auth.providers.github_oauth_provider import GitHubOAuthProvider
from flet.security import decrypt, encrypt

from mvp_counter.settings import settings


class LoginModel:
    def __init__(self) -> None:
        self.provider = GitHubOAuthProvider(
            client_id=settings.github_client_id,
            client_secret=settings.github_client_secret,
            redirect_url="http://127.0.0.1:34567/api/oauth/redirect",
        )

    def login(self, page: ft.Page) -> None:
        stored_token = self._get_stored_token(page)
        if stored_token:
            page.login(self.provider, saved_token=stored_token)
            return

        page.login(self.provider)

    def store_token(self, page: ft.Page) -> None:
        if not page.auth or not page.auth.token:
            return
        token = page.auth.token.to_json()
        encrypted_token = encrypt(token, settings.app_secret_key)
        page.client_storage.set("auth_token", encrypted_token)

    def _get_stored_token(self, page: ft.Page) -> str | None:
        encrypted_token = page.client_storage.get("auth_token")
        if not encrypted_token:
            return
        token = decrypt(encrypted_token, settings.app_secret_key)
        return token
