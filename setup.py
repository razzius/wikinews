import setuptools

setuptools.setup(
    name='wikinews',
    version='0.0.3',
    url='https://github.com/razzius/wikinews',
    entry_points={
        'console_scripts': [
            'wikinews = wikinews:main'
        ]
    }
)
