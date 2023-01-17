from flet_routed_app import MvpViewBuilder, route

from mvp_counter.views.login.model import LoginModel
from mvp_counter.views.login.presenter import LoginPresenter
from mvp_counter.views.login.view import LoginView


@route("/login")
class LoginViewBuilder(MvpViewBuilder):
    model_class = LoginModel
    presenter_class = LoginPresenter
    view_class = LoginView
