from fletched.mvp import MvpViewBuilder
from fletched.routed_app import login_required, route

from mvp_counter.views.counter.business_logic import CounterDataSource
from mvp_counter.views.counter.presenter import CounterPresenter
from mvp_counter.views.counter.view import CounterView


@login_required
@route("/counter")
class CounterViewBuilder(MvpViewBuilder):
    data_source_class = CounterDataSource
    presenter_class = CounterPresenter
    view_class = CounterView
