frappe.ui.form.on("BOM Item", {
	item_code: function(frm, cdt, cdn){
		var doc = locals[cdt][cdn];
		if (doc.item_code){
			frappe.call({
				method: "frappe.client.get",
				args: {
					doctype: "Item",
					name: doc.item_code
				},
				callback: function(r){
					if(!r.exec){
						frappe.model.set_value(cdt, cdn, "waste_percentage", r.message.waste_percentage);
					}
				}
			});
		}
		else{
			frappe.model.set_value(cdt, cdn, "waste_percentage", "");
		}
	},
	width: function(frm, cdt, cdn){
		calculate_item_percentage_with_waste(frm, cdt, cdn);
	},
	height: function(frm, cdt, cdn){
		calculate_item_percentage_with_waste(frm, cdt, cdn);
	}
});


var calculate_item_percentage_with_waste = function(frm, cdt, cdn){
	var doc = locals[cdt][cdn];
	var item_width = 0;
	var item_height = 0;
	var width = 0;
	var height = 0;
	var waste_percentage = 0;
	if(doc.item_width && doc.item_width > 0){
		item_width = doc.item_width;
	}
	if(doc.item_height && doc.item_height > 0){
		item_height = doc.item_height;
	}
	if(doc.width && doc.width > 0){
		width = doc.width;
	}
	if(doc.height && doc.height > 0){
		height = doc.height;
	}
	if(doc.waste_percentage && doc.waste_percentage > 0){
		waste_percentage = doc.waste_percentage;
	}

	console.log([item_width, item_height, width, height, waste_percentage]);

	var item_sqft = item_width * item_height;
	var sqft = width * height;

	var waste = (waste_percentage*item_sqft)/100;

	var percentage = 0
	if(item_sqft > 0){
		percentage = (sqft/item_sqft);
	}

	console.log(percentage);


}