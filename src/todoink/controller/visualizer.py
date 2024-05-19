"""
A module containing classes used to visualize the app's data on different platforms
"""
from abc import ABC, abstractmethod

from todoink import Observer
from todoink.model.app import AppState


class VisualizerDisplay(Observer[AppState]):
    """
    An interface describing an object that can visualize data on a display
    """

    # Information about the current page and the total number of pages needed to display all the data
    _current_page: int = 0
    _total_pages: int = 0

    def update(self, app_state):
        # Update the total number of pages needed to display all the tasks
        self._total_pages = self._compute_total_pages(len(app_state.tasks))
        # Every time there is an update, re-render the display
        self.render(app_state)

    @abstractmethod
    def start(self):
        """
        Entry point for the display. This method should be called to start the display
        """

    @abstractmethod
    def _compute_total_pages(self, tasks_count: int) -> int:
        """
        Determine the total number of pages needed to display all the tasks in the current display
        """

    @property
    @abstractmethod
    def pagination_supported(self) -> bool:
        """
        Determine if the current display supports pagination
        """

    @abstractmethod
    def render(self, app_state: AppState):
        """
        Render the app state on the display
        """
        pass


class EInkSimulatorDisplay(VisualizerDisplay):
    """
    A class representing a simulator for an e-ink display
    """

    def start(self):
        print("Starting E-Ink Simulator...")

    def _compute_total_pages(self, tasks_count: int) -> int:
        # For the purpose of this simulation, we assume that each page can display 5 tasks
        return tasks_count // 5 + (1 if tasks_count % 5 > 0 else 0)

    @property
    def pagination_supported(self) -> bool:
        return True

    def render(self, app_state: AppState):
        # Display the current page number and the total number of pages
        print(f"Page {self._current_page + 1}/{self._total_pages}")

        # Display the tasks on the current page
        tasks = app_state.tasks[self._current_page * 5:(self._current_page + 1) * 5]
        for task in tasks:
            print(f"- {task.content}")
