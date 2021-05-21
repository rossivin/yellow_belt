from brand import Brand
from filter_vessel import FilterVessel
from filter_interface import FilterInterface

"""INPUTS"""
#brand1
brand1_name = "Budweiser"
brand1_cost = 22.50
brand1_abv = 5.0
#brand2
brand2_name = "Bud Light"
brand2_cost = 30.00
brand2_abv = 6.0
#filter
filter_volume = 40.0
pre_filter_volume = 10.0
post_filter_volume = 20.0
alcoholyzer_location = 15.0
#parameters
switch_volume = 35
volume_intervals = 1

"""INITIALIZING"""
brand1 = Brand(brand1_name, brand1_cost, brand1_abv)
brand2 = Brand(brand2_name, brand2_cost, brand2_abv)
vessel = FilterVessel(filter_volume, pre_filter_volume, post_filter_volume)

def simulate_instant(switch_volume, vessel, brand1, brand2):
	interface_sim = FilterInterface(vessel, brand1, brand2)
	print("Filter Size: %.2f hL" % filter_volume)
	print("Pre-Filter Volume: %.2f hL" % pre_filter_volume)
	print("Post-Filter Volume: %.2f hL" % post_filter_volume)

	print("\nTotal Volume of Brand 1 ({}) in Brand 2 ({}): {:.2f} hL".format(brand1.name, brand2.name, interface_sim.brandVolumeLeft(1, switch_volume)))
	print("Total Volume of Brand 2 ({}) in Brand 1 ({}): {:.2f} hL".format(brand2.name, brand1.name, interface_sim.totalBrandVolumeOut(2, switch_volume)))
	print("Financial Impact of Switch: CAD {:.2f}".format(interface_sim.financialImpactOfSwitch(switch_volume)))

simulate_instant(switch_volume, vessel, brand1, brand2)








