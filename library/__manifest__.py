{
    'name': 'Library Management',
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
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/book_menuitems.xml',
        'views/book_views.xml',
    ],
    'demo': [
        'demo/library_demo.xml',
    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
