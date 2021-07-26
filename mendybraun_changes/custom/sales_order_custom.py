from __future__ import unicode_literals
import frappe
from frappe import _

def send_order_confirmation(self, method):
	if self.docstatus == 1:
		recipients = self.contact_email
		frappe.sendmail(
			recipients=recipients,
			subject=_("Sales Order Confirmation"),
			template="sales_order_confirmation",
			args=dict(
				doc=self,
				site_url=frappe.utils.get_site_url(frappe.local.site)
			),
			header=_("Sales Order Confirmation")
		)