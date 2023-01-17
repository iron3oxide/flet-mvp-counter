import flet as ft
from flet_routed_app import RoutedApp

from mvp_counter.views.counter.model import CounterModel
from mvp_counter.views.counter.protocols import CounterViewProtocol


class CounterPresenter:
    def __init__(
        self, *, model: CounterModel, view: CounterViewProtocol, app: RoutedApp
    ) -> None:
        self.model = model
        self.view = view
        self.app = app
        self.page = self.app.page

        self.app.route_to_viewbuilder["/login"].presenter.access_from_app_demo()  # type: ignore
        print(self.app.state["demo"])

    def build(self) -> None:
        self.view.build(self)
        initial_number = self.model.get_last_number(self.page)
        self.view.current_number = initial_number

    def handle_plus_click(self, e: ft.ControlEvent) -> None:
        old_number = self.view.current_number
        new_number = self.model.increase_number(self.page, old_number)
        self.view.current_number = new_number

    def handle_minus_click(self, e: ft.ControlEvent) -> None:
        old_number = self.view.current_number
        new_number = self.model.decrease_number(self.page, old_number)
        self.view.current_number = new_number
