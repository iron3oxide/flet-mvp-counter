from typing import Callable

import flet as ft

from mvp_counter.counter import CounterModel, CounterPresenter, CounterView
from mvp_counter.login import LoginModel, LoginPresenter, LoginView


class Ui:
    def __init__(self, page: ft.Page) -> None:
        self.page = page

    @staticmethod
    def authorize(view_builder: Callable):
        def inner(self):
            if not self.page.auth:
                return self.unauthorized_view()
            return view_builder(self)

        return inner

    def login_view(self) -> LoginView:
        model = LoginModel()
        view = LoginView()
        presenter = LoginPresenter(model, view, self.page)
        presenter.build()

        return view

    @authorize
    def counter_view(self) -> CounterView:
        model = CounterModel()
        view = CounterView()
        presenter = CounterPresenter(model, view, self.page)
        presenter.build()

        return view

    def unauthorized_view(self) -> ft.View:
        return ft.View(
            controls=[
                ft.TextButton(
                    text="You are not authorized to access this. Click this button to return home.",
                    on_click=lambda e: self.page.go("/login"),
                ),
            ],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
