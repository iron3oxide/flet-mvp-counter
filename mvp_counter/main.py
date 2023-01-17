import flet as ft
from flet_routed_app import RoutedApp

from mvp_counter import views


def main(page: ft.Page) -> None:
    page.title = "Flet counter example"

    app = RoutedApp(page)
    app.add_view_builders(views.view_builders)

    page.go("/login")


ft.app(target=main, view=ft.WEB_BROWSER, port=34567)
