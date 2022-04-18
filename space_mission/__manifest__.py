# -*- coding: utf-8 -*-

{
    'name': 'Space Mission',
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
        'security/space_mission_security.xml',
        'security/ir.model.access.csv',
        'views/space_mission_menuitems.xml',
        'views/spaceship_views.xml',
        'views/mission_views.xml',
    ],
    'demo': [
        'demo/space_mission_demo.xml',
    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
