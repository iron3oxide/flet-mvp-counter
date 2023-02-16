import flet as ft
from fletched.mvp import MvpView, ViewConfig

from mvp_counter.controls import buttons
from mvp_counter.views.login.protocols import LoginPresenterProtocol


class LoginView(MvpView):
    ref_map = {"remember_me": ft.Ref[ft.Checkbox]()}
    config = ViewConfig(
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    def build(self, presenter: LoginPresenterProtocol) -> None:
        self.presenter = presenter
        ui = self._get_ui()
        self.controls.append(ui)

    def _get_ui(self) -> ft.Card:
        return ft.Card(
            content=ft.Column(
                controls=[
                    buttons.login(callback=self.login_intent),
                    ft.Row(
                        controls=[
                            ft.Checkbox(
                                ref=self.ref_map["remember_me"], label="Remember me"
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            ),
            width=300,
        )

    def login_intent(self, e: ft.ControlEvent) -> None:
        remember_me = bool(self.ref_map["remember_me"].current.value)
        self.presenter.handle_login_intent(remember_me)
