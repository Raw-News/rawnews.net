from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='rawnews.net',
      version=version,
      description="'A Raw-News branding package on top of the Plumi video sharing add-on suite for Plone.'",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='raw-news, plone, plumi',
      author='Andrea Amantini',
      author_email='andrea.amantini@raw-news.net',
      url='http://raw-news.net',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['rawnews'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plumi.app',
          'plumi.content',
          # -*- Extra requirements: -*-
      ],
      extras_require = {
        'test' : ['plone.app.testing',]
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
