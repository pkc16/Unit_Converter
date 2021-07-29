# class used for mass conversions

class Mass():

	def __init__(self, baseUnit, baseValue):
		self.baseUnit = baseUnit.lower()
		self.baseValue = float(baseValue)

		self.unit_G = "g"
		self.unit_KG = "kg"
		self.unit_OZ = "oz"
		self.unit_LB = "lb"
		self.unit_TON = "ton"

		self.dictConverted = {}

		if self.baseUnit in (self.unit_G, self.unit_KG):
			self.isBaseUnitMetric = True
		else:
			self.isBaseUnitMetric = False

	def convertBaseUnitToKilograms(self):
		if self.baseUnit == self.unit_G:
			return self.baseValue / 1000
		elif self.baseUnit == self.unit_KG:
			return self.baseValue

	def convertBaseUnitToPounds(self):
		if self.baseUnit == self.unit_OZ:
			return self.baseValue / 16
		elif self.baseUnit == self.unit_LB:
			return self.baseValue
		elif self.baseUnit == self.unit_TON:
			return self.baseValue * 2000	

	def convertToNewUnits(self):
		workingValue = 0.0
	
		if self.isBaseUnitMetric:
			workingValue = self.convertBaseUnitToKilograms()
			# workingValue is now in kilograms

			# check that value is not negative
			try:
				assert workingValue >= 0

				# convert to all units
				self.dictConverted[f"{self.unit_G}"] = round(workingValue * 1000, 2)
				self.dictConverted[f"{self.unit_KG}"] = round(workingValue, 2)
				self.dictConverted[f"{self.unit_OZ}"] = round(workingValue * 35.274, 2)
				self.dictConverted[f"{self.unit_LB}"] = round(workingValue * 2.20462, 2)
				self.dictConverted[f"{self.unit_TON}"] = round(workingValue * 2.20462 / 2000, 2)

			except AssertionError:
				print("Entered value is invalid because it is negative.")
				pass
			
		else:
			workingValue = self.convertBaseUnitToPounds()
			# workingValue is now in pounds

			# check that value is not negative
			try:
				assert workingValue >= 0

				# convert to all units
				self.dictConverted[f"{self.unit_G}"] = round(workingValue * ( 1 / 2.20462) * 1000, 2)
				self.dictConverted[f"{self.unit_KG}"] = round(workingValue / 2.20462, 2)
				self.dictConverted[f"{self.unit_OZ}"] = round(workingValue * 16, 2)
				self.dictConverted[f"{self.unit_LB}"] = round(workingValue, 2)
				self.dictConverted[f"{self.unit_TON}"] = round(workingValue / 2000, 2)

			except AssertionError:
				print("Entered value is invalid because it is negative.")
				pass