from base import Base

def Subclass(Base):
	def __init__(self, name):
		super().__init__()
		self.name = name

if __name__ == '__main__':
	s = Subclass('Me')
	print(s.name)
	print(s.text)
