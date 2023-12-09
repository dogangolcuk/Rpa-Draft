import pandas as pd

def manipulate_data(data):
    if data is not None and not data.empty:
        manipulated_data = data.copy()
        manipulated_data["ENGLISH"] = manipulated_data["TURKISH"] + "_manipulated" +" plugin"
        return manipulated_data
    return None
