from setuptools import setup

setup(name='aperture',
      version='0.1.1',
      description='Wrappers, settings, and extensions for Python/matplotlib',
      url='https://github.com/kevinsprong/aperture',
      author='Kevin Sprong',
      author_email='kevin@kevinsprong.com',
      license='MIT',
      packages=['aperture'],
      install_requires=[
          'matplotlib',
      ],
      zip_safe=False)
