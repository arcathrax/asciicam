from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Label, Button
from textual.containers import VerticalScroll
import pyperclip

from camera import Camera


class AsciiCamApp(App):
    camera = Camera()

    BINDINGS = [
        ("q", "quit", "Quit application"),
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
        self.set_interval(1 / 30, self.update_frame)
        self.title = "ASCIICAM"
        self.sub_title = "A camera feed in your terminal."

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield Header()
        yield Footer()
        yield VerticalScroll(
            self.items["previewlabel"],
            Button("Copy ASCII", id="copybtn"),
        )

    async def update_frame(self) -> None:
        """Periodically called to update camera frames."""
        ascii_frame = self.camera.get_ascii_camera()
        self.items["previewlabel"].update(ascii_frame)

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "copybtn":
            ascii_frame = self.camera.get_ascii_camera()
            pyperclip.copy(str(ascii_frame))
            self.sub_title = "Copied to clipboard!"


if __name__ == "__main__":
    app = AsciiCamApp()
    app.run()

