# Copyright (c) 2021, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

import frappe
from frappe.utils import cint, cstr, flt

def validate(self, method):
	pass
	# if self.items:
	# 	for d in self.items:
	# 		item = frappe.get_doc("Item", d.item_code)
	# 		if item.width and item.height and d.width and d.height:
	# 			item_sqft = item.width * item.height
	# 			sqft = d.width * d.height
	# 			waste = 0
	# 			if item.waste_percentage:
	# 				waste = ((item.waste_percentage/100)+1)
	# 			percentage = 0
	# 			if item_sqft > 0:
	# 				percentage = (sqft/item_sqft)
	# 			if item.waste_percentage:
	# 				percentage = percentage * waste

	# 			if percentage > 0:
	# 				d.rate = percentage
	# 				d.amount = flt(d.rate) * flt(d.qty)
	# 				d.base_rate = flt(d.rate) * flt(self.conversion_rate)
	# 				d.base_amount = flt(d.amount) * flt(self.conversion_rate)

	# 	self.update_exploded_items(save=False)
