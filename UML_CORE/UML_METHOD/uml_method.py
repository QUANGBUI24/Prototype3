################################################################
# IMPORTED MODULES #

import UML_CORE.UML_CLASS.uml_class as UML_CLASS
import UML_MANAGER.uml_manager as UML_MANAGER
from UML_UTILITY.FORMAT_CHECKING.validators import check_format

################################################################

# GET CLASS AND ITS METHODS LIST #
class_and_attr_and_method_list = UML_MANAGER.class_and_attr_and_method_list

################################################################
# ADD, DELETE, RENAME METHOD FUNCTIONS #

# Function to add an method to a class #
def add_method(class_name:str, method_name:str):
    # Put class name in lowercase
    class_name = class_name
    # Check if class name exists, 
    # if not, called function will print error, current function stops
    is_class_exist = UML_CLASS.check_class_name(class_name, should_exist=True)
    if not is_class_exist:
        return
    # Get method list for specific class
    method_list = get_method_list(class_name)
    method_name = method_name
    # Check if method already exists
    # if it does, called function will print error, current function ends
    is_method_exist = check_method_name(method_list, method_name,class_name,False)
    if not is_method_exist:
        return
    # Make sure user want to add method or not
    is_chosen_yes = user_choice(f"add method '{method_name}' to class '{class_name}'")
    if not is_chosen_yes:
        return
    # Create JSON object for method
    json_method = get_method_json_format(method_name)
    # Add JSON method object to global object that holds classes
    for cls in class_and_attr_and_method_list:
        if (cls["class_name"] == class_name):
            cls["method_list"].append(json_method)
    # Print successful message 
    print(f"Method '{method_name}' was successfully added to class '{class_name}'!")
     

# Function to delete an method from a class #
def delete_method(class_name:str, method_name:str):
    # Put class name in lowercase
    class_name = class_name
    # Check if class name exists, 
    # if not, called function will print error, current function stops
    is_class_exist = UML_CLASS.check_class_name(class_name, should_exist=True)
    if not is_class_exist:
        return
    # Get method list for specific class
    method_list = get_method_list(class_name)
    # method name lowercase
    method_name = method_name
    # Check if method already exists
    # if not, called function will print error, current function ends
    is_method_exist = check_method_name(method_list, method_name,class_name, True)
    if not is_method_exist:
        return
    # Make sure user want to delete method or not
    is_chosen_yes = user_choice(f"delete method '{method_name}' from class '{class_name}'")
    if not is_chosen_yes:
        return
    # Get method object that exists in class object
    method_object = get_method_object(method_list, method_name)  
    # Find and delete method object
    for cls in class_and_attr_and_method_list:
        if (cls["class_name"] == class_name):
            cls["method_list"].remove(method_object)
    # Print successful message 
    print(f"Method '{method_name}' was successfully deleted from class '{class_name}'!")
    

# Function to rename an method in a class
def rename_method(class_name:str, old_method_name:str, new_method_name:str):
    # Put class name in lowercase
    class_name = class_name
    # Check if class name exists, 
    # if not, called function will print error, current function stops
    is_class_exist = UML_CLASS.check_class_name(class_name, should_exist=True)
    if not is_class_exist:
        return
    # Get method list for specific class
    method_list = get_method_list(class_name)
    # Lowercase both methods
    old_method_name = old_method_name
    new_method_name = new_method_name
    # Check if old method name already exists
    # if not, called function will print error, current function ends
    is_old_method_exist = check_method_name(method_list, old_method_name,class_name, True)
    if not is_old_method_exist:
        return False
    # Check if new method name already exists
    # if it does, called function will print error, current function ends
    is_new_method_exist = check_method_name(method_list, new_method_name,class_name, False)
    if not is_new_method_exist:
        return
    # Make sure user want to rename method or not
    is_chosen_yes = user_choice(f"Rename method name '{old_method_name}' to method name '{new_method_name}' from class '{class_name}'")
    if not is_chosen_yes:
        return   
    # Find old method and change name to new method
    for cls in class_and_attr_and_method_list:
        if (cls["class_name"] == class_name):
            for method in cls["method_list"]:
                if method["method_name"] == old_method_name:
                    method["method_name"] = new_method_name
    # Print successful message
    print(f"Method '{old_method_name}' was renamed to '{new_method_name}' in class '{class_name}'!")




################################################################
# CHECK METHOD FUNCTIONS #

# Check Method Name Exist Helper #
def validate_method_name(method_list:str, method_name: str):
    for method in method_list:
        if method["method_name"] == method_name:
            return True
    return False

# Check if method name exists or doesnt exist depending on should_exist param 
# when given list of methods, method name and class name
def check_method_name(method_list:str, method_name:str,class_name:str, should_exist:bool) -> bool:
    # Check format of method_name, stop function and print error if not correct
    is_format_correct = check_format(method_name)
    if is_format_correct != "Valid input":
        print(is_format_correct)
        return False
    # Check if method exists
    is_method_exist = validate_method_name(method_list, method_name)
    # If the name should exist but not exist
    if should_exist and not is_method_exist:
        print(f"Method '{method_name}' not found in class '{class_name}'!")
        return False
    # If the name should not exist but still exist
    elif not should_exist and is_method_exist:
        print(f"Method '{method_name}' already existed in class '{class_name}'!")
        return False
    # True in any other cases
    return True
    

################################################################
# OTHER HELPER FUNCTIONS #

# Assuming we already know class_name exists, 
# and class_name is in correct format
# Get the method list for specific class
def get_method_list(class_name:str) -> list:
    for cls in class_and_attr_and_method_list:
        if (cls["class_name"] == class_name):
            return cls["method_list"]
        
# Get JSON Format of Method #
def get_method_json_format(method_name: str) -> dict[str, str]:
    return {
        "method_name": method_name
    }

# Get the method object from a list of methods,
# Assuming we know the method exists
# ONLY CALL IF YOU ALREADY CHECKED IF METHOD EXISTS #
def get_method_object(method_list:str, method_name) -> dict[str, str]:
    for method in method_list:
        if (method["method_name"] == method_name):
            return method
        
# User Decision Making #
def user_choice(action: str) -> bool:
    while True:
        user_input = input(f"Are you sure you want to {action}? (Yes/No): ").lower()
        if user_input in ["yes", "y"]:
            return True
        elif user_input in ["no", "n"]:
            print("Action cancelled.")
            return False
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

################################################################

