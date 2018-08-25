from cx_Freeze import setup, Executable

setup(

    name = "relatorio",
    version ="1.0.0",
    description = "py to exe",
    executables = [Executable("main.py")]

)