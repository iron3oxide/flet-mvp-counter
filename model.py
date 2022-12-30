import flet as ft


class Model:
    def __init__(self, page: ft.Page):
        self.page = page

    def get_last_number(self) -> int:
        if self.page.client_storage.contains_key("last_number"):
            return self.page.client_storage.get("last_number")  # type: ignore

        return 0

    def increase_number(self, number: int) -> int:
        number += 1
        self.page.client_storage.set("last_number", number)
        return number

    def decrease_number(self, number: int):
        number -= 1
        self.page.client_storage.set("last_number", number)
        return number
