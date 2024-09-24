from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
import glob
import os

_ext_src_root = "_ext_src"
_ext_sources = glob.glob("{}/src/*.cpp".format(_ext_src_root)) + glob.glob(
    "{}/src/*.cu".format(_ext_src_root)
)
_ext_headers = glob.glob("{}/include/*".format(_ext_src_root))

setup(
    name='pointnet2',
    ext_modules=[
        CUDAExtension(
            name='pointnet2._ext',
            sources=_ext_sources,
            extra_compile_args={
                "cxx": ["-O2", "-I{}".format(os.path.join(os.path.dirname(os.path.abspath(__file__)), _ext_src_root, "include"))],
                "nvcc": [
                    "-O2", 
                    "-I{}".format(os.path.join(os.path.dirname(os.path.abspath(__file__)), _ext_src_root, "include")),
                    "-I{}".format(os.path.join(os.environ.get('CUDA_HOME', '/usr/local/cuda'), 'include')),
                    "-DTORCH_EXTENSION_NAME=pointnet2._ext",
                    "-D_GLIBCXX_USE_CXX11_ABI=0",
                ],
            },
            include_dirs=[
                os.path.join(os.environ.get('CUDA_HOME', '/usr/local/cuda'), 'include'),
                os.path.join(os.path.dirname(os.path.abspath(__file__)), _ext_src_root, "include")
            ]
        )
    ],
    cmdclass={
        'build_ext': BuildExtension.with_options(use_ninja=False)
    },
    packages=['pointnet2'],
    package_data={'pointnet2': ['*.so']},
)