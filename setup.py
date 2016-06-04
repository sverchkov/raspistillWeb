import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'waitress',
    'pyramid_mako', #new dependency
    'exifread', #new dependency,
    'pyramid_tm',#fordb
    'SQLAlchemy',#fordb
    'transaction',#fordb
    'zope.sqlalchemy',#fordb
    'Pillow',
    ]

setup(name='raspistillWeb',
      version='0.2',
      description='raspistillWeb-Phenotiki',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Tim Jungnickel',
      author_email='tim.jungnickel@gmail.com',
      url='',
      keywords='phenotiki plant phenotyping uw web pyramid pylons raspberry pi raspberrypi rpi raspistill',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="raspistillweb",
      entry_points="""\
      [paste.app_factory]
      main = raspistillweb:main
      [console_scripts]
      initialize_raspistillweb_db = raspistillweb.scripts.initializedb:main
      """,
      )
