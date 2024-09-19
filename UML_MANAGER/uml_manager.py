"""
Author : Quang Bui
Created: September 15, 2024

Description:
    This shell will manage uml_class, uml_attribute
    and uml_relationship shells by sharing the data list
    to ensure the consistency between each shell

List of last date modified:
- September 15, 2024 (By Quang)

"""

################################################################
# IMPORTED MODULES #
import json
import os

import UML_UTILITY.SAVE_LOAD.save_load as SAVE_LOAD

################################################################
# LOADING SAVED FILE'S NAMES FROM JSON FILE TO GLOBAL LIST #
saved_file_name_list = SAVE_LOAD.load_name()
# LOADING DATA FROM JSON FILE TO GLOBAL DICTIONARY #
data_list = [[], []]
# Create a class so that we can display it or sort it alphabetically easily
class_list: list[str] = []
# Get list of classes and its attributes
class_and_attr_list = data_list[0]
# Get list of relationships
relationship_list = data_list[1]
# Add class name to class_list
for dictionary in class_and_attr_list:
    class_list.append(dictionary["class_name"])


def update_data(new_data_list: list):
    global data_list, class_list, class_and_attr_list, relationship_list, class_list
    data_list = new_data_list
    class_and_attr_list = data_list[0]
    relationship_list = data_list[1]
    class_list.clear()
    for dictionary in class_and_attr_list:
        class_list.append(dictionary["class_name"])


# Save data to the JSON file
def save_data_to_json(data: dict[str, list[str]], file_name: str):
    file_path = f"UML_UTILITY/SAVE_LOAD/SAVED_FILES/{file_name}.json"
    try:
        if file_name in saved_file_name_list:
            with open(file_path, "r") as file:
                data = json.load(file)
                data.update(data_list)
                return
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
