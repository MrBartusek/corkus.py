from setuptools import setup
import re

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = ''
with open('corkus/version.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

readme = ''
with open('README.md', encoding="utf8") as f:
    readme = f.read()

setup(
    name='corkus.py',
    author='MrBartusek',
    url='https://github.com/MrBartusek/corkus.py',
    project_urls={
        "Documentation": "https://corkuspy.readthedocs.io/en/stable/",
        "Issue tracker": "https://github.com/MrBartusek/corkus.py/issues"
    },
    package_data={"corkus": ["py.typed"]},
    packages=[
        "corkus",
        "corkus.objects",
        "corkus.endpoints",
        "corkus.utils",
        "corkus.data"
    ],
    version=version,
    license='MIT',
    description='Asynchronous, feature-rich and easy to use Python wrapper for Public Wynncraft API',
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=requirements,
    python_requires='>=3.8.0',
    classifiers=[
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: MIT License',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Topic :: Internet',
    'Topic :: Games/Entertainment',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities',
    ]
)
