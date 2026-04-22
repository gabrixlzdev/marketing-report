import tkinter as tk
from tkinter import filedialog
import os

from loader import load_campaings

def main():

    print("Welcome to the Marketing Report Generator!")
    print("Please select the CSV file containing the marketing data to generate the report.")
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    while True:
        CSV_FILE = filedialog.askopenfilename(title="select the CSV file", filetypes = [("CSV files", "*.csv")]) #path to the csv file

        if not CSV_FILE:
            print("No file selected. select another file.")
            continue

        else:
            confirm = input(f"Is {os.path.basename(CSV_FILE)} the correct file? (y/n): ")

            if confirm.lower() == 'y':
                break
            elif confirm.lower() == 'n':
                continue
            else:
                print("Invalid input. Please enter y or n.")
                
    df, column_campaings, selected_campaings = load_campaings(CSV_FILE) #function to read the csv file and generate the report
    

if __name__ == "__main__":
    main()