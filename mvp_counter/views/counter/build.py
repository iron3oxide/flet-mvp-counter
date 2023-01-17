from flet_routed_app import MvpViewBuilder, login_required, route

from mvp_counter.views.counter.model import CounterModel
from mvp_counter.views.counter.presenter import CounterPresenter
from mvp_counter.views.counter.view import CounterView


@login_required
@route("/counter")
class CounterViewBuilder(MvpViewBuilder):
    model_class = CounterModel
    presenter_class = CounterPresenter
    view_class = CounterView
