import os
import glob
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

ROOT = os.path.dirname(os.path.abspath(__file__))
print("ROOT:", ROOT)

_ext_src_root = "_ext_src"
_ext_sources = glob.glob(os.path.join(ROOT, _ext_src_root, "src", "*.cpp")) + \
               glob.glob(os.path.join(ROOT, _ext_src_root, "src", "*.cu"))
_ext_headers = glob.glob(os.path.join(ROOT, _ext_src_root, "include", "*.h"))

print("_ext_sources:", _ext_sources)
print("_ext_headers:", _ext_headers)

def get_extensions():
    ext_modules = [
        CUDAExtension(
            name='pointnet2._ext',
            sources=_ext_sources,
            extra_compile_args={
                "cxx": ["-O2", "-I{}".format(os.path.join(ROOT, _ext_src_root, "include"))],
                "nvcc": ["-O2", "-I{}".format(os.path.join(ROOT, _ext_src_root, "include"))],
            },
        )
    ]
    return ext_modules

setup(
    name='pointnet2',
    ext_modules=get_extensions(),
    cmdclass={
        'build_ext': BuildExtension.with_options(no_python_abi_suffix=True)
    }
)