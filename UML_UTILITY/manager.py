################################################################
#   Author : Quang Bui
#   Created: September 12, 2024
#
#   This class will manage all the the actions in the program
################################################################


################################################################
# IMPORTED MODULES #
import os
import sys

# Add the project root directory to sys.path (ChatGPT instruction)
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)  # This must be placed first before importing

import UML_UTILITY.save_load as SAVE_LOAD
from UML_UTILITY.validators import check_format

################################################################

# LOADING DATA FROM JSON FILE TO GLOBAL DICTIONARY #
data_list = SAVE_LOAD.load_data_from_json("data.json")

# GET THE LIST OF DICTIONARY OF CLASS NAME AND ITS ATTRIBUTE #
if data_list[0] is not None:
    class_and_attr_list = data_list[0]
else:
    print("Something's wrong with the data.json file!!!!")

# print(type(class_and_attr_list))

################################################################################
# WORKING WITH CLASSES #


# Add Class #
def add_class(class_name: str):
    # After checking format, check if class_name already existed or not
    is_name_exist = check_class_name(class_name, should_exist=False)
    # If not, prompt error
    if not is_name_exist:
        return
    # Convert to json object and append to the list
    transformed_json_object = get_class_json_format(class_name)
    class_and_attr_list.append(transformed_json_object)
    print(f"Added class '{class_name}' successfully!")


# Delete Class #
def delete_class(class_name: str):
    # After checking format, check if class_name already existed or not
    is_name_exist = check_class_name(class_name, should_exist=True)
    # If not, prompt error
    if not is_name_exist:
        return
    # If class exist, get the class object and pop from the list
    class_object = get_chosen_class(class_name)
    class_and_attr_list.remove(class_object)
    print(f"Successfully removed class '{class_name}'!")


# Rename Class #
def rename_class(class_name: str, new_name: str):
    # If class exist, remove the class, else prompt error'
    able_to_rename = is_able_to_rename(class_name, new_name)
    if not able_to_rename:
        return
    # If it is able to rename, get the object from the list
    class_object = get_chosen_class(class_name)
    # Change to new name
    class_object["class_name"] = new_name
    print(f"Successfully changed class name from '{class_name}' to '{new_name}'!")


################################################################################
# CHECKING CLASS NAME #


# Check Class Name Exist Helper #
def validate_class_name(class_name: str):
    for dictionary in class_and_attr_list:
        if dictionary["class_name"] == class_name:
            return True
    return False


# Check Class Name Exist Including Prompting Error Messages #
def check_class_name(class_name: str, should_exist: bool) -> bool:
    is_format_correct = check_format(class_name)
    if is_format_correct != "Valid input":
        print(is_format_correct)
        return False
    is_name_exist: bool = validate_class_name(class_name)
    # If the name should exist but not exist
    if should_exist and not is_name_exist:
        print(f"Class '{class_name}' not found!")
        return False
    # If the name should not exist but still exist
    elif not should_exist and is_name_exist:
        print(f"Class '{class_name}' has already existed!")
        return False
    # True in any other cases
    return True


# Helper Function To Check Both Current Name And New Name In 'rename_class()' #
def is_able_to_rename(class_name: str, new_name: str) -> bool:
    # Check current class name format
    class_name_result = check_format(class_name)
    if class_name_result != "Valid input":
        # If not valid, prompt error
        print(class_name_result)
        return False
    # Check new class name format
    new_class_name_result = check_format(new_name)
    if new_class_name_result != "Valid input":
        # If not valid, prompt error
        print(new_class_name_result)
        return False
    # After checking format, check if class_name and new_name already existed or not
    is_current_name_exist = check_class_name(class_name, should_exist=True)
    if not is_current_name_exist:
        return False
    is_new_name_exist = check_class_name(new_name, should_exist=False)
    if not is_new_name_exist:
        return False
    return True


################################################################################
# OTHER HELPER FUNCTIONS #


# Get JSON Format #
# NOTE: Don't call this class if you did not check for class name!!!!!!! #
def get_class_json_format(class_name: str) -> dict[str, list[dict[str, str]]]:
    return {
        "attr_list": [{"attr_name": ""}],  # Placeholder for attribute names
        "class_name": class_name,
    }


# Get Chosen Class #
def get_chosen_class(class_name: str) -> dict[str, list[dict[str, str]]]:
    for dictionary in class_and_attr_list:
        if dictionary["class_name"] == class_name:
            return dictionary


# Display Class List #
def display_class_list():
    print("\n===================")
    print("--Class List--")
    for dictionary in class_and_attr_list:
        print(dictionary["class_name"])
    print("===================")


# Display Class Details #
def display_class_detail(class_name: str):
    class_object = get_chosen_class(class_name)
    print("\n===================")
    print("--Class Name--")
    print(f"{class_object['class_name']}")  # Center with 20 spaces
    print("*******************")
    attr_list = class_object["attr_list"]
    print("--Class Attribute--")
    for element in attr_list:
        for key, val in element.items():
            print(f"{val}")
    print("===================")


################################################################################


# add_class("Shape")
# add_class("Animal")
# add_class("House")
# rename_class("Shape", "Tree")
# SAVE_LOAD.save_data_from_json(data_list, "data.json")
