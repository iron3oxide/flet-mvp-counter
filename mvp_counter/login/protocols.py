from typing import Protocol

import flet as ft


class LoginPresenterProtocol(Protocol):
    def build(self) -> None:
        ...

    def handle_login_attempt(self, e: ft.ControlEvent) -> None:
        ...


class LoginViewProtocol(Protocol):
    def build(self, presenter: LoginPresenterProtocol) -> None:
        ...

    @property
    def remember_me(self) -> bool:
        ...
