from __future__ import unicode_literals
import frappe

@frappe.whitelist(allow_guest=True)
def update_sales_order_status(sales_order, status="Rejected"):
	frappe.db.set_value("Sales Order", sales_order, "status", status)