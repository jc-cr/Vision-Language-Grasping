import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(current_dir, 'build', 'lib.linux-x86_64-cpython-38', 'pointnet2')
if build_dir not in sys.path:
    sys.path.append(build_dir)

# Remove the import of _ext from here