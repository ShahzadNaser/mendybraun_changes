from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils.password import encrypt

def validate(self, method):
	if not self.route_name:
		self.route_name = encrypt(self.name)

def send_order_confirmation(self, method):
	return
	# if self.docstatus == 1:
	# 	recipients = self.contact_email
	# 	frappe.sendmail(
	# 		recipients=recipients,
	# 		subject=_("Sales Order Confirmation"),
	# 		template="sales_order_confirmation",
	# 		args=dict(
	# 			doc=self,
	# 			site_url=frappe.utils.get_site_url(frappe.local.site)
	# 		),
	# 		header=_("Sales Order Confirmation")
	# 	)