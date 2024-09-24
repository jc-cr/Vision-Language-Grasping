import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(current_dir, 'build', 'lib.linux-x86_64-cpython-38', 'pointnet2')
if build_dir not in sys.path:
    sys.path.append(build_dir)

try:
    from pointnet2 import _ext
except ImportError:
    print(f"Error importing _ext in __init__.py")
    print(f"Current directory: {current_dir}")
    print(f"Build directory: {build_dir}")
    print(f"Build directory contents: {os.listdir(build_dir) if os.path.exists(build_dir) else 'Directory does not exist'}")
    print(f"sys.path: {sys.path}")
    raise