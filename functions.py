from brand import Brand
from filter_interface import FilterInterface
#GET EXCEL DATA

def getFilterNum(sheet, r):

	return sheet.cell(row = r, column = 2).value

def getBrand1(sheet, r):

	return sheet.cell(row = r, column = 3).value

def getBrand2(sheet, r):

	return sheet.cell(row = r, column = 4).value

def getWashIn(sheet, r):

	return sheet.cell(row = r, column = 6).value

#GET INFORMATINO BASED ON DATA

def getFilter(filter_num, filters):
	if filter_num == 1 or filter_num == 2:
		filter_vessel = filters[filter_num - 1]
	else:
		filter_vessel = None
	return filter_vessel


def getBrandSpecs(brand_name, sim_settings):
	if brand_name == None:
		return None
	else:
		this_brand = Brand(brand_name, sim_settings.brand_dictionary[brand_name]["cost"], sim_settings.brand_dictionary[brand_name]["alcohol"])
		return this_brand

def getCompatibility(brand1_name, brand2_name, sim_settings):

		#Returns:
		#0 = Same Brand
		#1 = 50/50
		#2 = Premium to Non-Premium
		#3 = Water-Interphase
		#4 = Incompatible

		if brand1_name is not None and brand2_name is not None:
			cVal1 = sim_settings.compatibility_matrix[brand1_name][brand2_name]
			cVal2 = sim_settings.compatibility_matrix[brand2_name][brand1_name]

			if cVal1 == 0:
				return 0
			elif cVal1 == 1:
				if cVal2 == 1:
					return 1
				elif cVal2 == 2:
					return 1
				else:
					return 3
			elif cVal1 == 2:
				return 3
			elif cVal1 == 3:
				return 4
		else:
			return None

#PRINTING

def printHeadings(sheet):

	sheet.cell(row = 1, column = 9).value = "Compatibility Value"
	sheet.cell(row = 1, column = 10).value = "Financial Impact"
	sheet.cell(row = 1, column = 11).value = "Volume Switch"

def printer(sheet, r, compatibility_value, financial_impact, volume_switch):
	
	sheet.cell(row = r, column = 9).value = compatibility_value
	sheet.cell(row = r, column = 10).value = financial_impact
	sheet.cell(row = r, column = 11).value = volume_switch

def simulate(sheet, r, filters, sim_settings):

	filter_num = getFilterNum(sheet, r)
	brand1_name = getBrand1(sheet, r)
	brand2_name = getBrand2(sheet, r)
	wash_in = getWashIn(sheet, r)

	brand1 = getBrandSpecs(brand1_name, sim_settings)
	brand2 = getBrandSpecs(brand2_name, sim_settings)

	filter_vessel = getFilter(filter_num, filters)
	compatibility = getCompatibility(brand1_name, brand2_name, sim_settings)

	if brand1 != None and brand2 != None and filter_vessel != None:
		filter_simulation = FilterInterface(filter_vessel, brand1, brand2)
		cutoff_volume = sim_settings.interface_specs[filter_num - 1][compatibility]
		financial_impact = filter_simulation.financialImpactOfSwitch(cutoff_volume)
	else:
		cutoff_volume = 0
		financial_impact = 0

	printer(sheet, r, compatibility, financial_impact, cutoff_volume)


	




