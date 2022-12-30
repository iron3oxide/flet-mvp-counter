from typing import Protocol

import flet as ft

from model import Model


class View(Protocol):
    def get_ui(self, presenter) -> ft.Row:
        ...

    def get_current_number(self) -> int:
        ...

    def set_current_number(self, number: str) -> None:
        ...


class Presenter:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view

    def build(self) -> ft.Row:
        initial_number = self.model.get_last_number()
        print(initial_number)
        self.view.set_current_number(str(initial_number))
        self.model.page.update()
        return self.view.get_ui(self)

    def handle_plus_click(self, e) -> None:
        old_number = self.view.get_current_number()
        new_number = self.model.increase_number(old_number)
        self.view.set_current_number(str(new_number))
        self.model.page.update()

    def handle_minus_click(self, e) -> None:
        old_number = self.view.get_current_number()
        new_number = self.model.decrease_number(old_number)
        self.view.set_current_number(str(new_number))
        self.model.page.update()
