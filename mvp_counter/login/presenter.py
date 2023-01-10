import flet as ft

from mvp_counter.login.model import LoginModel
from mvp_counter.login.protocols import LoginViewProtocol


class LoginPresenter:
    def __init__(
        self, model: LoginModel, view: LoginViewProtocol, page: ft.Page
    ) -> None:
        self.model = model
        self.view = view
        self.page = page

        self.page.on_login = self.handle_login

    def build(self):
        self.view.build(self)

    def handle_login_attempt(self, e: ft.Event):
        self.model.login(self.page)

    def handle_login(self, e: ft.LoginEvent):
        if e.error:
            return
        if self.view.remember_me:
            self.model.store_token(self.page)
        self.page.go("/counter")
