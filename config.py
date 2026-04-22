import json
import time
from typing import Optional

def save_config(config) -> None:
    with open("config.json","w") as f:
        json.dump(config,f) #converte um dicionário Python para texto no formato JSON e escreve no arquivo.
    
def load_config() -> Optional[dict]:
    try:
        with open("config.json","r") as f:
            config = json.load(f) # lê o texto JSON do arquivo e converte de volta para um dicionário Python.
            return config
    except FileNotFoundError:
        return None
    
def  select_column(column_campaings) -> str:
    for i,column in enumerate(column_campaings):
        print(f"{i+1}. {column}")

    while True: 
        try:    
            column_selected = int(input("Enter the number of the column that contains the data: ")) - 1

            if column_selected < 0 or column_selected >= len(column_campaings):   
                print("Invalid input. Please enter a valid number.")
                continue
        
        except (ValueError):
            print("Invalid input. Please enter a valid number.")
            continue

        break

    return column_campaings[column_selected]
    
def setup_config(config, column_campaings) -> dict:
    
    while True:
    
        if config is None:

            print("No configuration found. Setting up a new configuration...")
            time.sleep(2)

            print("For the spend column data:")
            spend_column = select_column(column_campaings)

            print("For the impressions column data:")
            impressions_column = select_column(column_campaings)

            print("For the reach column data:")
            reach_column = select_column(column_campaings)

            print("For the clicks column data:")
            clicks_column = select_column(column_campaings)

            print("For the conversions column data:")
            conversions_column = select_column(column_campaings)

            print("For the cost per lead column data:")
            cost_per_lead_column = select_column(column_campaings)

            print("For the new contacts column data:")
            new_contacts_column = select_column(column_campaings)

            config = {
                "spend": spend_column,
                "impressions": impressions_column,
                "reach": reach_column,
                "clicks": clicks_column,
                "conversions": conversions_column,
                "cost_per_lead": cost_per_lead_column,
                "new_contacts": new_contacts_column
            }
        
            save_config(config)

            break 

        else:
            print("Configuration found. Using the existing configuration...")
            time.sleep(2)

            use_existing = input("Do you want to use the existing configuration? (y/n): ").lower()

            if use_existing == "n":
                print("Setting up a new configuration...")
                time.sleep(2)
                config = None
                continue
            
            elif use_existing == "y":
                break

    return config
