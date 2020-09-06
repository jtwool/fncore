import setuptools

with open("README.md", "r") as f
  long_description = f.read()

setuptools.setup(
    name="fncore",
    version="2020.9",
    author="JT Wolohan",
    author_email="jwolohan@gmail.com",
    description="Fuctional programming core library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jtwool/fncore",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
