# function converts user answer to bool value
# if answer is not 'y' returns False
def ans_to_bool(ans: str):
	return True if ans == 'y' else False


# function converts user answer to integer value
# if answer is not even digit then it return the lowest allowed value
def ans_to_int(ans: str, lowest: int):
	try:
		integer = int(ans)
		if integer > lowest:
			return integer
	except ValueError:
		return lowest
	return lowest
