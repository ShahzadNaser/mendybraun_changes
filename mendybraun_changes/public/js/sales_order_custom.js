frappe.ui.form.on("Sales Order", {
	validate: function(frm){
		var doc = frm.doc;
		var deposit_amount = (doc.rounded_total * doc.deposit_percentage)/100;
		frm.set_value("deposit_amount", deposit_amount);
	}
});