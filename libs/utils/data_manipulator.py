import importlib.util

class DataManipulator:
    def __init__(self):
        self.plugin_module = None
        self.manipulate_data_function = None

    def load_plugin(self, module_path):
        try:
            spec = importlib.util.spec_from_file_location("plugin", module_path)
            self.plugin_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(self.plugin_module)
            self.manipulate_data_function = getattr(self.plugin_module, "manipulate_data")
            print(f"Plugin '{module_path}' loaded successfully.")
            return True
        except Exception as e:
            print(f"Error loading plugin: {e}")
            return False

    def manipulate_data(self, data):
        try:
            if self.plugin_module is not None and self.manipulate_data_function is not None:
                manipulated_data = self.manipulate_data_function(data)
                if manipulated_data is not None:
                    print("Data manipulated successfully.")
                    return manipulated_data
            else:
                print("Plugin not loaded or manipulation function not found.")
        except Exception as e:
            print(f"Error during data manipulation: {e}")
        return None

# # Example usage:
# manipulator = DataManipulator()
# manipulator.load_plugin("your_plugin_file.py")
# result = manipulator.manipulate_data(your_data)
# if result is not None:
#     print("Manipulated data:")
#     print(result)
