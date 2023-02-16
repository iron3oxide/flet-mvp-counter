from fletched.mvp import MvpDataSource, MvpModel


class CounterModel(MvpModel):
    number: int = 0


class CounterDataSource(MvpDataSource):
    current_model = CounterModel()

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
