import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bike-demand-modelling-renan-cunha", # Replace with your own username
    version="0.0.1",
    author="Renan Cunha",
    author_email="renancunhafonseca@gmail.com",
    description="Bike Share Demand Modelling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/renan-cunha/bike_usage_modelling",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
