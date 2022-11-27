#!/usr/bin/python3

from models.base_model import Base, BaseModel
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.session import Session
from sqlalchemy import create_engine
from os import environ


class DBStorage:
    """"""
    __engine = None
    __session = None

    def __init__(self):
        """ """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                        environ.get("HBNB_MYSQL_USER"),
                                        environ.get("HBNB_MYSQL_PWD"),
                                        environ.get("HBNB_MYSQL_HOST"),
                                        environ.get("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if environ.get("HBNB_ENV") == "test":
            Base.metadata.drop(self.__engine)

    def all(self, cls=None):
        """Query in current db all objs deptending of cls name"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        ret_dict = {}
        classes = {
            'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }
        for clss in classes.keys():
            for obj in self.__session.query(classes[clss]).all():
                if '_sa_instance_state' in obj.__dict__:
                    del obj.__dict__['_sa_instance_state']
                ret_dict[str(clss) + '.' + obj.id] = obj
        return ret_dict

    def new(self, obj):
        """ """
        self.__session.add(obj)

    def save(self):
        """ """
        self.__session.commit()

    def delete(self, obj=None):
        """ """
        if obj:
            self.__session.delete(obj)
        else:
            pass

    def reload(self):
        """ """
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(
                            bind=self.__engine, expire_on_commit=False))
