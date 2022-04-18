from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'

    # ATTRIBUTES ####################################################====================---------------
    name = fields.Char(string='Name', required=True)
    # authors = fields.One2many()
    # editors = fields.One2many()
    publisher = fields.Char(string='Publisher', required=True)
    year = fields.Date(string='Year')
    isbn = fields.Char(string='ISBN', required=True)
    genre = fields.Selection([
                            ('drama', 'Drama'),
                            ('fantasy', 'Fantasy'),
                            ('sci_fi', 'Sci-Fi'),
                            ('mystery', 'Mystery'),
                            ('romance', 'Romance'),
                            ('contemporary', 'Contemporary'),
                            ('other', 'Other'),
                        ], string='Genre', default='other')

    # METHODS #######################################################====================---------------
    @api.onchange('isbn')
    def _onchange_isbn(self):
        if len(self.isbn) != 13:
            raise ValidationError('ISBN should be 13 characters long! Input length: %s' % len(self.isbn))
