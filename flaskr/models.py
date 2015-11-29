import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


Base = declarative_base()
engine = sa.create_engine('sqlite:///database.sqlite',
        connect_args={'check_same_thread':False})

def new_session():
    
    Session = sessionmaker()
    Session.configure(bind=engine)

    return Session()

sess = new_session()


# --- * MODELS * --- #

class Data():
    created = sa.Column(sa.TIMESTAMP, server_default=sa.func.now(),
            onupdate=sa.func.current_timestamp())


class User(Base, Data):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.String(128), unique=True)
    first_name = sa.Column(sa.String(128))
    last_name = sa.Column(sa.String(128))
    password = sa.Column(sa.String(128))
    image_id = sa.Column(sa.Integer, sa.ForeignKey('images.id'))
    notifications = relationship(
            'Notification',
            backref='notifications',
            foreign_keys='Notification.user_id'
    )
   

class Place(Base, Data):
    __tablename__ = 'places'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(256), unique=True)


class Image(Base, Data):
    __tablename__ = 'images'
    id = sa.Column(sa.Integer, primary_key=True)
    filename = sa.Column(sa.String(256), unique=True)
    place_id = sa.Column(sa.String(256), sa.ForeignKey('places.id'))
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    title = sa.Column(sa.String(256))
    description = sa.Column(sa.String(1080))


class Comment(Base, Data):
    __tablename__ = 'comments'
    id = sa.Column(sa.Integer, primary_key=True)
    image_id = sa.Column(sa.Integer, sa.ForeignKey('images.id'))
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    text = sa.Column(sa.String(700))


class Notification(Base, Data):
    __tablename__ = 'notifications'
    id = sa.Column(sa.Integer, primary_key=True)
    image_id = sa.Column(sa.Integer, sa.ForeignKey('images.id'))
    user_caused_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    type = sa.Column(sa.String(64))

    caused_by = relationship(
        'User',
        primaryjoin='User.id==Notification.user_caused_id'
      )

def initialize_database():
    Base.metadata.create_all(engine)
