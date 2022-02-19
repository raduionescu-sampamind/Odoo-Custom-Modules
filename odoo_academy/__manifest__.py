# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy Module',
    'version': '1.0',
    'summary': 'Odoo Technical Training module',
    'description': 'Module developed for the Odoo Technical Training sessions.',
    'category': 'Custom',
    'author': 'Radu Ionescu',
    'website': 'https://www.sampamind.com',
    'license': 'LGPL-3',
    'depends': [

    ],
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/course_views.xml',
    ],
    'demo': [
        'demo/academy_demo.xml',
    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
