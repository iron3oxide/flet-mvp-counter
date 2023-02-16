from fletched.routed_app import route
from fletched.mvp import MvpViewBuilder

from mvp_counter.views.login.business_logic import LoginDataSource
from mvp_counter.views.login.presenter import LoginPresenter
from mvp_counter.views.login.view import LoginView


@route("/login")
class LoginViewBuilder(MvpViewBuilder):
    data_source_class = LoginDataSource
    presenter_class = LoginPresenter
    view_class = LoginView
