from setuptools import find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def setup_package():
    metadata = dict(
        name="sorcerer",
        version="0.12",
        packages=find_packages(),
        install_requires=["Click>=7.0"],
        author="Liam Scalzulli",
        author_email="liamscalzulli@gmail.com",
        description="Programming problem solution README table generator",
        long_description=long_description,
        long_description_content_type='text/markdown',
        keywords="programming competitive tables markdown readmes",
        url="https://github.com/terror/sorcerer",
        project_urls={
            "Source Code": "https://github.com/terror/sorcerer",
        },
        classifiers=[
            "Development Status :: 3 - Alpha",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3 :: Only",
        ],
        entry_points={"console_scripts": ["sorcerer = sorcerer.cli:cli"]},
        python_requires=">=3.7",
    )

    try:
        from setuptools import setup
    except ImportError:
        from distutils.core import setup
    setup(**metadata)


if __name__ == "__main__":
    setup_package()
