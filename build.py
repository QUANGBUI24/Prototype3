import os
import subprocess
import platform

def activate_venv():
    """Activates the virtual environment and installs dependencies."""
    print("Activating virtual environment and installing dependencies...")

    # Check the operating system and set the activation and install command accordingly
    if platform.system() == "Windows":
        # For Windows systems
        install_command = r"venv\Scripts\pip install -r requirements.txt"
    else:
        # For Unix-based systems (Linux and macOS)
        install_command = "./venv/bin/pip install -r requirements.txt"

    # Run the command to install requirements
    result = subprocess.run(install_command, shell=True)
    if result.returncode != 0:
        print("Failed to install dependencies.")
    else:
        print("Dependencies installed successfully.")

def run_program():
    """Runs the main program using the virtual environment's Python."""
    print("Running main.py...")

    # Use the virtual environment's Python to run the main script
    if platform.system() == "Windows":
        python_executable = r"venv\Scripts\python.exe"
    else:
        python_executable = "./venv/bin/python"

    result = subprocess.run([python_executable, "main.py"], shell=True)
    if result.returncode != 0:
        print("Failed to run the program.")
    else:
        print("Program ran successfully.")

if __name__ == "__main__":
    activate_venv()
    run_program()
