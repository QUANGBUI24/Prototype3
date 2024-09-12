import manager as MANAGER

######################################################################
# TEST CASES FOR CLASS MANAGEMENT FUNCTIONS #
######################################################################

######################################################################
# Test Add Class All Cases #

# Test Case 1: Add a valid class
MANAGER.add_class("chicken")  # Expected: Successfully adds the class "chicken"

# Test Case 2: Add a class that already exists
MANAGER.add_class(
    "chicken"
)  # Expected: Print error message that class "chicken" already exists

# Test Case 3: Add a class with invalid name format
MANAGER.add_class(
    "123Chicken"
)  # Expected: Print error message due to invalid name format

######################################################################
# Test Delete Class All Cases #

# Test Case 1: Delete a class that exists
MANAGER.delete_class("chicken")  # Expected: Successfully removes the class "chicken"

# Test Case 2: Delete a class that does not exist
MANAGER.delete_class(
    "dragon"
)  # Expected: Print error message that class "dragon" not found

# Test Case 3: Delete a class with invalid name format
MANAGER.delete_class(
    "123Chicken"
)  # Expected: Print error message due to invalid name format

######################################################################
# Test Rename Class All Cases #

# Test Case 1: Rename a class that exists to a valid new name
MANAGER.rename_class(
    "chicken", "person"
)  # Expected: Successfully changes name from "chicken" to "person"

# Test Case 2: Rename a class to a name that already exists
MANAGER.rename_class(
    "person", "chicken"
)  # Expected: Print error message that class "chicken" already exists

# Test Case 3: Rename a class to an invalid name format
MANAGER.rename_class(
    "person", "123Person"
)  # Expected: Print error message due to invalid new name format

# Test Case 4: Rename a class that does not exist
MANAGER.rename_class(
    "dragon", "person"
)  # Expected: Print error message that class "dragon" not found

######################################################################
# Test Helper Functions All Cases #

# Test Case 1: Check class existence helper for an existing class
exists = MANAGER.validate_class_name("person")  # Expected: Returns True
print(f"Class 'person' exists: {exists}")

# Test Case 2: Check class existence helper for a non-existent class
exists = MANAGER.validate_class_name("dragon")  # Expected: Returns False
print(f"Class 'dragon' exists: {exists}")

######################################################################
# Test JSON Format Getter All Cases #

# Test Case 1: Get JSON format for a valid class name
json_format = MANAGER.get_class_json_format(
    "person"
)  # Expected: Returns dict format with class "person"
print(f"JSON format for class 'person': {json_format}")

# Test Case 2: Get JSON format for an invalid class name format
json_format = MANAGER.get_class_json_format(
    "123Person"
)  # Expected: Returns dict format despite invalid format (handled elsewhere)
print(f"JSON format for class '123Person': {json_format}")

######################################################################
# Test Get Chosen Class All Cases #

# Test Case 1: Get a class that exists
chosen_class = MANAGER.get_chosen_class(
    "person"
)  # Expected: Returns the dictionary object of the class "person"
print(f"Chosen class 'person': {chosen_class}")

# Test Case 2: Get a class that does not exist
chosen_class = MANAGER.get_chosen_class(
    "dragon"
)  # Expected: Returns None and prints error message
print(f"Chosen class 'dragon': {chosen_class}")

######################################################################
# Test Rename Validation All Cases #

# Test Case 1: Valid rename case
valid = MANAGER.is_able_to_rename(
    "person", "hero"
)  # Expected: True, can rename from "person" to "hero"
print(f"Is able to rename 'person' to 'hero': {valid}")

# Test Case 2: Rename to an existing class name
valid = MANAGER.is_able_to_rename(
    "person", "chicken"
)  # Expected: False, cannot rename to an existing class name "chicken"
print(f"Is able to rename 'person' to 'chicken': {valid}")

# Test Case 3: Rename using invalid new name format
valid = MANAGER.is_able_to_rename(
    "person", "123Hero"
)  # Expected: False, invalid format for new class name "123Hero"
print(f"Is able to rename 'person' to '123Hero': {valid}")

######################################################################
# Final Check - List All Classes After Tests #

# Print out the current list of classes and their attributes after all tests
print()
for ele in MANAGER.class_and_attr_list:
    print(ele)
    print()

######################################################################
# END OF TEST CASES #
######################################################################
