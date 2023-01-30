from flet_mvp_utils import MvpPresenter

from mvp_counter.views.login.business_logic import LoginDataSource
from mvp_counter.views.login.protocols import LoginViewProtocol


class LoginPresenter(MvpPresenter):
    def __init__(
        self, *, data_source: LoginDataSource, view: LoginViewProtocol
    ) -> None:
        self.data_source = data_source
        self.view = view

        super().__init__(self.data_source, self.view)

    def handle_login_intent(self, remember_me: bool) -> None:
        self.data_source.login(remember_me)
