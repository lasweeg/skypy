import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="skypy",
    url="https://github.com/FuchsCrafter/skypy",
    version="0.0.1",
    author="FuchsCrafter",
    license="CC0",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: CC0 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=["requests"]
)
