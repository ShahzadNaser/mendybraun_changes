# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe import _

@frappe.whitelist()
def get_fields_data(data, board):
	board = json.loads(board)
	data = json.loads(data)
	for a in data:
		doc = frappe.get_doc(board['reference_doctype'], a['name']).as_dict()
		for custom in board['fields']:
			a[custom['field']] = doc[custom['field']]
	return data