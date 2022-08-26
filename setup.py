from setuptools import setup

_version = '2.0.0'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="lunarcrush",
    version=_version,
    author="saizk",
    author_email="sergioaizcorbe@hotmail.com",
    description="Unofficial LunarCrush API v2 Wrapper for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saizk/LunarCrushAPI",
    project_urls={
        "Bug Tracker": "https://github.com/saizk/LunarCrushAPI/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={".": ""},
    packages=["lunarcrush"],
    install_requires=['requests'],
    include_package_data=True,
    python_requires=">=3.6",
)
