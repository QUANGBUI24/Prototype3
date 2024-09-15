import os
import subprocess
import platform
import sys

REQUIRED_PYTHON_VERSION = "3.12.5"

def check_python_version():
    """Checks if the Python version matches the required version."""
    current_version = platform.python_version()
    if current_version != REQUIRED_PYTHON_VERSION:
        print(f"Error: This project requires Python {REQUIRED_PYTHON_VERSION}, but you're using Python {current_version}.\n")
        print("Please install the correct Python version and try again.")
        sys.exit(1)
    else:
        print(f"Python version {current_version} is correct.\n")

def activate_venv():
    """Installs dependencies from requirements.txt within the virtual environment."""
    print("Activating virtual environment and installing dependencies...\n")

    # Determine the correct path to pip based on the operating system
    if platform.system() == "Windows":
        pip_path = os.path.join("venv", "Scripts", "pip.exe")
    else:
        pip_path = os.path.join("venv", "bin", "pip")

    # Ensure the pip executable exists
    if not os.path.isfile(pip_path):
        print(f"Error: pip executable not found at {pip_path}. Ensure the virtual environment is created correctly.\n")
        return

    # Run the command to install requirements
    result = subprocess.run([pip_path, "install", "-r", "requirements.txt"])
    if result.returncode != 0:
        print("Failed to install dependencies.\n")
    else:
        print("\nDependencies installed successfully.\n")

def run_program():
    """Runs the main program using the virtual environment's Python."""
    print("Running main.py...\n")

    # Determine the correct path to the Python executable based on the operating system
    if platform.system() == "Windows":
        python_executable = os.path.join("venv", "Scripts", "python.exe")
    else:
        python_executable = os.path.join("venv", "bin", "python3")

    # Ensure the Python executable exists
    if not os.path.isfile(python_executable):
        print(f"Error: Python executable not found at {python_executable}. Ensure the virtual environment is created correctly.\n")
        return

    print(f"Using Python executable at: {python_executable}\n")

    result = subprocess.run([python_executable, "main.py"])
    if result.returncode != 0:
        print("\nFailed to run the program.")
    else:
        print("\nProgram ran successfully.")

if __name__ == "__main__":
    check_python_version()
    activate_venv()
    run_program()
