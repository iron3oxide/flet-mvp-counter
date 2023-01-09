import flet as ft

from components import buttons, text_fields
from protocols import PresenterProtocol


class View:
    def __init__(self) -> None:
        self._txt_number = ft.Ref[ft.TextField]()

    def get_component(self, presenter: PresenterProtocol) -> ft.Row:

        plus_button = buttons.add()
        plus_button.on_click = presenter.handle_plus_click

        minus_button = buttons.remove()
        minus_button.on_click = presenter.handle_minus_click

        counter_field = text_fields.counter()
        # counter_field.ref = self._txt_number

        return ft.Row(
            [
                minus_button,
                counter_field,
                plus_button,
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
