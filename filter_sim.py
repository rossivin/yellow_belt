import math
import openpyxl as xl
from brand import Brand
from filter_interface import FilterInterface
from filter_vessel import FilterVessel
from settings import Settings
import functions

#Initialize Simulation Settings
ss = Settings()
filter1 = FilterVessel(ss.filter_specs[0]["volume"], ss.filter_specs[0]["pre_volume"], ss.filter_specs[0]["post_volume"])
filter2 = FilterVessel(ss.filter_specs[1]["volume"], ss.filter_specs[1]["pre_volume"], ss.filter_specs[1]["post_volume"])
filters = [filter1, filter2]

#Initialize Spreadsheets
wb = xl.load_workbook(filename = ss.data_workbook)
brand_sh = wb[ss.brand_sheet]
data_sh = wb[ss.data_sheet]
matrix_sh = wb[ss.matrix_sheet]

def main_loop():
	
	functions.printHeadings(data_sh)
	for r in range(2, data_sh.max_row+1):
		functions.simulate(data_sh, r, filters, ss)
	wb.save(ss.data_workbook)

def test_filter():

	filter_volume = 40
	filter_pre_volume = 11.6
	filter_post_volume = 75-11.6-40

	my_filter = FilterVessel(filter_volume, filter_pre_volume, filter_post_volume)

	brand1_name = "CHIPIE"
	brand2_name = "CIBOIRE"

	brand1 = functions.getBrandSpecs(brand1_name, ss)
	brand2 = functions.getBrandSpecs(brand2_name, ss)

	brand1.alcohol = 7.77
	brand2.alcohol = 0.1

	filter_simulation = FilterInterface(my_filter, brand1, brand2)
	switch_volume = 37.5
	financial_impact = filter_simulation.financialImpactOfSwitch(switch_volume)
	outlet_composition = filter_simulation.outletComposition(1,switch_volume)*100

	print("Brand 1:",brand1_name)
	print("Brand 2:",brand2_name)
	print("Filter Volume:",filter_volume,"hL")
	print("Filter Pre-Volume:",filter_pre_volume,"hL")
	print("Filter Post-Volume:",filter_post_volume,"hL")
	print("Switch Volume:",switch_volume,"hL")
	print("Financial Impact",financial_impact,"$")
	print("Outlet Composition",outlet_composition,"%")

main_loop()
test_filter()

