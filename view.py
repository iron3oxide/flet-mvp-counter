import flet as ft

from components import buttons, text_fields
from protocols import PresenterProtocol


class View:
    def __init__(self) -> None:
        self._txt_number = ft.Ref[ft.TextField]()

    def get_component(self, presenter: PresenterProtocol) -> ft.Row:
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
        self._txt_number.current.update()
