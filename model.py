import flet as ft


class Model:
    def get_last_number(self, page: ft.Page) -> int:
        if page.client_storage.contains_key("last_number"):
            return page.client_storage.get("last_number")  # type: ignore

        return 0

    def increase_number(self, page: ft.Page, number: int) -> int:
        number += 1
        page.client_storage.set("last_number", number)
        return number

    def decrease_number(self, page: ft.Page, number: int) -> int:
        number -= 1
        page.client_storage.set("last_number", number)
        return number
