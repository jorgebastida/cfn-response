import sys

from setuptools import setup, find_packages

tests_require = []

# as of Python >= 3.3 unittest.mock module is maintained within Python.
if sys.version_info < (3, 3):
    tests_require.append('mock>=1.0.0')

setup(
    name='cfn-response',
    version='0.0.3',
    url='http://github.com/jorgebastida/cfn-response',
    license='BSD',
    author='Jorge Bastida',
    author_email='me@jorgebastida.com',
    description="""cfn-response is a micro package which exposes some
    helpers to talk with CloudFormation from within python Lambda functions.
    This package is intentionally small in order to be embedded lambda functions.
    If you are looking to create aws-lambda backed Custom CloudFormation
    resources using python, you are going to need this.""",
    keywords="aws lambda cloudformation custom resources",
    py_modules=["cfnresponse"],
    platforms='any',
    install_requires=[],
    test_suite='tests',
    tests_require=tests_require,
    classifiers=[
        'Programming Language :: Python :: 2',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Utilities'
    ],
    zip_safe=False
)
