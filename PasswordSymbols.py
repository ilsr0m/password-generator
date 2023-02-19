# this class contains symbol string which is used for password generation
class PasswordSymbols(object):
	def __init__(self):
		self._symbols = ''

	def get_symbols(self):
		return self._symbols

	def set_symbols(self, symbols: str):
		self._symbols = symbols
