import flet as ft

from protocols import PresenterProtocol


class View:
    def __init__(self) -> None:
        self._txt_number = ft.TextField(
            value="0", text_align=ft.TextAlign.RIGHT, width=100
        )

    def get_ui(self, presenter: PresenterProtocol) -> ft.Row:
        return ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=presenter.handle_minus_click),
                self._txt_number,
                ft.IconButton(ft.icons.ADD, on_click=presenter.handle_plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

    def get_current_number(self) -> int:
        return int(self._txt_number.value)  # type: ignore

    def set_current_number(self, number: str) -> None:
        self._txt_number.value = number
