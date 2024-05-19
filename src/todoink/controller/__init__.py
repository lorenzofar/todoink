from __future__ import annotations

import logging
import os

import yaml
from todoist_api_python.api import TodoistAPI

from todoink import SingletonMeta
from todoink.controller.app import AppController

LOGGER = logging.getLogger()


class AppConfig(metaclass=SingletonMeta):
    """
    A class representing the configuration loaded from a .yaml file
    """

    def __init__(self, config_file: str):
        LOGGER.info("Loading config from %s", config_file)
        # Load config from a yaml file
        with open(config_file) as f:
            config = yaml.safe_load(f)
            if config is not None:
                for key, value in config.items():
                    setattr(self, key.upper(), value)


class ControllerFactory:
    """
    Factory class for creating controllers
    """

    def __init__(self, app_config: AppConfig):
        self.__app_config = app_config

    def todoist_ctrl(self) -> TodoistAPI:
        return TodoistAPI(
            self.__app_config.TODOIST["test_token"]
        )

    def app_controller(self, app_state) -> AppController:
        return AppController(
            app_state,
            self.__app_config.REFRESH_RATE,
            self.todoist_ctrl()
        )
