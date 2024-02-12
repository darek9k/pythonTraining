import openpyxl

from page_object_pattern.utils.search_data import SearchData


class ExcelReader:
    @staticmethod
    def get_data():
        wb = openpyxl.load_workbook("../utils/Dane.xlsx")
        sheet = wb.active
        data = []
        for row in sheet.iter_rows(min_row=2):
            search_data = SearchData(row[0].value, row[1].value)
            data.append(search_data)
        return data
