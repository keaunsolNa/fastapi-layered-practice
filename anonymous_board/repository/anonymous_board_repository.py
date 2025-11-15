from abc import ABC, abstractmethod

from anonymous_board.entity.anonymous_board import AnonymousBoard

class AnonymousBoardRepository(ABC):

    @abstractmethod
    def create(self, title: str, content: str) -> AnonymousBoard:
        pass