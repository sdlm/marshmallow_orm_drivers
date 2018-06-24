import abc


class MyQuerySet(abc.ABC):

    # noinspection PyUnresolvedReferences
    def __init__(self, model):
        self.model = model

    @abc.abstractmethod
    def get(self, **kwargs):
        pass

    @abc.abstractmethod
    def exists(self, **kwargs):
        pass

    @abc.abstractmethod
    def count(self, **kwargs):
        pass

    @abc.abstractmethod
    def create(self, **kwargs):
        pass
