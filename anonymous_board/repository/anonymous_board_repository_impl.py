from typing import List

from anonymous_board.entity.anonymous_board import AnonymousBoard
from anonymous_board.service.anonymous_board_service import AnonymousBoardService
from config.mysql_config import SessionLocal


class AnonymousBoardRepositoryImpl(AnonymousBoardService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, title: str, content: str) -> AnonymousBoard:
        db = SessionLocal()

        try:
            board = AnonymousBoard(title=title, content=content)
            db.add(board)
            db.commit()
            db.refresh(board)
            return board

        except:
            db.rollback()
            raise

        finally:
            db.close()

    def find_all(self) -> List[AnonymousBoard]:
        db = SessionLocal()

        try:
            return (db.query(AnonymousBoard).
                    order_by(AnonymousBoard.created_at.desc()).all())
        finally:
            db.close()

    def find_by_id(self, board_id: str) -> AnonymousBoard:
        db = SessionLocal()

        try:
            return (db.query(AnonymousBoard).
                    filter(AnonymousBoard.id == board_id).first())
        finally:
            db.close()