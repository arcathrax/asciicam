from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Label
from textual.containers import VerticalScroll

from camera import Camera

class AsciiCamApp(App):
    camera = Camera()

    BINDINGS = [
        ("q", "quit", "Quit application")
    ]
    CSS_PATH = "asciicamera.tcss"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Registry of widgets you can reference by string
        self.items: dict[str, Label] = {
            "previewlabel": Label("", id="previewlabel"),
        }

    async def on_mount(self) -> None:
        """Called when the app starts. Sets up periodic updates."""
        self.set_interval(1/30, self.update_frame)
        self.title = "asciicam"
        self.sub_title = "live camera in your terminal"

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield Header()
        yield Footer()
        yield VerticalScroll(
            self.items["previewlabel"]
        )

    async def update_frame(self) -> None:
        """Periodically called to update camera frames."""
        ascii = self.camera.get_ascii_camera()
        self.items["previewlabel"].update(ascii)

if __name__ == "__main__":
    app = AsciiCamApp()
    app.run()
