import os
from sqlalchemy.ext.declarative import declarative_base

from metric.src import ROOTPATH
from metric.src.path import auto


Model = declarative_base()


class Schemas:
    path_model = os.path.join(ROOTPATH, 'dbs', 'models')

    def __init__(self):
        self.model = lambda: None
        self.__gathering()

    def __gathering(self):
        for k, v in auto('db', 'model', 'db/model').items():
            setattr(self.model, v.__name__, v)
