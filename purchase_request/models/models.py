# -*- coding: utf-8 -*-

from odoo import models, fields, api

READONLY_STATES = {
		'draft': [('readonly', False)],
	}
class inventory_custome (models.Model):
    _inherit = 'purchase.request'
    notes=fields.Char(' ')  # to hide field
    req_dep_id = fields.Many2one('hr.department',string="Requested Department",states=READONLY_STATES, readonly=1)

class inventory_custome_line(models.Model):
    _inherit = 'purchase.request.line'
    req_dep_id = fields.Many2one ('hr.department', string="Requested Department")
