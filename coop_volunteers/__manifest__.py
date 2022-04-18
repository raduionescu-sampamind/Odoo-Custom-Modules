{
    'name': 'Cooperative Volunteering',
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
        'security/volunteers_security.xml',
        'security/ir.model.access.csv',
        'views/task_menuitems.xml',
        'views/task_views.xml',
    ],
    'demo': [
        'demo/volunteers_demo.xml',
    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
