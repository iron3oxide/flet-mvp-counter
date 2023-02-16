from typing import Protocol

from fletched.mvp import MvpViewProtocol
from pydantic import BaseModel


class LoginPresenterProtocol(Protocol):
    def handle_login_intent(self, remember_me: bool) -> None:
        ...


class LoginViewProtocol(MvpViewProtocol):
    def build(self, presenter: LoginPresenterProtocol) -> None:
        ...

    def render(self, model: BaseModel) -> None:
        ...
