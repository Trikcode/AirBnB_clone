#!/usr/bin/python3
import uuid
import datetime
from models import storage
class BaseModel:
    def __init__(self, *args, **kwargs):
        if(bool(kwargs)):
            for key in kwargs.keys():
                if(key != '__class__'):
                    setattr(self, key, kwargs[key])
                    self.created_at = datetime.datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f') 
                    self.updated_at = datetime.datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
    def __str__(self):
        return '[{}] ({}) {}'.format(type(self).__name__, self.id, self.__dict__)    
   
    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()
    def to_dict(self):
        selu = self.__dict__
        selu['__class__'] = type(self).__name__
        selu['updated_at'] = self.updated_at.isoformat();
        selu['created_at'] = self.created_at.isoformat();
        return self.__dict__
