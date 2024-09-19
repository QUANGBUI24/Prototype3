"""
Author : Quang Bui
Created: September 12, 2024

Description:
    Implement Save / Load features

List of last date modified:
- September 15, 2024 (By Quang)

"""

import json


# Save data to the JSON file
def save_data_to_json(data: dict[str, list[str]], file_path: str):
    if file_path is None:
        return
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
            print("Succesfully save data!")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {file_path}.")
        return None


# Load data from the JSON file
def load_data_from_json(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {file_path}.")
        return None
    
# Saving saved file's names to JSON file
def save_name(name_list: list[str]):
    file_path = "UML_UTILITY/SAVE_LOAD/SAVED_FILES/NAME_LIST.json"
    try:
        with open(file_path, "w") as file:
            json.dump(name_list, file, indent=4)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {file_path}.")
        return None
    
# Load data from the JSON file
def load_name():
    file_path = "UML_UTILITY/SAVE_LOAD/SAVED_FILES/NAME_LIST.json"
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {file_path}.")
        return None
