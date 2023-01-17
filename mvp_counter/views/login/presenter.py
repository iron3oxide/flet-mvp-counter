import flet as ft
from flet_routed_app import RoutedApp

from mvp_counter.views.login.model import LoginModel
from mvp_counter.views.login.protocols import LoginViewProtocol


class LoginPresenter:
    def __init__(
        self, *, model: LoginModel, view: LoginViewProtocol, app: RoutedApp
    ) -> None:
        self.model = model
        self.view = view
        self.app = app
        self.page = self.app.page

        self.page.on_login = self.handle_login

        self.app.state["demo"] = "State sharing works!"

    def build(self) -> None:
        self.view.build(self)

    def access_from_app_demo(self) -> None:
        print("Accessing presenter of built view works!")

    def handle_login_attempt(self, e: ft.ControlEvent) -> None:
        self.model.login(self.page)

    def handle_login(self, e: ft.LoginEvent) -> None:
        if e.error:
            return
        if self.view.remember_me:
            self.model.store_token(self.page)
        self.page.go("/counter")
