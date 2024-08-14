#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')

    @property
    def cities(self):
        all_states = models.storage.all()
        l_cities = []
        l_common = []
        for key in all_states:
            city = key.split('.')
            if city[0] == 'City':
                l_cities.append(all_states[key])
        for el in l_cities:
            if el.state_id == self.id:
                l_common.append(el)
        return l_common
