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
    def getInstance(cls):
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