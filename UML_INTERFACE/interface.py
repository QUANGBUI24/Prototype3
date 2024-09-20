"""
Author : Quang Bui
Created: September 12, 2024

Description:
    Command Line User Interface

List of last date modified:
- September 15, 2024 (By Quang)

"""

import os
from enum import Enum
from itertools import zip_longest

import UML_CORE.UML_ATTRIBUTE.uml_attribute as UML_ATTRIBUTE
import UML_CORE.UML_CLASS.uml_class as UML_CLASS
import UML_CORE.UML_RELATIONSHIP.uml_relationship as UML_REL
import UML_MANAGER.uml_manager as UML_MANAGER


class InterfaceOptions(Enum):
    WORK = "work"
    LIST_CLASS = "list_class"
    CLASS_DETAIL = "class_detail"
    CLASS_REL = "class_rel"
    SAVED_LIST = "saved_list"
    SAVE = "save"
    LOAD = "load"
    DELETE_SAVED = "delete_saved"
    CLEAR_DATA = "clear_data"
    SORT = "sort"
    HELP = "help"
    EXIT = "exit"


class UMLClassInterfaceOption(Enum):
    ADD_CLASS = "add_class"
    DELETE_CLASS = "delete_class"
    RENAME = "rename_class"
    ADD_ATTR = "add_attr"
    DELETE_ATTR = "delete_attr"
    RENAME_ATTR = "rename_attr"
    ADD_REL = "add_rel"
    DELETE_REL = "delete_rel"
    HELP = "help"
    BACK = "back"


def prompt_main_menu():
    print("Welcome To Our UML Program!")
    print("Type 'work' start working with class(es)")
    print("Type 'list_class' to see the list of all created class(es)")
    print("Type 'class_detail <class_name>' to see the detail of the chosen class")
    print("Type 'class_rel' to see the relationships between class(es)")
    print("Type 'saved_list' to see the list of saved files")
    print("Type 'save' to save data")
    print("Type 'load' to load data from saved files")
    print("Type 'delete_saved to delete saved file")
    print("Type 'clear_data' to delete all the data in the current storage")
    print("Type 'sort' to sort the class list in alphabetical order")
    print("Type 'help' to see the instructions")
    print("Type 'exit' to quit program")


def prompt_working_menu():
    # Class
    print("Type 'add_class <class_name>' to add a class")
    print("Type 'delete_class <class_name>' to delete a class")
    print("Type 'rename_class <class_name> <new_name>' to rename a class")
    # Attribute
    print("Type 'add_attr <class_name> <attr_name>' to add an attribute")
    print(
        "Type 'delete_attr <class_name> <attr_name>' to delete an attribute from the chosen class"
    )
    print(
        "Type 'rename_attr <class_name> <current_attribute_name> <new_name>' to rename an attribute"
    )
    # Relationship
    print(
        "Type 'add_rel <source_class> <destination_class_name> <relationship_level>' to add relationship and relationship level"
    )
    print(
        "Type 'delete_rel <chosen_class_name> <destination_class_name>' to delete a relationship"
    )
    print("Type 'help' to see the instruction")
    print("Type 'back' to go back to main menu'")


def working_loop():
    prompt_working_menu()
    while True:
        print("\n(work-menu)\n")
        print("\n==> ", end="")
        user_input: str = input()
        # Split the input by space
        user_input_component = user_input.split()
        # Get separate command and class name part
        command = user_input_component[0]
        first_param = user_input_component[1] if len(user_input_component) > 1 else None
        second_param = (
            user_input_component[2] if len(user_input_component) > 2 else None
        )
        third_param = user_input_component[3] if len(user_input_component) > 3 else None
        # Start the logic
        #######################################################
        # Add class
        if command == UMLClassInterfaceOption.ADD_CLASS.value and first_param:
            UML_CLASS.add_class(first_param)
        # Delete class
        elif command == UMLClassInterfaceOption.DELETE_CLASS.value and first_param:
            UML_CLASS.delete_class(first_param)
        # Rename class
        elif (
            command == UMLClassInterfaceOption.RENAME.value
            and first_param
            and second_param
        ):
            UML_CLASS.rename_class(first_param, second_param)

        #######################################################

        # Add attribute
        elif (
            command == UMLClassInterfaceOption.ADD_ATTR.value
            and first_param
            and second_param
        ):
            UML_ATTRIBUTE.add_attr(first_param, second_param)
        # Delete attribute
        elif (
            command == UMLClassInterfaceOption.DELETE_ATTR.value
            and first_param
            and second_param
        ):
            UML_ATTRIBUTE.delete_attr(first_param, second_param)
        # Rename attribute
        elif (
            command == UMLClassInterfaceOption.RENAME_ATTR.value
            and first_param
            and second_param
            and third_param
        ):
            UML_ATTRIBUTE.rename_attr(first_param, second_param, third_param)

        #######################################################

        # Add relationship
        elif (
            command == UMLClassInterfaceOption.ADD_REL.value
            and first_param
            and second_param
            and third_param
        ):
            UML_REL.add_relationship(first_param, second_param, third_param)
        # Delete relationship
        elif (
            command == UMLClassInterfaceOption.DELETE_REL.value
            and first_param
            and second_param
        ):
            UML_REL.remove_relationship(first_param, second_param)

        #######################################################
        # See menu again
        elif command == UMLClassInterfaceOption.HELP.value:
            prompt_working_menu()
        #######################################################
        # Go back to main menu
        elif command == UMLClassInterfaceOption.BACK.value:
            prompt_main_menu()
            break
        else:
            print(
                "Unknown command or wrong argument, see the instruction for more details"
            )


def main_program_loop():
    prompt_main_menu()
    while True:
        print("\n(main-menu)\n")
        print("\n==> ", end="")
        user_input: str = input()
        # Split the input by space
        user_input_component = user_input.split()
        command = user_input_component[0]
        # Check if command has an associated class name
        first_param = user_input_component[1] if len(user_input_component) > 1 else None
        # Go to the working menu
        if command == InterfaceOptions.WORK.value:
            working_loop()
        # List all the created class names or all class detail
        elif command == InterfaceOptions.LIST_CLASS.value:
            display_wrapper()
        # Show the details of the chosen class
        elif command == InterfaceOptions.CLASS_DETAIL.value and first_param:
            display_single_class_detail(first_param)
        # Show the relationship of the chosen class with others
        elif command == InterfaceOptions.CLASS_REL.value:
            display_relationship_list()
        # Show the list of saved files
        elif command == InterfaceOptions.SAVED_LIST.value:
            display_saved_file_name()
        # Show the main menu again
        elif command == InterfaceOptions.HELP.value:
            prompt_main_menu()
        # Sort the class list
        elif command == InterfaceOptions.SORT.value:
            sort_class_list()
        # Save the data
        elif command == InterfaceOptions.SAVE.value:
            saving_file_wrapper()
        # Load the data
        elif command == InterfaceOptions.LOAD.value:
            loading_file_wrapper()
        # Delete saved file
        elif command == InterfaceOptions.DELETE_SAVED.value:
            delete_saved_file_wrapper()
        # Clear data in current storage
        elif command == InterfaceOptions.CLEAR_DATA.value:
            clear_current_data()
        # Exit the program
        elif command == InterfaceOptions.EXIT.value:
            break
        else:
            print(
                f"Unknown command '{user_input}'. Type 'help' for a list of commands."
            )
    exit()


########################################################################################################
# DISPLAY METHODS #

# Display wrapper function #
def display_wrapper():
    if len(UML_MANAGER.class_and_attr_list) == 0:
        print("No class to display!")
    else:
        is_detail = ask_user_choices("print all class detail")
        if is_detail:
            display_class_list_detail()
        else:
            display_list_of_only_class_name()


# Display only list of class names #
def display_list_of_only_class_name():
    print("\n|===================|")
    print(f"{"--     Name     --":^20}")
    print("|*******************|")
    class_list = UML_MANAGER.class_list
    for class_name in class_list:
        print(f"{class_name:^20}")
    print("|===================|")


# Display Class List #
def display_class_list_detail(classes_per_row=3):
    # Generate class details split into lines
    class_details_list = [
        get_class_detail(class_name).split("\n")
        for class_name in UML_MANAGER.class_list
    ]
    print(
        "\n-------------------------------------------------------------------------------------------------\n"
    )
    # Chunk the class details into groups of `classes_per_row`
    for i in range(0, len(class_details_list), classes_per_row):
        chunk = class_details_list[i : i + classes_per_row]

        # Use zip_longest to align and print side by side
        for lines in zip_longest(*chunk, fillvalue=" " * 20):
            print("   ".join(line.ljust(30) for line in lines))
        print(
            "\n-------------------------------------------------------------------------------------------------\n"
        )


# Display Relationship List #
def display_relationship_list(classes_per_row=3):
    # Generate class details split into lines
    class_relationship_detail_list = [
        get_relationship_detail(class_name).split("\n")
        for class_name in UML_MANAGER.class_list
    ]
    print(
        "\n-------------------------------------------------------------------------------------------------\n"
    )
    # Chunk the class relationship details into groups of `classes_per_row`
    for i in range(0, len(class_relationship_detail_list), classes_per_row):
        chunk = class_relationship_detail_list[i : i + classes_per_row]

        # Use zip_longest to align and print side by side
        for lines in zip_longest(*chunk, fillvalue=" " * 20):
            print("   ".join(line.ljust(30) for line in lines))
        print(
            "\n-------------------------------------------------------------------------------------------------\n"
        )


# Display Class Details #
def display_single_class_detail(class_name: str):
    classes_detail_list = get_class_detail(class_name)
    print(f"\n{classes_detail_list}")


# Display saved file's names #
def display_saved_file_name():
    print("\n|===================|")
    for dictionary in UML_MANAGER.saved_file_name_list:
        for key in dictionary:
            print(f"{key:^20}")
    print("|===================|\n")


########################################################################################################
# GET DETAILS METHODS #


# Class Detail As String #
def get_class_detail(class_name: str) -> str:
    class_object = UML_CLASS.get_chosen_class(class_name)
    if class_object is None:
        print(f"Class '{class_name}' does not exist!")
        return
    output = []
    output.append("|===================|")
    output.append(f"{"--     Name     --":^21}")
    output.append(f"{class_object['class_name']:^20}")
    output.append("|*******************|")
    attr_list = class_object["attr_list"]
    output.append(f"{"--  Attribute  --":^21}")
    for element in attr_list:
        for key, val in element.items():
            output.append(f"{val:^20}")
    output.append("|*******************|")
    rel_list = UML_MANAGER.relationship_list
    output.append(f"{"-- Relationship  --":^21}")
    for element in rel_list:
        if element["source"] == class_name:
            output.append(f"{"|-----------|":^20}")
            output.append(f"{element["source"]:^20}")
            output.append(f"{element["dest"]:^20}")
            output.append(f"{element["relation"]:^20}")
            output.append(f"{"|-----------|":^20}")

    output.append("|===================|")
    return "\n".join(output)


# Get Class Relationships #
def get_relationship_detail(class_name: str) -> str:
    class_object = UML_CLASS.get_chosen_class(class_name)
    output = []
    output.append("|===================|")
    output.append(f"{"--     Name     --":^21}")
    output.append(f"{class_object['class_name']:^20}")
    output.append("|*******************|")
    rel_list = UML_MANAGER.relationship_list
    output.append("|===================|")
    output.append(f"{"-- Relationship  --":^21}")
    for element in rel_list:
        if element["source"] == class_name:
            output.append(f"{"|-----------|":^20}")
            output.append(f"{element["source"]:^20}")
            output.append(f"{element["dest"]:^20}")
            output.append(f"{element["relation"]:^20}")
            output.append(f"{"|-----------|":^20}")
    output.append("|===================|")
    return "\n".join(output)


########################################################################################################
# SAVE/LOAD RELATED METHODS #

# Wrapper for saving function
def saving_file_wrapper():
    file_name = get_file_name_to_save()
    if file_name == "quit":
        print()
        prompt_main_menu()
        return
    is_saving = ask_user_choices(f"save data to file '{file_name}.json'")
    if not is_saving:
        print("Canceled saving!")
        return
    UML_MANAGER.save_data_to_json(file_name)
        

# Wrapper for loading function
def loading_file_wrapper():
    file_name = get_file_name_to_delete_load_clear("load")
    if file_name == "quit":
        print()
        prompt_main_menu()
        return
    is_loading = saved_file_name_check(file_name)
    if not is_loading:
        print(f"\nFile '{file_name}.json' does not exist")
        return
    new_data_list = UML_MANAGER.data_list = UML_MANAGER.load_data_from_json(file_name)
    if new_data_list is not None:
        check_file_and_set_status(file_name)
        UML_MANAGER.update_data(new_data_list)
        keep_updating_data()
        print(f"Successfully loaded file '{file_name}.json'")
        
# Wrapper for Delete saved file
def delete_saved_file_wrapper():
    # Provide saved file's name
    file_name = get_file_name_to_delete_load_clear("delete")
    if file_name == "quit":
        print()
        prompt_main_menu()
        return
    # Check if the name exists or not, if not, stop, else remove it
    is_name_exist = saved_file_name_check(file_name)
    if not is_name_exist:
        print(f"\nFile '{file_name}.json' does not exist")
        return
    is_delete_saved_file = ask_user_choices(f"delete saved file '{file_name}.json'")
    if not is_delete_saved_file:
        print("Canceled deleting!")
        return
    delete_saved_file(file_name)


# Delete Saved File #
def delete_saved_file(file_name: str):
    # Get saved file's name list
    name_list = UML_MANAGER.saved_file_name_list
    for dictionary in name_list:
        if file_name in dictionary:
            name_list.remove(dictionary)
    file_path = f"UML_UTILITY/SAVED_FILES/{file_name}.json"
    UML_MANAGER.save_name_list(name_list)
    os.remove(file_path)
    print(f"\nSuccessfully removed file '{file_name}.json'")


# Asking users to provide name for the file they want to save
def get_file_name_to_save() -> str:
    # Prompt the user for a file name to save
    print("\nPlease provide a name for the file you'd like to save or type 'quit' to go back to main menu:")
    display_saved_file_name()
    print("==>", end=" ")
    file_name = input()
    # Get the saved file name list (which is now a list of dictionaries)
    name_list = UML_MANAGER.saved_file_name_list
    # Check if the file name already exists in any dictionary in the list
    file_exists = any(file_name in dictionary for dictionary in name_list)
    # If the file name doesn't exist, add it to the list as a new dictionary
    if not file_exists and file_name != "quit":
        name_list.append({file_name: "on"})
        UML_MANAGER.save_name_list(name_list)
    return file_name  # Return the file name


# Asking users to provide name for the file they want to delete, load or clear
def get_file_name_to_delete_load_clear(place_holder: str) -> str:
    name_list = UML_MANAGER.saved_file_name_list
    if len(name_list) == 0:
        print("No saved file exists!\n")
        return
    print(f"\nPlease choose the file you want to {place_holder} or type 'quit' to go back to menu:")
    display_saved_file_name()
    print("\n==>", end=" ")
    file_name = input()
    return file_name


# Saved File Name Check #
def saved_file_name_check(save_file_name: str) -> bool:
    name_list = UML_MANAGER.saved_file_name_list
    for dictionary in name_list:
        for key in dictionary:
            if key == save_file_name:
                return True
    return False


########################################################################################################
# SAVED FILES HELPER METHODS #

def set_file_status(file_name: str, status: str):
    name_list = UML_MANAGER.saved_file_name_list
    for dictionary in name_list:
        for key in dictionary:
            if key == file_name:
                dictionary[key] = status
    UML_MANAGER.save_name_list(name_list)


def check_file_and_set_status(file_name: str) -> str:
    name_list = UML_MANAGER.saved_file_name_list
    for dictionary in name_list:
        for key in dictionary:
            if dictionary[key] == "on":
                dictionary[key] = "off"
    set_file_status(file_name, status="on")
    return file_name


def set_all_file_off():
    name_list = UML_MANAGER.saved_file_name_list
    for dictionary in name_list:
        for key in dictionary:
            dictionary[key] = "off"
    UML_MANAGER.save_name_list(name_list)


def clear_current_data():
    name_list = UML_MANAGER.saved_file_name_list
    if len(name_list) == 0:
        print("File is empty!\n")
        return
    for dictionary in name_list:
        for key in dictionary:
            if dictionary[key] == "on":
                data_list = UML_MANAGER.data_list = [[], []]
                UML_MANAGER.update_data(data_list)
                keep_updating_data()
                UML_MANAGER.save_data_to_json(key)
                print(f"Successfully clear data in file '{key}'")
                return
    print("No active file!")

########################################################################################################
# OTHER METHODS #

# Asking if user choices
def ask_user_choices(action: str) -> bool:
    while True:
        user_input = input(
            f"\nDo you want to {action}? (Yes/No): "
        ).lower()
        if user_input in ["yes", "y"]:
            return True
        elif user_input in ["no", "n"]:
            return False
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")


def exit():
    set_all_file_off()
    print("Exited Program")


# Sorting Class List #
def sort_class_list():
    UML_CLASS.class_list.sort()
    display_class_list_detail()


# Updating The Data #
def keep_updating_data():
    # Update the UML_CLASS
    UML_CLASS.data_list = UML_MANAGER.data_list
    UML_CLASS.class_and_attr_list = UML_MANAGER.class_and_attr_list
    UML_CLASS.relationship_list = UML_MANAGER.relationship_list
    UML_CLASS.class_list = UML_MANAGER.class_list
    # Update the UML_ATTRIBUTE
    UML_ATTRIBUTE.class_and_attr_list = UML_MANAGER.class_and_attr_list
    UML_ATTRIBUTE.class_list = UML_MANAGER.class_list
    # Update the UML_RELATIONSHIP
    UML_REL.data_list = UML_MANAGER.data_list
    UML_REL.class_and_attr_list = UML_MANAGER.class_and_attr_list
    UML_REL.relationship_list = UML_MANAGER.relationship_list
    UML_REL.class_list = UML_MANAGER.class_list


########################################################################################################
