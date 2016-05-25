from setuptools import setup

setup(
    name='cfn-response',
    version='0.0.4',
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
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Utilities'
    ],
    zip_safe=False
)
