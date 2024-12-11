from abc import ABC, abstractmethod


class Queue(ABC):
    CAPACITY = 5

    @abstractmethod
    def enqueue(self, it):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def isEmpty(self):
        pass

    @abstractmethod
    def isFull(self):
        pass
