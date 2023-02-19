from PasswordSymbols import *


# simple builder class for building symbol string according to set functions
class PasswordSymbolsBuilder(object):
	def __init__(self):
		self._symbols = PasswordSymbols()

	# add digits if True
	def set_digits(self, included: bool):
		if included:
			chs = self._symbols.get_symbols()
			self._symbols.set_symbols(chs + '0123456789')
		return self

	# add lowercase if True
	def set_lowercase_letters(self, included: bool):
		if included:
			chs = self._symbols.get_symbols()
			self._symbols.set_symbols(chs + 'abcdefghijklmnopqrstuvwxyz')
		return self

	# add uppercase if True
	def set_uppercase_letters(self, included: bool):
		if included:
			chs = self._symbols.get_symbols()
			self._symbols.set_symbols(chs + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
		return self

	# add other symbols if True
	def set_others(self, included: bool):
		if included:
			chs = self._symbols.get_symbols()
			self._symbols.set_symbols(chs + '!#$%&*+-=?@^_')
		return self

	# function allow to avoid ambiguous symbols
	# avoid if True
	def avoid_ambiguous_characters(self, included: bool):
		if included:
			ambiguous = set('iIlL1oO0')
			symbols_set = set(self._symbols.get_symbols())
			symbols_set -= ambiguous
			new_symbols = ''.join(sorted(symbols_set))
			self._symbols.set_symbols(new_symbols)
		return self

	# return built symbol string if settings are done
	def build(self):
		return self._symbols
