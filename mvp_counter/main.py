import flet as ft

from mvp_counter.router import Router


def main(page: ft.Page) -> None:
    page.title = "Flet counter example"

    router = Router(page)
    page.on_route_change = router.append_view
    page.on_view_pop = router.pop_view

    page.go("/login")


ft.app(target=main, view=ft.WEB_BROWSER, port=34567)
