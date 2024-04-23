from odoo import fields, models , api
from datetime import timedelta

from odoo.exceptions import ValidationError

class TransientOffer(models.TransientModel):
    '''
    Transient models are the models that stores data for a limitted time. 
    '''
    _name='transient.model.offer'
    _description='Transient offer'
    _transient_max_count = 0 #for limiting number of rows
    _transient_max_hours = 2.0 #limiting number of hours data needs to be there in database # float value

    @api.autovacuum
    def _transient_vacuum(self):
        return super()._transient_vacuum()

    partner_email = fields.Char(string='Email')
    partner_phone = fields.Char(string='Phone No.')


class AbstractOffer(models.AbstractModel):
    '''
    Abstract models are the models that dont store database in its own table , its is use to inherite 
    '''
    _name='abstract.model.offer'
    _description='Abstract offer'

    partner_email = fields.Char(string='Email')
    partner_phone = fields.Char(string='Phone No.')

class PropertyOffers(models.Model):
    _name = "estate.property.offers"
    _inherit=['abstract.model.offer']
    _description = "This is the estate property offers"

    price=fields.Float(string="Price")
    status= fields.Selection([('accepted','Accepted'),('rejected','Rejected')],
                                         string="Status")
    partner_id=fields.Many2one('res.partner', string='Customer')
    property_id = fields.Many2one('estate.property', string='Property')
    validity=fields.Integer(string="validity")
    deadline = fields.Date(string="Deadline", compute='_compute_deadline')
    creation_date= fields.Date(string="Create Date", default=lambda self: fields.Date.today())


    @api.depends('validity','creation_date')
    def _compute_deadline(self):
        for rec in self:
            if rec.creation_date and rec.validity:
                rec.deadline= rec.creation_date + timedelta(days=rec.validity)
            else:
                rec.deadline=False
    
    # @api.model_create_multi
    # def create(self,vals):
    #     for rec in vals:
    #         if not rec.get('creation_date'):
    #             rec['creation_date']=fields.Date.today()
    #         return super(PropertyOffers,self).create(vals)
        
    

    def action_accept_offer(self):
        if self.property_id:
            self._validate_accepted_offer()
            self.property_id.write({
                'selling_price': self.price,
                'state': 'accepted'
            })
        self.status = 'accepted'

    def _validate_accepted_offer(self):
        offer_ids = self.env['estate.property.offers'].search([
            ('property_id', '=', self.property_id.id),
            ('status', '=', 'accepted'),
        ])
        if offer_ids:
            raise ValidationError("You have an accepted offer already")

    def action_decline_offer(self):
        self.status = 'rejected'
        if all(self.property_id.offer_ids.mapped('status')):
            self.property_id.write({
                'selling_price': 0,
                'state': 'received'
            })

    def extend_offer_deadline(self):
        activ_ids = self._context.get('active_ids', [])
        if activ_ids:
            offer_ids = self.env['estate.property.offers'].browse(activ_ids)
            for offer in offer_ids:
                offer.validity = 10

    def _extend_offer_deadline(self):
        offer_ids = self.env['estate.property.offers'].search([])
        for offer in offer_ids:
            offer.validity = offer.validity + 1