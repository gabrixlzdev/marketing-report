import tkinter as tk
from tkinter import filedialog
import os


from loader import load_campaings
from metrics import filter_campaings, calculate_summary
from config import setup_config, load_config
from reporter import generate_report


#we will work with df = data frames.
#| a   | b | c |
#|-----|---|---|
#| x   | 6 | 52|
#| y   | 2 | 17|
#| z   | 12| 4 |

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

    columns = df.columns.tolist() #get the columns of the data frame as a list
    config = load_config() #function to load the configuration from a file
    config = setup_config(config, columns) #function to set up the configuration

    df_filtered = filter_campaings(df, column_campaings, selected_campaings) #function to filter the data based on the selected campaigns
    
    summary = calculate_summary(df_filtered,config) #function to calculate the summary of the data

    generate_report(summary, df_filtered,column_campaings,selected_campaings) #function to generate the report

if __name__ == "__main__":
    main()