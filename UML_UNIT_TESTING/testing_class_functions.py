import sys
import os

# Add the root directory of the project to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import UML_CORE.UML_CLASS.uml_class as UMLClass

######################################################################
# TEST CASES FOR CLASS MANAGEMENT FUNCTIONS #
######################################################################

######################################################################
# Test Add Class All Cases #
print("=== Testing Add Class Functionality ===")

# Test Case 1: Add a valid class
print("Test Case 1: Add a valid class 'chicken'")
UMLClass.add_class("chicken")  # Expected: Successfully adds the class "chicken"

# Test Case 2: Add a class that already exists
print("Test Case 2: Add a class that already exists 'chicken'")
UMLClass.add_class(
    "chicken"
)  # Expected: Print error message that class "chicken" already exists

# Test Case 3: Add a class with invalid name format
print("Test Case 3: Add a class with invalid name format '123Chicken'")
UMLClass.add_class(
    "123Chicken"
)  # Expected: Print error message due to invalid name format

# Test Case 4: Add a class with uppercase valid name format
print("Test Case 4: Add a class with uppercase valid name format 'PLANET'")
UMLClass.add_class("PLANET")  # Expected: Successfully adds the class "planet"

######################################################################
# Test Delete Class All Cases #
print("\n=== Testing Delete Class Functionality ===")

# Test Case 1: Delete a class that exists
print("Test Case 1: Delete a valid class 'chicken'")
UMLClass.delete_class("chicken")  # Expected: Successfully removes the class "chicken"

# Test Case 2: Delete a class that does not exist
print("Test Case 2: Delete a class that does not exist 'dragon'")
UMLClass.delete_class(
    "dragon"
)  # Expected: Print error message that class "dragon" not found

# Test Case 3: Delete a class with invalid name format
print("Test Case 3: Delete a class with invalid name format '123Chicken'")
UMLClass.delete_class(
    "123Chicken"
)  # Expected: Print error message due to invalid name format

######################################################################
# Test Rename Class All Cases #
print("\n=== Testing Rename Class Functionality ===")
UMLClass.add_class("animal")  # Expected: Successfully adds the class "chicken"
# Test Case 1: Rename a class that exists to a valid new name
print("Test Case 1: Rename class 'animal' to existed class 'shape'")
UMLClass.rename_class(
    "animal", "shape"
)  # Expected: Successfully changes name from "animal" to "shape"

# Test Case 2: Rename a class to a name that already exists
print("Test Case 2: Rename class 'person' to an existing class 'shape'")
UMLClass.rename_class(
    "person", "shape"
)  # Expected: Print error message that class "shape" already exists

# Test Case 3: Rename a class to an invalid name format
print("Test Case 3: Rename class 'person' to '123Person'")
UMLClass.rename_class(
    "person", "123Person"
)  # Expected: Print error message due to invalid new name format

# Test Case 4: Rename a class that does not exist
print("Test Case 4: Rename class 'dragon' to 'person'")
UMLClass.rename_class(
    "dragon", "person"
)  # Expected: Print error message that class "dragon" not found

######################################################################
# Test Helper Functions All Cases #
print("\n=== Testing Helper Functions ===")

# Test Case 1: Check class existence helper for an existing class
print("Test Case 1: Check if class 'person' exists")
exists = UMLClass.validate_class_name("person")  # Expected: Returns True
print(f"Class 'person' exists: {exists}")

# Test Case 2: Check class existence helper for a non-existent class
print("Test Case 2: Check if class 'dragon' exists")
exists = UMLClass.validate_class_name("dragon")  # Expected: Returns False
print(f"Class 'dragon' exists: {exists}")

######################################################################
# Test JSON Format Getter All Cases #
print("\n=== Testing JSON Format Getter Functionality ===")

# Test Case 1: Get JSON format for a valid class name
print("Test Case 1: Get JSON format for class 'person'")
json_format = UMLClass.get_class_json_format(
    "person"
)  # Expected: Returns dict format with class "person"
print(f"JSON format for class 'person': {json_format}")

######################################################################
# Test Get Chosen Class All Cases #
print("\n=== Testing Get Chosen Class Functionality ===")

# Test Case 1: Get a class that exists
print("Test Case 1: Get class 'person'")
chosen_class = UMLClass.get_chosen_class(
    "person"
)  # Expected: Returns the dictionary object of the class "person"
print(f"Chosen class 'person': {chosen_class}")

# Test Case 2: Get a class that does not exist
print("Test Case 2: Get class 'dragon'")
chosen_class = UMLClass.get_chosen_class(
    "dragon"
)  # Expected: Returns None and prints error message
print(f"Chosen class 'dragon': {chosen_class}")

######################################################################
# Test Rename Validation All Cases #
print("\n=== Testing Rename Validation Functionality ===")

# Test Case 1: Valid rename case
print("Test Case 1: Check if can rename 'person' to non-existed class 'hero'")
valid = UMLClass.is_able_to_rename(
    "person", "hero"
)  # Expected: True, can rename from "person" to "hero"
print(f"Is able to rename 'person' to 'hero': {valid}")

# Test Case 2: Rename to an existing class name
print("Test Case 2: Check if can rename 'person' to existing class 'shape'")
valid = UMLClass.is_able_to_rename(
    "person", "shape"
)  # Expected: False, cannot rename to an existing class name "chicken"
print(f"Is able to rename 'person' to 'shape': {valid}")

# Test Case 3: Rename using invalid new name format
print("Test Case 3: Check if can rename 'person' to '123Hero'")
valid = UMLClass.is_able_to_rename(
    "person", "123Hero"
)  # Expected: False, invalid format for new class name "123Hero"
print(f"Is able to rename 'person' to '123Hero': {valid}")

######################################################################
# Final Check - List All Classes After Tests #
print("\n=== Final Check: List All Classes After Tests ===")

# Print out the current list of classes and their attributes after all tests
for ele in UMLClass.class_and_attr_list:
    print(ele)
    print()

######################################################################
# END OF TEST CASES #
######################################################################
