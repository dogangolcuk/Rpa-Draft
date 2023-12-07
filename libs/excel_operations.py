# from openpyxl import Workbook
from common_imports import Workbook
from libs.logging_utils import log_message


def open_excel_and_write():
    try:
        workbook = Workbook()
        sheet = workbook.active
        sheet['E5'] = "Data written from RPA script WITH PYTHON"
        workbook.save('output.xlsx')
        log_message("Opened Excel and wrote data successfully.")
    except Exception as e:
        log_message(f"Error opening Excel and writing data: {e}")
