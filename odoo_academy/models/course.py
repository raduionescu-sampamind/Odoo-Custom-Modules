# -*- coding: utf-8 -*-

from odoo import fields, models, api


class Course(models.Model):
    _name = 'academy.course'
    _description = 'Course'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
    level = fields.Selection([
                            ('beginner', 'Beginner'),
                            ('intermediate', 'Intermediate'),
                            ('advanced', 'Advanced'),
                        ], string='Level', copy=False)
