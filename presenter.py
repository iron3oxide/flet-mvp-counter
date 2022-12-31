import flet as ft

from model import Model
from protocols import ViewProtocol


class Presenter:
    def __init__(self, model: Model, view: ViewProtocol, page: ft.Page) -> None:
        self.model = model
        self.view = view
        self.page = page

    def build(self) -> ft.Row:
        initial_number = self.model.get_last_number(self.page)
        self.view.set_current_number(str(initial_number))
        self.page.update()
        return self.view.get_ui(self)

    def handle_plus_click(self, e) -> None:
        old_number = self.view.get_current_number()
        new_number = self.model.increase_number(self.page, old_number)
        self.view.set_current_number(str(new_number))
        self.page.update()

    def handle_minus_click(self, e) -> None:
        old_number = self.view.get_current_number()
        new_number = self.model.decrease_number(self.page, old_number)
        self.view.set_current_number(str(new_number))
        self.page.update()
