from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError


class Course(models.Model):
    _name = 'academy.course'
    _description = 'Course'

    # ATTRIBUTES ####################################################======================================----------------------------
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
    base_price = fields.Float(string='Base price', default=0.0)
    additional_fee = fields.Float(string='Additional fee', default=10.0)
    total_price = fields.Float(string='Total price', readonly=True)
    session_ids = fields.One2many(comodel_name='academy.session', inverse_name='course_id', string='Sessions')
    level = fields.Selection([
                            ('beginner', 'Beginner'),
                            ('intermediate', 'Intermediate'),
                            ('advanced', 'Advanced'),
                        ], string='Level', copy=False)

    # METHODS #######################################################======================================----------------------------
    @api.onchange('base_price', 'additional_fee')
    def _onchange_total_price(self):
        if self.base_price < 0.00:
            raise UserError('Base price can not be negative!')
        self.total_price = self.base_price + self.additional_fee

    @api.constrains('additional_fee')
    def _check_additional_fee(self):
        for course in self:
            if course.additional_fee < 10.00:
                raise ValidationError('Additional fees can not be less than 10! Input: %s' % course.additional_fee)
