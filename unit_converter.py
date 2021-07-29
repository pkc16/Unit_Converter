# Unit Conversion program

import length, mass, temperature, volume
import re

# This function prompts for the unit type
def getUnit(conversionType, unitType):
	unit = ""
	if conversionType.upper() == "L":
		unit = input(f"\nEnter the {unitType}: cm, m, km, in, ft, yd, mi : ")
		while unit.upper() not in ("CM","M","KM","IN","FT","YD","MI"):
			unit = input(f"Enter the {unitType}: cm, m, km, in, ft, yd, mi : ")

	elif conversionType.upper() == "M":
		unit = input(f"\nEnter the {unitType}: g, kg, oz, lb, ton : ")
		while unit.upper() not in ("G","KG","OZ","LB","TON"):
			unit = input(f"Enter the {unitType}: g, kg, oz, lb, ton : ")

	elif conversionType.upper() == "T":
		unit = input(f"\nEnter the {unitType}: (C)elsius, (F)ahrenheit, (K)elvin : ")
		while unit.upper() not in ("C","F","K"):
			unit = input(f"Enter the {unitType}: (C)elsius, (F)ahrenheit, (K)elvin : ")

	elif conversionType.upper() == "V":
		unit = input(f"\nEnter the {unitType}: cm3, m3, ml, l, cup, pint, quart, gallon : ")
		while unit.upper() not in ("CM3","M3","ML","L","CUP","PINT","QUART", "GALLON"):
			unit = input(f"Enter the {unitType}: cm3, m3, ml, l, cup, pint, quart, gallon : ")

	return unit

def isValidValue(conversionType, value):
	# This method checks if value is appropriate
	try:
		# if value can be converted to float, then it is a numeric
		x = float(value)
		if x < 0 and conversionType.upper() in ("L","M","V"):
			raise ValueError
		else:
			return True

	except ValueError:
		print("Value is invalid")
		return False


# Begin execution
# Prompt for the conversion type
conversionType = True
while conversionType:
	conversionType = input("Enter type for conversion: (l)ength, (m)ass, (t)emperature, (v)olume : ")
	while conversionType.upper() not in ("L","M","T","V"):
		conversionType = input("Enter type for conversion: (l)ength, (m)ass, (t)emperature, (v)olume : ")

	baseUnit = getUnit(conversionType, "base unit")

	# Now prompt for the value to be converted
	value = input(f"\nEnter the value in {baseUnit}: ")
	while not isValidValue(conversionType, value):
		value = input(f"\nEnter the value in {baseUnit}: ")

	# Now do the conversion
	if conversionType.upper() == "L":
		len_conv = length.Length(baseUnit, value)
		len_conv.convertToNewUnits()
		if len(len_conv.dictConverted) > 0:
			print("\nConverted values:\n")
			for key, val in len_conv.dictConverted.items():
				print(key + ": " + str(val))
		
	elif conversionType.upper() == "M":
		mass_conv = mass.Mass(baseUnit, value)
		mass_conv.convertToNewUnits()
		if len(mass_conv.dictConverted) > 0:
			print("\nConverted values:\n")
			for key, val in mass_conv.dictConverted.items():
				print(key + ": " + str(val))

	elif conversionType.upper() == "T":
		temp_conv = temperature.Temperature(baseUnit.upper(), value)
		temp_conv.convertToNewUnits()
		if len(temp_conv.dictConverted) > 0:
			print("\nConverted values:\n")
			for key, val in temp_conv.dictConverted.items():
				print(key + ": " + str(val))

	elif conversionType.upper() == "V":
		vol_conv = volume.Volume(baseUnit, value)
		vol_conv.convertToNewUnits()
		if len(vol_conv.dictConverted) > 0:
			print("\nConverted values:\n")
			for key, val in vol_conv.dictConverted.items():
				print(key + ": " + str(val))

	runAgain = input("\nDo you want to do another conversion? (press Enter to continue, or 'q' to quit) ")
	if runAgain.upper() == "Q":
		break

