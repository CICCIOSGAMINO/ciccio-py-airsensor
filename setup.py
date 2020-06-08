# setup.py is the build script for setuptools. It tells setuptools about your 
# package (such as the name and version) as well as which code files to include.
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ciccio-py-airsensor", # Replace with your own username
    version="0.1.0",
    author="@cicciosgamino",
    author_email="marco.canali@gmail.com",
    description="Easy python adafruit serial reader for airsensor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CICCIOSGAMINO/py-airsensor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    entry_points = {
      'console_scripts': [
        'airsensor=main_pkg.app:main'
      ]
    }
)