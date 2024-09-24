import os
import sys

print(f"Current working directory: {os.getcwd()}")
print(f"Contents of current directory: {os.listdir()}")
print(f"Contents of parent directory: {os.listdir('..')}")

# Add the current directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

print(f"Pointnet2 directory contents: {os.listdir(current_dir)}")
