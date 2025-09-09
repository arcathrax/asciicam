from textual.app import App, ComposeResult
from textual.widgets import Footer, Header
from textual.containers import VerticalScroll

class AsciiCamApp(App):
    BINDINGS = [
        ("q", "quit", "Quit application")
    ]

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield Header()
        yield Footer()
        yield VerticalScroll(
        )

if __name__ == "__main__":
    app = AsciiCamApp()
    app.run()
