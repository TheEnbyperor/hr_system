import datetime
import sqlalchemy.orm
from sqlalchemy.ext.declarative import declared_attr, declarative_base

# GEt SQLAlchemy base to inherit from
Base = declarative_base()


class TableMixin:
    """
    Base table mixin that all all other tables will use.
    Generates table name and provides ID column.
    """

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    updated_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)


class User(TableMixin, Base):
    """
    Table for storing users
    """

    # Name of the user
    name = sqlalchemy.Column(sqlalchemy.String)
    # Email address
    email = sqlalchemy.Column(sqlalchemy.String)
    # Nation insurance number
    ni = sqlalchemy.Column(sqlalchemy.String)
    # Day hired on
    hired_on = sqlalchemy.Column(sqlalchemy.Date, default=sqlalchemy.func.now())


if __name__ == "__main__":
    # Connect to DB
    db_engine = sqlalchemy.create_engine("sqlite:///data.sqlite3", echo=True)
    Session = sqlalchemy.orm.sessionmaker(bind=db_engine)
