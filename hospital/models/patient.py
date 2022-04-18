from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"

    name = fields.Char(string="Full Name", compute='_compute_full_name')
    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='other')
    note = fields.Text(string='Patient History')

    @api.depends('first_name', 'last_name')
    def _compute_full_name(self):
        self.name = self.first_name + ' ' + self.last_name
