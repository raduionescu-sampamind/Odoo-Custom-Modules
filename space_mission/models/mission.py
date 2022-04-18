from odoo import fields, models, api


class Mission(models.Model):
    _name = 'space.mission.mission'
    _description = 'Mission'

    # ATTRIBUTES ####################################################======================================----------------------------
    name = fields.Char(string='Title')
    spaceship_id = fields.Many2one(comodel_name='space.mission.spaceship', string='Spaceship')
    crew_member_ids = fields.Many2many(comodel_name='res.partner', string='Crew Members')
    launch_date = fields.Date(string='Launch Date')
    return_date = fields.Date(string='Return Date')

    # METHODS #######################################################======================================----------------------------
