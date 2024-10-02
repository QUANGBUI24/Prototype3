from cx_Freeze import setup, Executable

setup(
    name="TEST",
    version="1.0",
    description="Python UML Program",
    executables=[Executable("main.py")]
)
