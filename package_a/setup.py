#!/usr/bin/env python

from setuptools import find_namespace_packages, setup

setup(
    name="a",
    description="Terraform Automation CLI for IndigoAg",
    version="0.1.1",
    packages=find_namespace_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "boto3>=1.18.7,<2.0.0",
        "click"
    ],
    extras_require={"dev": ['moto']},
    entry_points="""
        [console_scripts]
        pkg_a=a.main:main
        """,
)
