import sqlalchemy.orm
from sqlalchemy.ext.declarative import declared_attr, declarative_base

Base = declarative_base()


class TableMixin:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)


class User(TableMixin, Base):
    name = sqlalchemy.Column(sqlalchemy.String)


if __name__ == "__main__":
    # Connect to DB
    db_engine = sqlalchemy.create_engine("sqlite:///data.sqlite3", echo=True)
    Session = sqlalchemy.orm.sessionmaker(bind=db_engine)

    # Setup tables
    Base.metadata.create_all(db_engine)
