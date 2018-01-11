import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = "C:\\Users\\Lisek\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Lisek\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6"

executables = [cx_Freeze.Executable("prs.py")]

cx_Freeze.setup(
	name = "PRS v0.0",

	executables = executables
)
