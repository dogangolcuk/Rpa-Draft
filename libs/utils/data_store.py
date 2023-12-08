class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class DataStore(metaclass=Singleton):
    def __init__(self):
        self.data_storage = {}

    def write_data(self, data_id, data):
        self.data_storage[data_id] = data
        print(f"Data with ID '{data_id}' stored successfully.")

    def read_data(self, data_id):
        if data_id in self.data_storage:
            data = self.data_storage[data_id]
            print(f"Retrieved data for ID '{data_id}': {data}")
            return data
        else:
            print(f"No data found for ID '{data_id}'.")
            return None