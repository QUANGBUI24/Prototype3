"""
Author : Quang Bui
Created: September 12, 2024

Description:
    Implement Save / Load features

List of last date modified:
- September 15, 2024 (By Quang)

"""

import json
import os

# Save data to the JSON file
def save_data_to_json(data: dict[str, list[str]], file_path: str):
    if file_path is None:
        return
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
            print("Successfully save data!")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {file_path}.")
        return None


# Load data from the JSON file
def load_data_from_json(file_name: str):
    file_path = f"UML_UTILITY/SAVE_LOAD/SAVED_FILES/{file_name}.json"
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
def save_name_list(name_list: list[str]):
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
    
# # Load chosen saved file
# def load_chosen_saved_file(file_name: str):
#     file_path = f"UML_UTILITY/SAVE_LOAD/SAVED_FILES/{file_name}"
#     try:
#         # Check if file is empty
#         if os.stat(file_path).st_size == 0:
#             return None
#         # Load data from JSON
#         with open(file_path, "r") as file:
#             data = json.load(file)
#             return data
#     except FileNotFoundError:
#         print(f"File {file_path} not found.")
#         return None
#     except json.JSONDecodeError:
#         print(f"Error decoding JSON from {file_path}.")
#         return None
    
# Load all saved file's name from the JSON file "NAME_LIST.json"
def load_name():
    file_path = "UML_UTILITY/SAVE_LOAD/SAVED_FILES/NAME_LIST.json"
    try:
        # Check if file is empty
        if os.stat(file_path).st_size == 0:
            return []
        # Load data from JSON
        with open(file_path, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {file_path}.")
        return None
