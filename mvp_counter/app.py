from fletched.routed_app import CustomAppState, RoutedApp


class AppState(CustomAppState):
    test: int = 0
    demo: str = ""


class App(RoutedApp):
    state: AppState = AppState()
