import flet as ft

from mvp_counter.blocks import buttons
from mvp_counter.login.protocols import LoginPresenterProtocol


class LoginView(ft.View):
    def __init__(self):
        super().__init__(
            route="/login",
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        self._remember_me = ft.Ref[ft.Checkbox]()

    def build(self, presenter: LoginPresenterProtocol):
        ui = self._get_ui(presenter)
        self.controls.append(ui)

    def _get_ui(self, presenter: LoginPresenterProtocol) -> ft.Card:
        return ft.Card(
            content=ft.Column(
                controls=[
                    buttons.login(callback=presenter.handle_login_attempt),
                    ft.Row(
                        controls=[
                            ft.Checkbox(ref=self._remember_me, label="Remember me")
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            ),
            width=300,
        )

    @property
    def remember_me(self) -> bool:
        return bool(self._remember_me.current.value)
