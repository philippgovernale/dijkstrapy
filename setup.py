from setuptools import setup

setup(
    name='dijkstrapy',
    version='0.1.3',
    description='A CLI rpn calculator',
    long_description='A command-line calculator using reverse polish notation that is fully written in Python',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2 :: Only',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    ],
    keywords='rpn calculator cli',
    url='https://github.com/philippgovernale/dijkstrapy',
    author='Philipp Governale',
    author_email='philipp.governale1@gmail.com',
    license='GPLv3+',
    py_modules = ['dijkstrapy', 'getchar','handler','mathfuncs', 'screen', 'stackop', 'sysfuncs', 'var', 'win10col'],
    entry_points='''
        [console_scripts]
        dijkstrapy=dijkstrapy
    ''',
)
