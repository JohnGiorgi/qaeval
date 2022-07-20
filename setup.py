import setuptools

# version.py defines the VERSION variable.
# We use exec here so we don't import qaeval whilst setting up.
VERSION = {}
with open('qaeval/version.py', 'r') as version_file:
    exec(version_file.read(), VERSION)

setuptools.setup(
    name='qaeval',
    version=VERSION['VERSION'],
    author='Daniel Deutsch',
    description='A package for evaluating the content of summaries through question-answering',
    url='https://github.com/danieldeutsch/qaeval',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'allennlp>=2.9.0',
        'click>=7.1.2',
        'edlib>=1.2.7',
        'spacy>=2.2.4',
        'torch>=1.6.0',
        'transformers>=4.1',
        'urllib3>=1.25.10'
    ]
)