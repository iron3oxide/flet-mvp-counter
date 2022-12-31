import flet as ft

from model import Model
from presenter import Presenter
from view import View


def main(page: ft.Page) -> None:
    model = Model()
    view = View()
    presenter = Presenter(model, view, page)
    ui = presenter.build()

    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(ui)


ft.app(target=main, view=ft.WEB_BROWSER, port=34567)
