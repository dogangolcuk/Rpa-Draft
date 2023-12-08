import pandas as pd
from openpyxl import load_workbook
from common_imports import pandas as pd, os
from data_store import DataStore
from libs.logging_utils import log_message
from openpyxl.utils import get_column_letter


def read_data_from_store(data_id):
    data_store = DataStore()
    return data_store.read_data(data_id)


def manipulate_data(data):
    if data is not None and not data.empty:
        manipulated_data = data.copy()
        manipulated_data["ENGLISH"] = manipulated_data["TURKISH"]
        return manipulated_data
    return None


def change_file_permissions(file_path):
    try:
        os.chmod(file_path, 0o666)
        print(f"Permissions changed for {file_path}")
    except OSError as e:
        print(f"Error changing permissions: {e}")


def write_to_excel_new_sheet(manipulated_data, excel_file, sheet_name='Manipulated_Data'):
    try:
        # Create a new Pandas DataFrame from manipulated_data
        df = pd.DataFrame(manipulated_data)

        with pd.ExcelWriter(excel_file, engine='openpyxl', mode='a') as writer:
            writer.book = load_workbook(excel_file)

            # Check if the specified sheet exists, if not, create a new one
            if sheet_name not in writer.book.sheetnames:
                writer.book.create_sheet(title=sheet_name)

            # Write the data to the specified sheet
            writer.sheets = {ws.title: ws for ws in writer.book.worksheets}
            sheet = writer.book[sheet_name]

            for idx, row in df.iterrows():
                for col_idx, value in enumerate(row):
                    sheet[get_column_letter(
                        col_idx + 1) + str(idx + 1)] = value

            writer.save()

            print(f"Manipulated data saved to a new sheet '{
                  sheet_name}' in {excel_file}")
    except Exception as e:
        print(f"Error occurred while writing to Excel: {e}")


def manipulate_and_write_data(cmd):
    data = read_data_from_store(cmd["getDataId"])
    print("Original Data")
    print(data)

    manipulated_data = manipulate_data(data)
    if manipulated_data is not None:
        print("Manipulated Data")
        print(manipulated_data)

        change_file_permissions(cmd["filePath"])
        write_to_excel_new_sheet(manipulated_data, cmd["filePath"])
