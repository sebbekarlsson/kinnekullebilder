import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


Base = declarative_base()
engine = sa.create_engine('sqlite:///database.sqlite', connect_args={'check_same_thread':False})

def new_session():
    
    Session = sessionmaker()
    Session.configure(bind=engine)

    return Session()

sess = new_session()


# --- * MODELS * --- #

class Data():
    created = sa.Column(sa.TIMESTAMP, server_default=sa.func.now(), onupdate=sa.func.current_timestamp())


class User(Base, Data):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.String(128))
    first_name = sa.Column(sa.String(128))
    last_name = sa.Column(sa.String(128))
    password = sa.Column(sa.String(128))


def initialize_database():
    Base.metadata.create_all(engine)