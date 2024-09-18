import unittest

def run_tests(test_name=None):
    """Run specified tests or all tests if no specific test is mentioned."""
    if test_name:
        # Run a specific test file
        suite = unittest.defaultTestLoader.loadTestsFromName(test_name)
    else:
        # Discover and run all tests in the 'tests' directory
        suite = unittest.defaultTestLoader.discover('UML_UNIT_TESTING')
    
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    # Simple command-line interface to select tests
    print("Enter the test name to run (e.g., tests.test_A), or press Enter to run all tests:")
    test_name = input("Test Name: ").strip()
    run_tests(test_name if test_name else None)
