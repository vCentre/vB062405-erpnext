# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals

import frappe
from frappe import _
import frappe.defaults
from erpnext.shopping_cart.doctype.shopping_cart_settings.shopping_cart_settings import is_cart_enabled

def show_cart_count():
	if (is_cart_enabled() and
		frappe.db.get_value("User", frappe.session.user, "user_type") == "Website User"):
		return True

	return False

def set_cart_count(login_manager):
	if show_cart_count():
		from erpnext.shopping_cart.cart import set_cart_count
		set_cart_count()

def clear_cart_count(login_manager):
	if show_cart_count():
		frappe.local.cookie_manager.delete_cookie("cart_count")

def update_website_context(context):
	cart_enabled = is_cart_enabled()
	context["shopping_cart_enabled"] = cart_enabled

def update_my_account_context(context):
	context["my_account_list"].extend([
		{"label": _("Orders"), "url": "orders"},
		{"label": _("Invoices"), "url": "invoices"},
		{"label": _("Shipments"), "url": "shipments"},
		{"label": _("Issues"), "url": "issues"},
		{"label": _("Addresses"), "url": "addresses"},
	])
