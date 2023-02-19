from random import randrange


# obviously this class allows to generate passwords
# just use static method 'generate' to use it
class PasswordGenerator(object):
	@staticmethod
	def generate(permissible_symbols: str, length: int, password_amount: int):
		pwd_list = []  # list of passwords
		if permissible_symbols == '':  # symbol string is empty
			return None
		# main computations
		for _ in range(password_amount):
			pwd = ''  # password variable
			for _ in range(length):
				# push random symbol from symbol string
				rand = randrange(0, len(permissible_symbols))
				pwd += permissible_symbols[rand]
			pwd_list.append(pwd)
		return pwd_list
