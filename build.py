import os
import subprocess
import platform

def create_venv():
    """Creates the virtual environment using python3."""
    print("Creating virtual environment...")
    if platform.system() == "Windows":
        subprocess.run(["python", "-m", "venv", "venv"])
    else:
        subprocess.run(["python3", "-m", "venv", "venv"])

def activate_venv():
    """Installs dependencies from requirements.txt within the virtual environment."""
    print("Activating virtual environment and installing dependencies...")

    # Determine the correct path to pip based on the operating system
    if platform.system() == "Windows":
        pip_path = os.path.join("venv", "Scripts", "pip.exe")
    else:
        pip_path = os.path.join("venv", "bin", "pip")

    # Ensure the pip executable exists
    if not os.path.isfile(pip_path):
        print(f"Error: pip executable not found at {pip_path}. Ensure the virtual environment is created correctly.")
        return

    # Run the command to install requirements
    result = subprocess.run([pip_path, "install", "-r", "requirements.txt"])
    if result.returncode != 0:
        print("Failed to install dependencies.")
    else:
        print("Dependencies installed successfully.")

def run_program():
    """Runs the main program using the virtual environment's Python."""
    print("Running main.py...")

    # Determine the correct path to the Python executable based on the operating system
    if platform.system() == "Windows":
        python_executable = os.path.join("venv", "Scripts", "python.exe")
    else:
        python_executable = os.path.join("venv", "bin", "python3")

    # Ensure the Python executable exists
    if not os.path.isfile(python_executable):
        print(f"Error: Python executable not found at {python_executable}. Ensure the virtual environment is created correctly.")
        return

    result = subprocess.run([python_executable, "main.py"])
    if result.returncode != 0:
        print("Failed to run the program.")
    else:
        print("Program ran successfully.")

if __name__ == "__main__":
    # Uncomment this if you need to create the virtual environment initially
    # create_venv()
    activate_venv()
    run_program()
