# pointnet2/setup.py
import os
import glob
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

ROOT = os.path.dirname(os.path.abspath(__file__))
print("ROOT:", ROOT)

_ext_sources = glob.glob("*.cpp") + glob.glob("*.cu")
_ext_headers = glob.glob("*.h")

print("_ext_sources:", _ext_sources)
print("_ext_headers:", _ext_headers)

def get_extensions():
    ext_modules = [
        CUDAExtension(
            name='_ext',
            sources=_ext_sources,
            extra_compile_args={
                "cxx": ["-O2", "-I{}".format(ROOT)],
                "nvcc": ["-O2", "-I{}".format(ROOT)],
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