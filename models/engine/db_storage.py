#!/usr/bin/python3
""" new class for sqlAlchemy """
from os import getenv

import models
from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """ create the table for env"""
    __engine = None
    __session = None

    def __init__(self):
        self.session = None
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """return dict
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lis = [State, City, User, Place, Review, Amenity]
            for i in lis:
                query = self.__session.query(i)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)

    def new(self, obj):

        """add a new element in the table
        """

        self.__session.add(obj)

    def save(self):
        """save changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete an el
        """
        if obj:
            self.session.delete(obj)

    def get(self, cls, id):
        """A method to retrieve one object
        Return the object based on the class name and its ID, or
        None if not found
        """
        return self.__session.query(cls).filter(cls.id == id).first()

    def count(self, cls=None):
        """A method to count the number of objects in storage
        Return the number of objects in storage matching the given class name
        If no name is passed, returns the count of all objects in storage
        """
        if cls is None:
            return len(self.all())
        return len(self.all(cls))

    def reload(self):
        """config
        """
        Base.metadata.create_all(self.__engine)
        maker = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(maker)
        self.__session = Session()

    def close(self):
        """ calls remove()
        """
        self.__session.close()
