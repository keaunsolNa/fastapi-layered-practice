from abc import ABC, abstractmethod


# ABC = ABstract class
# abstractmethod는 추상 매서드 (인터페이스)
# Java에서는 interface AnonymousBoardService { } 형태로 표현
# Rust 관점에서는 trait AnonymousBoardService라고 보면 된다.
class AnonymousBoardService(ABC):

    @abstractmethod
    def create(self, title: str, content: str):
        pass

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_id(self, board_id: str):
        pass