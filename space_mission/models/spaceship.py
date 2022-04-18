from odoo import fields, models, api
from odoo.exceptions import UserError


class Spaceship(models.Model):
    _name = 'space.mission.spaceship'
    _description = 'Spaceship'

    # ATTRIBUTES ####################################################======================================----------------------------
    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', required=True, default=True)
    length = fields.Float(string='Length')
    width = fields.Float(string='Width')
    passenger_number = fields.Integer(string='Passenger No.')
    mission_ids = fields.One2many(comodel_name='space.mission.mission', inverse_name='spaceship_id', string='Missions')
    ship_type = fields.Selection([
                                ('type_1', 'Small Ship'),
                                ('type_2', 'Cruiser Ship'),
                                ('type_3', 'Destroyer Ship'),
                            ], string='Type', required=True)
    fuel_type = fields.Selection([
                                ('gas', 'Gas'),
                                ('gasoline', 'Gasoline'),
                                ('av_gas', 'Aviation Gasoline'),
                                ('bio_diesel', 'Bio Diesel'),
                            ], string='Fuel', required=True)

    # METHODS #######################################################======================================----------------------------
    @api.constrains('length', 'width')
    def _check_dimensions(self):
        for spaceship in self:
            if spaceship.width > spaceship.length:
                raise UserError('Width can not be greater than length! Input: l: %s w: %s' % (spaceship.length, spaceship.width))
