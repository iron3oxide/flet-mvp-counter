import flet as ft

from mvp_counter.counter import CounterModel, CounterPresenter, CounterView
from mvp_counter.login import LoginModel, LoginPresenter, LoginView


def build_login(page: ft.Page) -> LoginView:
    model = LoginModel()
    view = LoginView()
    presenter = LoginPresenter(model, view, page)
    presenter.build()

    return view


def build_counter(page: ft.Page) -> CounterView:
    model = CounterModel()
    view = CounterView()
    presenter = CounterPresenter(model, view, page)
    presenter.build()

    return view
