# class used for temperature conversions

class Temperature():

	def __init__(self, baseUnit, baseValue):
		self.baseUnit = baseUnit
		self.baseValue = float(baseValue)

		self.unit_C = "C"
		self.unit_K = "K"
		self.unit_F = "F"

		self.dictUnits = {"C": "Celsius",
							"K": "Kelvin",
							"F": "Fahrenheit"}

		self.dictConverted = {}

		if self.baseUnit in (self.unit_C, self.unit_K):
			self.isBaseUnitMetric = True
		else:
			self.isBaseUnitMetric = False

	def convertBaseUnitToKelvin(self):
		if self.baseUnit == self.unit_C:
			return self.baseValue + 273.15
		elif self.baseUnit == self.unit_K:
			return self.baseValue

	def convertBaseUnitToFahrenheit(self):
		if self.baseUnit == self.unit_F:
			return self.baseValue	

	def convertToNewUnits(self):
		workingValue = 0.0
		if self.isBaseUnitMetric:
			workingValue = self.convertBaseUnitToKelvin()
			# workingValue is now in Kelvin

			# check that value is not less than absolute zero (0 K)
			try:
				assert workingValue >= 0

				# convert to all units
				self.dictConverted[f"{self.dictUnits[self.unit_C]}"] = round(workingValue - 273.15, 2)
				self.dictConverted[f"{self.dictUnits[self.unit_K]}"] = round(workingValue, 2)
				self.dictConverted[f"{self.dictUnits[self.unit_F]}"] = round((workingValue - 273.15) * (9/5) + 32, 2)
				
			except AssertionError:
				print("Entered value is invalid because it is less than absolute zero.")
				pass

		else:
			workingValue = self.convertBaseUnitToFahrenheit()
			# workingValue is now in Fahrenheit

			# check that value is not less than absolute zero (-459.67 F)
			try:
				assert workingValue >= -459.67

				# convert to all units
				self.dictConverted[f"{self.dictUnits[self.unit_C]}"] = round((workingValue - 32) * (5/9), 2)
				self.dictConverted[f"{self.dictUnits[self.unit_K]}"] = round((workingValue - 32) * (5/9) + 273.15, 2)
				self.dictConverted[f"{self.dictUnits[self.unit_F]}"] = round(workingValue, 2)

			except AssertionError:
				print("Entered value is invalid because it is less than absolute zero.")
				pass
