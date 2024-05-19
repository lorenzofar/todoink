"""
A module containing classes used to represent and store the app's state
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List

from todoist_api_python.api import TodoistAPI
from todoist_api_python.models import Task

from todoink import Observable


class InteractionMode(Enum):
    """
    An enum representing the different interaction modes of the app
    """
    NORMAL = 0
    EDITING = 1


@dataclass
class AppState(Observable):
    """
    A class representing the state of the app.
    It holds information about the current interaction mode and the current tasks list
    """
    # Interaction mode of the app, default is NORMAL
    interaction_mode: InteractionMode = InteractionMode.NORMAL
    __tasks: List[Task] = field(default_factory=list)

    def __init__(self):
        super().__init__()

    # Getter and setter for the tasks list
    @property
    def tasks(self) -> List[Task]:
        return self.__tasks

    @tasks.setter
    def tasks(self, tasks: List[Task]):
        self.__tasks = tasks
        self.notify(self)
