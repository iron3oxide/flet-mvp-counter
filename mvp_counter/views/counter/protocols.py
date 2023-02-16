from typing import Protocol

from fletched.mvp import MvpViewProtocol
from pydantic import BaseModel


class CounterPresenterProtocol(Protocol):
    def handle_increment_intent(self) -> None:
        ...

    def handle_decrement_intent(self) -> None:
        ...


class CounterViewProtocol(MvpViewProtocol):
    def render(self, model: BaseModel) -> None:
        ...

    def build(self, presenter: CounterPresenterProtocol) -> None:
        ...
