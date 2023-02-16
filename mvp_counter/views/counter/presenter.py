from dataclasses import dataclass

from fletched.mvp import MvpPresenter

from mvp_counter.views.counter.business_logic import CounterDataSource
from mvp_counter.views.counter.protocols import CounterViewProtocol


@dataclass
class CounterPresenter(MvpPresenter):
    data_source: CounterDataSource
    view: CounterViewProtocol

    def build(self) -> None:
        self.view.build(self)
        self.data_source.check_for_stored_number()

    def handle_increment_intent(self) -> None:
        self.data_source.increment_number()

    def handle_decrement_intent(self) -> None:
        self.data_source.decrement_number()
