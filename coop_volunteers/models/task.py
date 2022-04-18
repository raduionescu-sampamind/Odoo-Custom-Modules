from odoo import fields, models, api


class Task(models.Model):
    _name = 'volunteers.task'
    _description = 'Task'

    # ATTRIBUTES ####################################################====================---------------
    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    leader = fields.Char(string='Leader')
    start = fields.Datetime(string='Start Time', required=True)
    stop = fields.Datetime(string='Stop Time', required=True)
    is_repeating = fields.Boolean(string='Repeatable', default=False)
    repetition_frequency = fields.Selection([
                                            ('daily', 'Daily'),
                                            ('weekly', 'Weekly'),
                                            ('monthly', 'Monthly'),
                                            ('yearly', 'Yearly'),
                                        ], string='Frequency')
    type = fields.Selection([
                            ('type_1', 'Type 1'),
                            ('type_2', 'Type 2'),
                            ('type_3', 'Type 3'),
                            ('type_4', 'Type 4'),
                            ('type_5', 'Type 5'),
                        ], string='Type')
    state = fields.Selection([
                            ('draft', 'Draft'),
                            ('ready', 'Ready'),
                            ('in_progress', 'In progress'),
                            ('done', 'Done'),
                        ], string='State', default='draft')

    # METHODS #######################################################====================---------------
    @api.onchange('leader')
    def _onchange_leader(self):
        self.state = 'ready'
