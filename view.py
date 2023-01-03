import flet as ft

from protocols import PresenterProtocol


class View:
    def __init__(self) -> None:
        self._txt_number = ft.TextField(
            value="0", text_align=ft.TextAlign.RIGHT, width=100
        )

    def get_component(self, presenter: PresenterProtocol) -> ft.Row:
        def remove_button():
            return ft.IconButton(ft.icons.REMOVE, on_click=presenter.handle_minus_click)

        def add_button():
            return ft.IconButton(ft.icons.ADD, on_click=presenter.handle_plus_click)

        return ft.Row(
            [
                remove_button(),
                self._txt_number,
                add_button(),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

    @property
    def current_number(self) -> int:
        return int(self._txt_number.value)  # type: ignore

    @current_number.setter
    def current_number(self, number: int) -> None:
        self._txt_number.value = str(number)
        if self._txt_number.page:
            self._txt_number.update()
