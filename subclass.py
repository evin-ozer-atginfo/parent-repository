#+ Framework libraries.
import os
import sys
__real_path = os.path.split(os.path.realpath(__file__))[0]
lib_paths = [
    os.path.abspath(os.path.join(__real_path, './base-repository'))
]
sys.path += lib_paths

from base import Base

class Subclass(Base):
	def __init__(self, name):
		super().__init__()
		self.name = name + 'Meow'

if __name__ == '__main__':
	s = Subclass('Me')
	print(s.name)
	print(s.text)
