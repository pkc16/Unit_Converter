# class used for volume conversions

class Volume():

	def __init__(self, baseUnit, baseValue):
		self.baseUnit = baseUnit.lower()
		self.baseValue = float(baseValue)

		self.unit_CM3 = "cm3"
		self.unit_M3 = "m3"
		self.unit_ML = "ml"
		self.unit_L = "l"
		self.unit_CUP = "cup"
		self.unit_PINT = "pint"
		self.unit_QUART = "quart"
		self.unit_GALLON = "gallon"

		self.dictConverted = {}

		if self.baseUnit in (self.unit_CM3, self.unit_M3, self.unit_ML, self.unit_L):
			self.isBaseUnitMetric = True
		else:
			self.isBaseUnitMetric = False

	def convertBaseUnitToLiters(self):
		if self.baseUnit == self.unit_CM3:
			return self.baseValue / 1000
		elif self.baseUnit == self.unit_M3:
			return self.baseValue * 1000
		elif self.baseUnit == self.unit_ML:
			return self.baseValue / 1000
		elif self.baseUnit == self.unit_L:
			return self.baseValue

	def convertBaseUnitToGallons(self):
		if self.baseUnit == self.unit_CUP:
			return self.baseValue / 16
		elif self.baseUnit == self.unit_PINT:
			return self.baseValue / 8
		elif self.baseUnit == self.unit_QUART:
			return self.baseValue / 4
		elif self.baseUnit == self.unit_GALLON:
			return self.baseValue	

	def convertToNewUnits(self):
		workingValue = 0.0
		if self.isBaseUnitMetric:
			workingValue = self.convertBaseUnitToLiters()
			# workingValue is now in liters

			# check that value is not negative
			try:
				assert workingValue >= 0

				# convert to all units
				self.dictConverted[f"{self.unit_CM3}"] = round(workingValue * 1000, 2)
				self.dictConverted[f"{self.unit_M3}"] = round(workingValue / 1000, 2)
				self.dictConverted[f"{self.unit_ML}"] = round(workingValue * 1000, 2)
				self.dictConverted[f"{self.unit_L}"] = round(workingValue, 2)
				self.dictConverted[f"{self.unit_CUP}"] = round(workingValue * (1 / 3.78541) * 16, 2)
				self.dictConverted[f"{self.unit_PINT}"] = round(workingValue * (1 / 3.78541) * 8, 2)
				self.dictConverted[f"{self.unit_QUART}"] = round(workingValue * (1 / 3.78541) * 4, 2)
				self.dictConverted[f"{self.unit_GALLON}"] = round(workingValue / 3.78541, 2)

			except AssertionError:
				print("Entered value is invalid because it is negative.")
				pass

		else:
			workingValue = self.convertBaseUnitToGallons()
			# workingValue is now in gallons

			# check that value is not negative
			try:
				assert workingValue >= 0

				# convert to all units
				self.dictConverted[f"{self.unit_CM3}"] = round(workingValue * 3.78541 * 1000, 2)
				self.dictConverted[f"{self.unit_M3}"] = round(workingValue * 3.78541 / 1000, 2)
				self.dictConverted[f"{self.unit_ML}"] = round(workingValue * 3.78541 * 1000, 2)
				self.dictConverted[f"{self.unit_L}"] = round(workingValue * 3.78541, 2)
				self.dictConverted[f"{self.unit_CUP}"] = round(workingValue * 16, 2)
				self.dictConverted[f"{self.unit_PINT}"] = round(workingValue * 8, 2)
				self.dictConverted[f"{self.unit_QUART}"] = round(workingValue * 4, 2)
				self.dictConverted[f"{self.unit_GALLON}"] = round(workingValue, 2)

			except AssertionError:
				print("Entered value is invalid because it is negative.")
				pass