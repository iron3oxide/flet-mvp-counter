import flet as ft
from flet_mvp_utils import MvpView

from mvp_counter.controls import buttons, text_fields
from mvp_counter.views.counter.protocols import CounterPresenterProtocol


class CounterView(MvpView):
    def __init__(self, route: str) -> None:
        self.ref_map = {"number": ft.Ref[ft.TextField]()}
        super().__init__(
            ref_map=self.ref_map,
            route=route,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            appbar=ft.AppBar(),
        )

    def build(self, presenter: CounterPresenterProtocol) -> None:
        self.presenter = presenter
        ui = self._get_ui()
        self.controls.append(ui)

    def _get_ui(self) -> ft.Row:
        return ft.Row(
            [
                buttons.remove(self.decrement_intent),
                text_fields.counter(self.ref_map["number"]),
                buttons.add(self.increment_intent),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

    def increment_intent(self, e: ft.ControlEvent) -> None:
        self.presenter.handle_increment_intent()

    def decrement_intent(self, e: ft.ControlEvent) -> None:
        self.presenter.handle_decrement_intent()
