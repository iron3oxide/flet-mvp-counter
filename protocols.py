from typing import Protocol

import flet as ft


class PresenterProtocol(Protocol):
    def handle_plus_click(self, e) -> None:
        ...

    def handle_minus_click(self, e) -> None:
        ...


class ViewProtocol(Protocol):
    def get_component(self, presenter: PresenterProtocol) -> ft.Row:
        ...

    @property
    def current_number(self) -> int:
        ...

    @current_number.setter
    def current_number(self, number: int) -> None:
        ...
