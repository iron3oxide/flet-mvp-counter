from dataclasses import dataclass
from fletched.mvp import MvpPresenter

from mvp_counter.views.login.business_logic import LoginDataSource
from mvp_counter.views.login.protocols import LoginViewProtocol


@dataclass
class LoginPresenter(MvpPresenter):
    data_source: LoginDataSource
    view: LoginViewProtocol

    def handle_login_intent(self, remember_me: bool) -> None:
        self.data_source.login(remember_me)
