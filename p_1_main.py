# Program function: ECD transferred to check layout


from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "시트1"
wb.save(filename="테스트.xlsx")
