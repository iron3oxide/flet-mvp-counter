import flet as ft

from mvp_counter.ui import Ui


class Router:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.ui = Ui(self.page)

    def append_view(self, e: ft.RouteChangeEvent) -> None:
        self.page.views.clear()
        match e.route:
            case "/counter":
                self.page.views.append(self.ui.counter_view())

            case _:
                self.page.views.append(self.ui.login_view())

        self.page.update()

    def pop_view(self, e: ft.ViewPopEvent) -> None:
        if len(self.page.views) == 1:
            return
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)
