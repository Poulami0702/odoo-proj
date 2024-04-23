from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SchoolClass(models.Model):
    _name = 'school.class'
    _inherit = ['mail.thread']
    _description = 'school Records'
    _rec_name = 'name_ref' #by default _rec_name = 'name' if we want to change then we have to define it seperately
    
    name = fields.Char(string='name',required=True,tracking=True)
    # school_name = fields.Char(string='school_name',required=True,tracking=True)
    ref = fields.Char(string = "Referance",required=True)
    active = fields.Boolean(default=True)
    name_ref = fields.Char(string="Name/Reference", compute='_compute_name_ref', store=True)
    school_image = fields.Image(string="school image",max_width =100, max_height=100)
    school_description = fields.Html(dtring="school description")

    @api.depends('name', 'ref')
    def _compute_name_ref(self):
        for record in self:
            record.name_ref = f"{record.name} - {record.ref}"

    def name_get(self):
        return [(record.id, record.name_ref) for record in self]