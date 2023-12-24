from todoist_api_python.api import TodoistAPI
from flask import current_app

class ControllerFactory:
    """
    Factory class for creating controllers
    """

    @staticmethod
    def todoist_ctrl():
        return TodoistAPI(
            current_app.config["TODOIST"]["test_token"]
        )