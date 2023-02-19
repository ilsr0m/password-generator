from PasswordSymbolsBuilder import *
from PasswordGenerator import *
from AnsToModule import *


def main():
	# ask user to give settings how password/passwords should look:
	# amount and length of passwords, digits, lowercase, uppercase,
	# some other symbol kit, ambiguous symbols
	pwd_amount = ans_to_int(input('How many passwords you wish? (from 1): '), 1)
	pwd_length = ans_to_int(input('How long your password must be? (from 8): '), 8)
	include_digits = ans_to_bool(input('Include digits? (y/n): '))
	include_lowercase = ans_to_bool(input('Include lowercase letters? (y/n): '))
	include_uppercase = ans_to_bool(input('Include uppercase letters? (y/n): '))
	include_others = ans_to_bool(input('Include symbols "!#$%&*+-=?@^_"? (y/n): '))
	avoid_ambiguous = ans_to_bool(input('Avoid ambiguous symbols? (y/n): '))

	# build symbol string according to settings by user
	symbols = PasswordSymbolsBuilder(). \
		set_digits(include_digits). \
		set_uppercase_letters(include_uppercase). \
		set_lowercase_letters(include_lowercase). \
		set_others(include_others). \
		avoid_ambiguous_characters(avoid_ambiguous). \
		build().get_symbols()

	# generate password series
	password = PasswordGenerator().generate(symbols, int(pwd_length), int(pwd_amount))

	# in case symbol string has at least one character
	if password is not None:
		print("\n\nGenerated passwords: \n")
		print(*password, sep='\n')


if __name__ == "__main__":
	main()
