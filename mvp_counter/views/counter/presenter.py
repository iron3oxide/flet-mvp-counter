from flet_mvp_utils import MvpPresenter

from mvp_counter.views.counter.business_logic import CounterDataSource
from mvp_counter.views.counter.protocols import CounterViewProtocol


class CounterPresenter(MvpPresenter):
    def __init__(
        self, *, data_source: CounterDataSource, view: CounterViewProtocol
    ) -> None:
        self.data_source = data_source
        self.view = view

        super().__init__(self.data_source, self.view)

    def build(self) -> None:
        self.view.build(self)
        self.data_source.check_for_stored_number()

    def handle_increment_intent(self) -> None:
        self.data_source.increment_number()

    def handle_decrement_intent(self) -> None:
        self.data_source.decrement_number()
