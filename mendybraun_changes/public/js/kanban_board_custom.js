frappe.ui.form.on("Kanban Board", {
	refresh: function(frm){
		var option_fields = [];
		var fields = frappe.get_meta(frm.doc.reference_doctype).fields;
		$.each(fields || [], function(i,v){
			if(v.fieldname && !v.fieldtype.includes(['Table', 'Section Break', 'Column Break', 'Table MultiSelect', 'Fold']) ){
				option_fields.push(v.fieldname);
			}
		});
		frappe.meta.get_docfield('Kanban Board Fields', 'field', frm.doc.name).options = option_fields;
		var grid_rows = frm.fields_dict["fields"].grid.grid_rows_by_docname;
		$.each(grid_rows || [], function(i, v){
			frappe.meta.get_docfield('Kanban Board Fields', 'field', i).options = option_fields;
		});
		frm.refresh_field("fields");
	},
	validate: function(frm){
		var duplicate = [];
		$.each(frm.doc.fields || [], function(i,v) {
			if(duplicate.includes(v.field)){
				frappe.throw(__(`Duplicate Fieldname ${ v.field }`));
			}
			else{
				duplicate.push(v.field);
			}
		});
	}
});

frappe.ui.form.on("Kanban Board Fields", {
	add_fields: function(frm){
		
	}
});