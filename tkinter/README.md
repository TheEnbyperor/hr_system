# Creating/changing a model

## 1. Update/create the model class in python
Example; add Hired on field to the user model

This:
```python
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
```
Becomes this:
```python
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
    ### NEW
    # Day hired on
    hired_on = sqlalchemy.Column(sqlalchemy.Date, default=sqlalchemy.func.now())
```

## 2. Generate migrations with alembic
Make sure you're in the correct python environment, `source ./venv/bin/activate` if not.

Run `alembic revision` to generate the migration
```bash
alembic revison --autogenerate -m "Add hired on field"
```

## 3. Run the migration
```bash
alembic upgrade head
```