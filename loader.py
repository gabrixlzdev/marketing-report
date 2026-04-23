import pandas as pd

def load_campaings(CSV_FILE):
    # This function will read the CSV file and generate the report
    # You can implement the logic to read the CSV file and process the data as needed

    df = pd.read_csv(CSV_FILE)
    
    columns = df.columns.tolist()
    print("Plese select the column that contains the campaign names:")
    
    for i, column in enumerate(columns): #enumerate the collumns to print them with a number
        print (f"{i+1}. {column}")

    column_campaings = int(input("Enter the number of the column that contains the campaign names: ")) - 1 #get the user input and convert it to an integer, subtract 1 to get the correct index
    
    campaings = df[columns[column_campaings]].unique().tolist()

    print("Available campaigns:")

    for i, campaing in enumerate(campaings): #enumerate the campaings to print them with a number
        print (f"{i+1}. {campaing}")
    
    while True:

        numbers = input('Enter the numbers of the campaigns you want to include in the report, separated by commas: ')
        
        try:
            numbers_list = [int(number.strip()) for number in numbers.split(',')] #get the user input, split it by commas, strip any whitespace, and convert it to a list of integers   

            if any(n<=0 for n in numbers_list):
                print("0 is a invalid input. Please enter valid numbers separated by commas.")
                continue

            selected_campaings = [campaings[n - 1] for n in numbers_list] #get the user input and convert it to a list of campaings (string), subtract 1 to get the correct index
            
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid numbers separated by commas.")
            continue

        break

    return df, columns[column_campaings],selected_campaings
