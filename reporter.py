from openpyxl import Workbook
from tkinter import filedialog


def generate_report(summary, df_filtered: dict) -> None:
    # This function will generate the report based on the summary of the data
    # You can implement the logic to create a new sheet in the workbook and write the summary of the data to it as needed

    wb= Workbook() # create a new workbook (sheet) to store the summary of the data
    ws = wb.active # get the active sheet in the workbook

    ouput_path = filedialog.asksaveasfilename(
        title= "Save reporte as",
        defaultextension=".xlsx",
        filetypes=[("Excel files", "*.xlsx")]
    )

    

    ws.title = "Summary" # set the title of the sheet to "Summary"

    i=0
    keys = list(summary.keys()) #get the keys of the summary dictionary as a list
    values = list(summary.values()) #get the values of the summary dictionary as a list

    while i < len(summary):
        ws.cell(row=1, column=i+1).value = keys[i] #write the keys of the summary dictionary to the first row of the sheet
        ws.cell(row=2, column=i+1).value = values[i] #write the values of the summary dictionary to the second row of the sheet
        i+=1

    wb.save(ouput_path) # save the workbook to the specified path
    



