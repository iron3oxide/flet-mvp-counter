import flet as ft

from mvp_counter import ui


class Router:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.login_view = ui.build_login(self.page)
        self.counter_view = ui.build_counter(self.page)

    def append_view(self, e: ft.RouteChangeEvent) -> None:
        match e.route:
            case "/counter":
                if not self.page.auth:
                    return

                self.page.views.append(self.counter_view)

            case _:
                self.page.views.append(self.login_view)

    def pop_view(self, e: ft.ViewPopEvent) -> None:
        if len(self.page.views) == 1:
            return
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)
