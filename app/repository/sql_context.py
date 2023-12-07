from app.models import DB


class SqlContext(object):
    def __init__(self):
        self.session = DB.session

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        if self.session:
            try:
                self.session.commit()
            except Exception as ex:
                self.session.rollback()
                raise ex
