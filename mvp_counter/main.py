import flet as ft

from mvp_counter import views
from mvp_counter.app import App


def main(page: ft.Page) -> None:
    page.title = "Flet counter example"

    app = App(page, custom_state=True)
    app.add_view_builders(views.view_builders)

    page.go("/login")


ft.app(target=main, view=ft.WEB_BROWSER, port=34567)
