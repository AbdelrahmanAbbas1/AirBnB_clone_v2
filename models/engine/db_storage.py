#!/usr/bin/python3
"""This module defines a database storage engine"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """This class represents the dbstorage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Instintiates an instance of the class"""
        username = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database_name = getenv("HBNB_MYSQL_DB")
        database_url = "mysql+mysqldb://{}:{}@{}/{}".format(
                        username, password, host, database_name)
        self.__engine = create_engine(database_url, pool_pre_ping=True)

        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return all objects of the specified class"""
        all_dict = {}
        all_obj = []
        if cls is not None:
            if issubclass(cls, Base):
                all_obj = self.__session.query(cls).all()
        else:
            for subclass in Base.__subclasses__():
                all_obj.extend(self.__session.query(subclass).all())
        for obj in all_obj:
            key = f'{obj.__class__.__name__}.{obj.id}'
            all_dict[key] = obj
        return all_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)
        self.__session.commit()

    def save(self):
        """Save all the changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes the object from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
