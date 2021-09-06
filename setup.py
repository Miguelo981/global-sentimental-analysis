from setuptools import find_packages, setup


setup(
    name='global-sentimental-analysis',
    packages=find_packages(include=['lib']),
    version='0.1.0',
    description='A Python lib to extract the sentiment analysis from different countries joining several lang libs',
    author='Miguelo981',
    license='MIT',
    install_requires=[
          "textblob",
          "textblob-fr",
          "textblob-de",
          "pysentimiento",
      ],
    package_data={
        'lib':["*"]
    },
    scripts=['install.sh'],
)