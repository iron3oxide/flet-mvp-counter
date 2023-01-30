from flet.auth.providers.github_oauth_provider import GitHubOAuthProvider
from flet.security import decrypt, encrypt
from flet_mvp_utils import MvpDataSource, MvpModel

from mvp_counter.app import App
from mvp_counter.settings import settings


class LoginModel(MvpModel):
    remember_me: bool = False


class LoginDataSource(MvpDataSource):
    def __init__(self, app: App, route_parameters: dict) -> None:
        super().__init__(LoginModel)

        self.app = app
        self.page = app.page
        self.route_parameters = route_parameters
        self.provider = GitHubOAuthProvider(
            client_id=settings.github_client_id,
            client_secret=settings.github_client_secret,
            redirect_url="http://127.0.0.1:34567/api/oauth/redirect",
        )

    def login(self, remember_me: bool) -> None:
        self.update_model_complete({"remember_me": remember_me})

        stored_token = self._get_stored_token()
        if stored_token:
            self.page.login(self.provider, saved_token=stored_token)

        self.page.login(self.provider)
        if not self.page.auth:
            return

        if remember_me and not stored_token:
            self._store_token()

        self.page.go("/counter")

    def _store_token(self) -> None:
        if not self.page.auth or not self.page.auth.token:
            return
        token = self.page.auth.token.to_json()
        encrypted_token = encrypt(token, settings.app_secret_key)
        self.page.client_storage.set("auth_token", encrypted_token)

    def _get_stored_token(self) -> str | None:
        encrypted_token = self.page.client_storage.get("auth_token")
        if not encrypted_token:
            return
        token = decrypt(encrypted_token, settings.app_secret_key)
        return token
