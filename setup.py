#!/usr/bin/env python3
"""
Setup script for Badge Access Application
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="badge-access-system",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A comprehensive badge access control system with reporting and visualization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/badge-access",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "reportlab>=4.0.0",
        "plotnine>=0.12.0",
        "matplotlib>=3.7.0",
        "python-dateutil>=2.8.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "badge-access=building-access:main",
        ],
    },
)