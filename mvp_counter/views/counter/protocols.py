from typing import Protocol

import flet as ft


class CounterPresenterProtocol(Protocol):
    def handle_plus_click(self, e: ft.ControlEvent) -> None:
        ...

    def handle_minus_click(self, e: ft.ControlEvent) -> None:
        ...


class CounterViewProtocol(Protocol):
    def build(self, presenter: CounterPresenterProtocol) -> None:
        ...

    @property
    def current_number(self) -> int:
        ...

    @current_number.setter
    def current_number(self, number: int) -> None:
        ...
