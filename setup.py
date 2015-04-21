from setuptools import setup

setup(name='FotoApp',
      version='1.0',
      description='FotoApp',
      author='Ramo',
      author_email='example@example.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['Django',
                        'psycopg2',
                        'django-debug-toolbar',
						'Pillow'
                        ],
     )
