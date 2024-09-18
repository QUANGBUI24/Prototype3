import unittest
import os

# Define the test directories and their corresponding test files
TEST_DIRECTORIES = {
    "Attribute Features": "Attribute_Features/uml_attr_test.py",
    "Class Features": "Class_Features/uml_class_test.py",
    "Relationship Features": "Relationship_Features/test_relationship.py",
    "Formatting Validators": "Formating/test_validators.py"
}

def display_test_options():
    """Displays available test files to the user."""
    print("\nAvailable Test Files:")
    for i, (key, value) in enumerate(TEST_DIRECTORIES.items(), start=1):
        print(f"{i}. {key} - ({value})")
    print("0. Exit the test runner")

def get_user_choice():
    """Gets the user's choice for which test to run."""
    try:
        choice = int(input("\nEnter the number of the test to run, or 0 to exit: "))
        if choice == 0:
            return None  # Exit the runner
        elif 1 <= choice <= len(TEST_DIRECTORIES):
            selected_key = list(TEST_DIRECTORIES.keys())[choice - 1]
            return TEST_DIRECTORIES[selected_key]
        else:
            print("Invalid selection. Please enter a number corresponding to the test options.")
            return get_user_choice()
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_user_choice()

def run_tests(test_path=None):
    """Run specified tests or all tests if no specific test is mentioned."""
    if test_path:
        # Run a specific test file based on the selected path
        suite = unittest.defaultTestLoader.loadTestsFromName(test_path.replace('/', '.').replace('.py', ''))
    else:
        # Discover and run all tests from the specific directories
        suite = unittest.TestLoader().discover('UML_UNIT_TESTING', pattern='*.py')

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    while True:
        display_test_options()
        test_path = get_user_choice()
        if test_path is None:
            print("Exiting the test runner. Goodbye!")
            break
        run_tests(test_path)
