# Copyright 2021 Declarative Systems Pty Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools
import pipelines_example_pythonenv.version

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pipelines_example_pythonenv",
    version=pipelines_example_pythonenv.version.get_version(),
    author="Geoff Williams",
    author_email="geoff@declarativesystems.com",
    description="example pip packaging",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/declarativesystems/pipelines_example_pythonenv",
    packages=setuptools.find_packages(),
    # pick from https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": (['pipelines_example_pythonenv=pipelines_example_pythonenv:main'],)
    },
    include_package_data=True,
    install_requires=[
    ]
)
