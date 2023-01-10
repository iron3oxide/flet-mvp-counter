import flet as ft

from mvp_counter.blocks import buttons, text_fields
from mvp_counter.counter.protocols import CounterPresenterProtocol


class CounterView(ft.View):
    def __init__(self) -> None:
        super().__init__(
            route="/counter",
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            appbar=ft.AppBar(),
        )

        self._txt_number = ft.Ref[ft.TextField]()

    def build(self, presenter: CounterPresenterProtocol) -> None:
        ui = self._get_ui(presenter)
        self.controls.append(ui)

    def _get_ui(self, presenter: CounterPresenterProtocol) -> ft.Row:
        return ft.Row(
            [
                buttons.remove(presenter.handle_minus_click),
                text_fields.counter(self._txt_number),
                buttons.add(presenter.handle_plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

    @property
    def current_number(self) -> int:
        return int(self._txt_number.current.value)  # type: ignore

    @current_number.setter
    def current_number(self, number: int) -> None:
        self._txt_number.current.value = str(number)
        if self._txt_number.current.page:
            self._txt_number.current.update()
