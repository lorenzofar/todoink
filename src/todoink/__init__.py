from __future__ import annotations

import logging
import os
from abc import abstractmethod
from typing import Generic, Set, TypeVar

LOGGER = logging.getLogger()


class Observable:

    def __init__(self):
        self._observers: Set[Observer] = set()

    def register(self, observer: Observer):
        self._observers.add(observer)

    def unregister(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer.update(*args, **kwargs)


T = TypeVar('T', bound=Observable)


class Observer(Generic[T]):
    @abstractmethod
    def update(self, *args, **kwargs):
        raise NotImplementedError


class SingletonMeta(type):
    """
    A metaclass for creating singleton classes
    """

    def __init__(self, name, bases, dict):
        super(SingletonMeta, self).__init__(name, bases, dict)
        self.instance = None

    def __call__(self, *args, **kw):
        if self.instance is None:
            self.instance = super(SingletonMeta, self).__call__(*args, **kw)
        return self.instance
