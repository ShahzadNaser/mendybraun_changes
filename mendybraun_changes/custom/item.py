# Copyright (c) 2021, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

import frappe
import barcode
from barcode.writer import ImageWriter
from random import randrange
from functools import reduce
from barcode import generate
import random
import os.path

def after_insert(self, method):
	if not self.barcodes:
		numbers = generate_12_random_numbers()
		numbers.append(calculate_checksum(numbers))
		brc = ''.join(map(str, numbers))
		br = self.append("barcodes", {})
		br.barcode = brc
		br.barcode_type = 'UPC-A'
		self.save()
	else:
		brc = self.barcodes[0].barcode
	barcode.base.Barcode.default_writer_options['write_text'] = False
	EAN = barcode.get_barcode_class('Code128')
	ean = EAN(brc, writer=ImageWriter())
	filename = frappe.utils.get_files_path() + '/' + brc + ''
	name = generate('EAN13', brc, output=filename)
	return 'files/'+brc+'.svg'


def generate_12_random_numbers():
	numbers = []
	for x in range(12):
		numbers.append(randrange(10))
	return numbers

def calculate_checksum(ean):
	"""
	Calculates the checksum for an EAN13
	@param list ean: List of 12 numbers for first part of EAN13
	:returns: The checksum for `ean`.
	:rtype: Integer
	"""
	assert len(ean) == 12, "EAN must be a list of 12 numbers"
	sum_ = lambda x, y: int(x) + int(y)
	evensum = reduce(sum_, ean[::2])
	oddsum = reduce(sum_, ean[1::2])
	return (10 - ((evensum + oddsum * 3) % 10)) % 10


def get_item_barcode(item_code):
	item = frappe.get_doc("Item", item_code)

	if not item.barcodes:
		after_insert(item, "after_insert")
	brc = item.barcodes[0].barcode
	filename = frappe.utils.get_files_path() + '/' + brc + '.svg'
	if not os.path.isfile(filename):
		barcode.base.Barcode.default_writer_options['write_text'] = False
		generate('EAN13', brc, output=frappe.utils.get_files_path() + '/' + brc)

	return '/files/'+brc+'.svg'



