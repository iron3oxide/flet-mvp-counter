from typing import Protocol

import flet as ft


class PresenterProtocol(Protocol):
    def handle_plus_click(self, e) -> None:
        ...

    def handle_minus_click(self, e) -> None:
        ...


class ViewProtocol(Protocol):
    def get_ui(self, presenter: PresenterProtocol) -> ft.Row:
        ...

    def get_current_number(self) -> int:
        ...

    def set_current_number(self, number: str) -> None:
        ...
