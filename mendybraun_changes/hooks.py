from . import __version__ as app_version

app_name = "mendybraun_changes"
app_title = "ERPNext Changes for jplakerp"
app_publisher = "nomi-g"
app_description = "ERPNext Changes for jplakerp"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "nomi9639@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mendybraun_changes/css/mendybraun_changes.css"
app_include_js = "/assets/js/kanban_view_custom.js"

# include js, css files in header of web template
# web_include_css = "/assets/mendybraun_changes/css/mendybraun_changes.css"
# web_include_js = "/assets/mendybraun_changes/js/mendybraun_changes.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "mendybraun_changes/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = { 
	"BOM" : "public/js/bom_custom.js",
	"Kanban Board" : "public/js/kanban_board_custom.js",
	"Task": "public/js/task_custom.js",
	"Sales Order": "public/js/sales_order_custom.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "mendybraun_changes.install.before_install"
# after_install = "mendybraun_changes.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mendybraun_changes.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Item": {
		"after_insert": "mendybraun_changes.custom.item.after_insert"
	},
	"BOM": {
		"validate": "mendybraun_changes.custom.bom.validate"
	},
	"Sales Order": {
		"validate": "mendybraun_changes.custom.sales_order_custom.validate",
		"on_submit": "mendybraun_changes.custom.sales_order_custom.send_order_confirmation"
	}
}

jenv = {
    "methods": [
        "get_item_barcode:mendybraun_changes.custom.item.get_item_barcode"
    ]
}


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"mendybraun_changes.tasks.all"
# 	],
# 	"daily": [
# 		"mendybraun_changes.tasks.daily"
# 	],
# 	"hourly": [
# 		"mendybraun_changes.tasks.hourly"
# 	],
# 	"weekly": [
# 		"mendybraun_changes.tasks.weekly"
# 	]
# 	"monthly": [
# 		"mendybraun_changes.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "mendybraun_changes.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "mendybraun_changes.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "mendybraun_changes.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"mendybraun_changes.auth.validate"
# ]

