import math

class FilterInterface():

	def __init__(self, vessel, brand1, brand2):
		self.vessel = vessel
		self.brand1 = brand1
		self.brand2 = brand2
				
	def totalBrandVolumeOut(self, brand_num, volume):
		"""Returns the total volume of 'brand_num' out after 'volume' of brand2 is pushed through it"""
		if volume <= self.vessel.pre_line_volume + self.vessel.post_line_volume:
			if brand_num == 1:
				return volume
			else:
				return 0
		else:
			brand1_total_volume_out = self.vessel.pre_line_volume + self.vessel.post_line_volume
			interface_volume = volume - self.vessel.pre_line_volume - self.vessel.post_line_volume
			brand1_total_volume_out += -self.vessel.volume * math.exp(-interface_volume/self.vessel.volume) + self.vessel.volume
			if brand_num == 1:
				return brand1_total_volume_out
			else:
				return volume - brand1_total_volume_out

	def outletComposition(self, brand_num, volume):
		"""Returns the composition of 'brand_num' in the filter outlet after 'volume' of brand 2 is pushed through it"""
		if volume <= self.vessel.pre_line_volume + self.vessel.post_line_volume:
			if brand_num == 1:
				return 1
			else:
				return 0
		else:
			interface_volume = volume - self.vessel.pre_line_volume - self.vessel.post_line_volume
			brand1_composition_out = math.exp(-interface_volume/self.vessel.volume)
			if brand_num == 1:
				return brand1_composition_out
			else:
				return 1 - brand1_composition_out

	def brandVolumeLeft(self, brand_num, volume):

		initial_volume = self.vessel.volume + self.vessel.pre_line_volume + self.vessel.post_line_volume
		brand1_left_over_volume = initial_volume - self.totalBrandVolumeOut(1, volume)

		if brand_num == 1:
			return brand1_left_over_volume
		else:
			return initial_volume - brand1_left_over_volume

	def financialImpactOfSwitch(self, volume):

		brand1_volume_left = self.brandVolumeLeft(1,volume)
		brand2_volume_out = self.totalBrandVolumeOut(2,volume)

		part1 = brand2_volume_out * (self.brand2.cost - self.brand1.cost*(self.brand2.alcohol/self.brand1.alcohol))
		part2 = brand1_volume_left * (self.brand1.cost - self.brand2.cost*(self.brand1.alcohol/self.brand2.alcohol))
		return part1 + part2

	def alcoholyzerValue(self, volume, alcoholyzer_location):
		"""Alcoholyzer location needs to be in hLs"""
		if volume <= alcoholyzer_location:
			return self.brand1.alcohol
		else:
			interface_volume = volume - alcoholyzer_location
			brand1_composition_out = math.exp(-interface_volume/self.vessel.volume)
			return self.brand1.alcohol * brand1_composition_out + self.brand2.alcohol * (1 - brand1_composition_out)
