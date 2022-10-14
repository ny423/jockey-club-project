"""
Used for running **.tag file instead of typing commands everytime
"""
import os

current_dir = os.getcwd()

filename = "sample.tag"

os.chdir(r"C:/tagui/src/")
os.system(rf"tagui {current_dir}{filename}")
