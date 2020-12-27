import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="midi-wrapper-SnooperXP",
    version="0.0.5",
    author="Snooper Xp",
    author_email="snooperxp@gmail.com",
    description="A package that wraps Pygame midi for simplified use",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SnooperXP/neos-vr-midi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)