import logging
import time
from threading import Thread, Event

from todoink.model.app import AppState

LOGGER = logging.getLogger()


class AppController(Thread):

    def __init__(self, app_state: AppState, refresh_rate: int, todoist_ctrl):
        """
        Creates a new instance of the controller, updating the provided app state at the specified refresh
        rate
        Args:
            app_state: the object representing the app's state
            refresh_rate: the rate at which the app state should be updated, in seconds
        """
        super().__init__()
        self.__app_state = app_state
        self.__refresh_rate = refresh_rate
        self.__todoist_controller = todoist_ctrl
        self.__stop_event = Event()
        LOGGER.info("Initialized app controller with refresh rate of %d seconds", refresh_rate)

    def run(self):
        while not self.__stop_event.is_set():
            LOGGER.info("Updating tasks...")

            # Here query the Todoist API for tasks that are either planned for today or overdue
            tasks = self.__todoist_controller.get_tasks(filter="due: today | overdue")
            LOGGER.debug("Retrieved %d tasks", len(tasks))
            self.__app_state.tasks = tasks
            time.sleep(self.__refresh_rate)

    def stop(self):
        self.__stop_event.set()
        self.join()
