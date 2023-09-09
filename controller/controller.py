from view.loading_view import LoadingView


class ScreenController:
    def __init__(self, app):
        self.app = app  # Receba a instância da aplicação como argumento

    def show_loading_view(self):
        self.loading_view = LoadingView()
        self.loading_view.show()
