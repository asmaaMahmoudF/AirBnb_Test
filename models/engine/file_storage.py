import json #import json library to work with json api
class FileStorage:
    """FileStorage class"""
    
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects ={}
    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        class_name = obj.__class__.__name__  # Get the class name of the object
        obj_id = obj.id  # Get the ID of the object
        key = f"{class_name}.{obj_id}"  # Create a key using class name and ID
        self.__objects[key] = obj  # Add the object to the dictionary with the key

    def save(self):
        with open(self.__file_path, "w") as f:
            obj_dict = {}
            for key, value in self.__objects.items():
                obj_dict[key] = value.to_dict()
            json.dump(obj_dict, f)
        
if __name__ == "__main__":
    # print(FileStorage.__doc__)
    # print(FileStorage.new.__dict__)
    print(FileStorage.save.__dict__)
    print(FileStorage.all.__dict__)
    print(FileStorage.__objects)
print(FileStorage.__file_path)