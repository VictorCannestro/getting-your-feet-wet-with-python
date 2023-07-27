# https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder

from setuptools import setup, find_packages


setup(
      name='tictactoe', 
      version='0.1', 
      packages=find_packages()
)