from flet_mvp_utils import MvpDataSource, MvpModel

from mvp_counter.app import App


class CounterModel(MvpModel):
    number: int = 0


class CounterDataSource(MvpDataSource):
    def __init__(self, app: App, route_parameters: dict) -> None:
        self.app = app
        self.page = app.page
        self.route_parameters = route_parameters
        super().__init__(CounterModel)

    def check_for_stored_number(self) -> None:
        if self.page.client_storage.contains_key("last_number"):
            last_number: int = self.page.client_storage.get("last_number")  # type: ignore
            self.update_model_complete({"number": last_number})

    def increment_number(self) -> None:
        number = self.current_model.number + 1
        if self.update_model_complete({"number": number}):
            self.page.client_storage.set("last_number", number)

    def decrement_number(self) -> None:
        number = self.current_model.number - 1
        if self.update_model_complete({"number": number}):
            self.page.client_storage.set("last_number", number)
