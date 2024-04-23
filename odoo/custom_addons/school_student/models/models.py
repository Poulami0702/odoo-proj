
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SchoolStudent(models.Model):
    _name = 'school.student'
    _inherit = ['mail.thread']
    _order = 'age desc'
    _description = 'school_student.school_student'

    name = fields.Char(string='name',required=True,tracking=True)
    school_id = fields.Many2one('school.class',string='school_name')
    age = fields.Integer(string = 'age',tracking=True)
    is_child = fields.Boolean(string='is_child?',tracking=True)
    notes = fields.Text(string='Notes',tracking=True)
    gender = fields.Selection([('male', 'male'), ('female', 'female'),('others', 'others')], string='gender')
    capitalized_name = fields.Char(string='capitalized_name', compute='_compute_capitalized_name', store=True) #to store compute field in databse, we have to write store = True
    ref = fields.Char(string = "Referance", default= lambda self: _('New'))
    tag_id = fields.Many2many('res.partner.category', string='Tag')
    country_id = fields.Many2one('res.country',string='country')
    state_ids = fields.Many2many('res.country.state',string='state',)
    country_code= fields.Char(string="country_code",related = "country_id.code")   #this is the related field. where related has to be many to one field , as country_id is many to one field . hence->country_id.code -> where code is the related field  
    staff_line_ids = fields.One2many("res.staff.lines", "connecting_field", string="staff_line_ids")
    establish_date= fields.Date(string="Establish Date")
    open_date = fields.Datetime(string="Open Date")
    documents = fields.Binary(string="Documents")
    document_name = fields.Char(string="File name")



    @api.model_create_multi
    def create(self,val_list):
        #val_list is the list of all data 
        #if we want to change before creating we can inherit and change the value and then create them
        # for creating sequence
        for vals in val_list:
            vals['ref']=self.env["ir.sequence"].next_by_code('school.student')
        return super(SchoolStudent,self).create(val_list)

    @api.depends('name')
    def _compute_capitalized_name(self):
        for rec in self: 
            #iterrating over self -> as there are many items so have the computed value for all the items
            if rec.name:
                rec.capitalized_name=self.name.upper()
            else:
                rec.capitalized_name=""

    @api.onchange('age')
    def _onchange_age(self):
        if self.age<=10:
            self.is_child=True
        else:
            self.is_child=False

    @api.constrains("is_child","age")
    def _chcek_child_age(self):
        for rec in self:
            if rec.is_child and rec.age==0:
                raise ValidationError(("Age has to be recorded"))
            
class ResStaffLine(models.Model):
    _name = 'res.staff.lines'
    _inherit = ['mail.thread']
    _description = "This is for res_staff model"


    connecting_field = fields.Many2one("school.student", string="Student")
    name = fields.Char(string='name',required=True,tracking=True)
    product_id = fields.Many2one('product.product',string = "product")