import flet as ft

from model import Model
from protocols import ViewProtocol


class Presenter:
    def __init__(self, model: Model, view: ViewProtocol, page: ft.Page) -> None:
        self.model = model
        self.view = view
        self.page = page

    def build(self):
        component = self.view.get_component(self)
        self.page.add(component)
        initial_number = self.model.get_last_number(self.page)
        self.view.current_number = initial_number

    def handle_plus_click(self, e) -> None:
        old_number = self.view.current_number
        new_number = self.model.increase_number(self.page, old_number)
        self.view.current_number = new_number

    def handle_minus_click(self, e) -> None:
        old_number = self.view.current_number
        new_number = self.model.decrease_number(self.page, old_number)
        self.view.current_number = new_number
