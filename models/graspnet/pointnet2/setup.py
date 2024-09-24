# pointnet2/setup.py
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
import glob
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
print("ROOT: ", ROOT)

_ext_src_root = "_ext_src"
_ext_sources = glob.glob("{}/src/*.cpp".format(_ext_src_root)) + glob.glob(
    "{}/src/*.cu".format(_ext_src_root)
)
_ext_headers = glob.glob("{}/include/*".format(_ext_src_root))


def get_extensions():
    print("Current working directory:", os.getcwd())
    print("ROOT:", ROOT)
    print("_ext_sources:", _ext_sources)
    print("_ext_headers:", _ext_headers)
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