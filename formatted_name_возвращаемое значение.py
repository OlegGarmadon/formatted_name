"""Возвращаемое значение"""

#Возвращение простого значения
def get_formatted_name(first_name, last_name):
	"""Возвращает акуратно отформатированное полное имя"""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Необязательный аргумент

def get_formatted_name(first_name, middle_name, last_name):
	"""Возвращает акуратно отформатированное полное имя"""
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('jon', 'hooker', 'heer')
print(musician)

