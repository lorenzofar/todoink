import logging
import os

from todoink.controller.visualizer import EInkSimulatorDisplay
from todoink.model.app import AppState
from todoink.controller import ControllerFactory, AppConfig

basedir = os.path.abspath(os.path.dirname(__file__))
DEFAULT_CONFIG_FILE = os.path.join(basedir, "config.yaml")

logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":
    app_config = AppConfig(config_file = os.environ.get("TODOINK_CONFIG", DEFAULT_CONFIG_FILE))

    # Create an instance of the app state
    app_state = AppState()
    controller_factory = ControllerFactory(app_config)
    # Create an instance of the app controller
    controller = controller_factory.app_controller(app_state)
    # Then initialize the display
    display = EInkSimulatorDisplay()
    # And register it as an observer of the app state
    app_state.register(display)

    # Start the controller
    controller.start()
    # Start the display
    display.start()
