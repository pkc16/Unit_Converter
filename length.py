# class used for length conversions

class Length():

	def __init__(self, baseUnit, baseValue):
		self.baseUnit = baseUnit.lower()
		self.baseValue = float(baseValue)

		self.unit_CM = "cm"
		self.unit_M = "m"
		self.unit_KM = "km"
		self.unit_INCH = "in"
		self.unit_FOOT = "ft"
		self.unit_YARD = "yd"
		self.unit_MILE = "mi"

		self.dictConverted = {}

		if self.baseUnit in (self.unit_CM, self.unit_M, self.unit_KM):
			self.isBaseUnitMetric = True
		else:
			self.isBaseUnitMetric = False

	def convertBaseUnitToMeters(self):
		if self.baseUnit == self.unit_CM:
			return self.baseValue / 100
		elif self.baseUnit == self.unit_M:
			return self.baseValue
		elif self.baseUnit == self.unit_KM:
			return self.baseValue * 1000

	def convertBaseUnitToFeet(self):
		if self.baseUnit == self.unit_INCH:
			return self.baseValue / 12
		elif self.baseUnit == self.unit_FOOT:
			return self.baseValue
		elif self.baseUnit == self.unit_YARD:
			return self.baseValue * 3
		elif self.baseUnit == self.unit_MILE:
			return self.baseValue * 5280	

	def convertToNewUnits(self):
		workingValue = 0.0
		if self.isBaseUnitMetric:
			workingValue = self.convertBaseUnitToMeters()
			# workingValue is now in meters

			# check that value is not negative
			try:
				assert workingValue >= 0

				# convert to all units
				self.dictConverted[f"{self.unit_CM}"] = round(workingValue * 100, 2)
				self.dictConverted[f"{self.unit_M}"] = round(workingValue, 2)
				self.dictConverted[f"{self.unit_KM}"] = round(workingValue / 1000, 2)
				self.dictConverted[f"{self.unit_INCH}"] = round(workingValue * 100 / 2.54, 2)
				self.dictConverted[f"{self.unit_FOOT}"] = round(workingValue * 100 * (1 / 2.54) * (1 / 12), 2)
				self.dictConverted[f"{self.unit_YARD}"] = round(workingValue * 100 * (1 / 2.54) * (1 / 12) * (1 / 3), 2)
				self.dictConverted[f"{self.unit_MILE}"] = round(workingValue * 100 * (1 / 2.54) * (1 / 12) * (1 / 5280), 2)

			except AssertionError:
				print("Entered value is invalid because it is negative.")
				pass

		else:
			workingValue = self.convertBaseUnitToFeet()
			# workingValue is now in feet

			# check that value is not negative
			try:
				assert workingValue >= 0

				# convert to all units
				self.dictConverted[f"{self.unit_CM}"] = round(workingValue * 12 * 2.54, 2)
				self.dictConverted[f"{self.unit_M}"] = round(workingValue * 12 * 2.54 / 100, 2)
				self.dictConverted[f"{self.unit_KM}"] = round(workingValue * 12 * 2.54 * (1 / 100) * (1 / 1000), 2)
				self.dictConverted[f"{self.unit_INCH}"] = round(workingValue * 12, 2)
				self.dictConverted[f"{self.unit_FOOT}"] = round(workingValue, 2)
				self.dictConverted[f"{self.unit_YARD}"] = round(workingValue / 3, 2)
				self.dictConverted[f"{self.unit_MILE}"] = round(workingValue / 5280, 2)

			except AssertionError:
				print("Entered value is invalid because it is negative.")
				pass