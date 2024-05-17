# 3.BaseModel__Task
#!/usr/bin/env python3
from uuid import uuid4
from datetime import datetime
class BaseModel:
    """BaseModel class"""


    def __init__(self, *args, **kwargs) -> None:
        """init function"""
        self.id  =  str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
    def __str__(self):
        """str function"""
        return f"{self.__class__.__name__} ({self.id}) {self.__dict__}"
    def save(self):
        """save function"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """to_dict function"""
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = model_dict['created_at'].isoformat()
        model_dict['updated_at'] = model_dict['updated_at'].isoformat()
        return model_dict



