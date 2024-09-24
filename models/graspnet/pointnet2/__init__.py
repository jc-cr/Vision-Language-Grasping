import os
import sys

print(f"Current working directory: {os.getcwd()}")
print(f"Contents of current directory: {os.listdir()}")
print(f"Contents of parent directory: {os.listdir('..')}")

# Add the current directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    print(f"Attempting to import _ext from {os.path.abspath('.')}")
    from . import _ext
    print("Successfully imported _ext")
except ImportError as e:
    print(f"Failed to import _ext module: {e}")
    print(f"sys.path: {sys.path}")
    raise