from typing import Protocol

import flet as ft


class LoginPresenterProtocol(Protocol):
    def build(self):
        ...

    def handle_login_attempt(self, e):
        ...


class LoginViewProtocol(Protocol):
    def build(self, presenter: LoginPresenterProtocol) -> None:
        ...

    def _get_ui(self, presenter: LoginPresenterProtocol) -> ft.Card:
        ...

    @property
    def remember_me(self) -> bool:
        ...
