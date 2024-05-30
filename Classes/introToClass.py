class Cookie:
    # The constructor method for the class
	def __init__(self, color): # It initializes an instance of the class with a specific color, hence the init...
     #if it has self in the parameters, it is a part of a method that is inside of a class
		self.color =  color
	
	def get_color(self):
		return self.color
	
	def set_color(self, color):
		self.color = color
		
		
cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print('Cookie One is:', cookie_one.get_color())
print('Cookie Two is:', cookie_two.get_color())

cookie_one.set_color('yellow')

print('Cookie One is now:', cookie_one.get_color())
print('Cookie Two is still:', cookie_two.get_color())