import pandas as pd
from data_store import DataStore
from libs.logging_utils import log_message

def excel_to_pandas(cmd):
    try:
        with pd.ExcelFile(cmd["filePath"]) as xls:
            df = pd.read_excel(xls)
            # Process the DataFrame or perform any other operations here
            # For example, writing to a data store
            data_store = DataStore()
            data_store.write_data(cmd["writeDataId"], df)
            
        # File automatically closes when the 'with' block is exited
        data = data_store.read_data(cmd["writeDataId"])
        print(data)
        # return df  # You can return the DataFrame if needed
    except Exception as e:
        print(f"Error occurred: {e}")
