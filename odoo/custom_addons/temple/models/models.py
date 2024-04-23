# -*- coding: utf-8 -*-

from odoo import models, fields, api


class temple(models.Model):
    _name = 'temple.temple'
    _inherit = ['mail.thread']
    _description = 'This is temple description'

    name = fields.Char(string='name',required=True,tracking=True)
    temple_name = fields.Char(string='temple_name',tracking=True)
    age = fields.Integer(string = 'age',tracking=True)
    is_child = fields.Boolean(string='is_child?',tracking=True)
    notes = fields.Text(string='Notes',tracking=True)
    gender = fields.Selection([('male', 'male'), ('female', 'female'),('others', 'others')], string='gender')
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

