
import setuptools


setuptools.setup(
    name='django-unixdatetimefield',
    version='1.0.1',
    author='Niklas Andersson',
    author_email='nandersson900@gmail.com',
    description='UnixDateTimeField in Django',
    url='https://github.com/Niklas9/django-unixdatetimefield',
    zip_safe=False,
    install_requires=[
        'django',
    ],
    tests_require=[
        'psycopg2',
        'django-nose',
    ],
    packages=setuptools.find_packages(),
    #test_suite='runtests.runtests',
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
