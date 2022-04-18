{
    'name': 'Hospital Management',
    'version': '1.0',
    'summary': 'Hospital management Odoo module',
    'sequence': 10,
    'description': 'Module for managing hospital patients and their appointments.',
    'category': 'Custom',
    'website': 'https://www.sampamind.com',
    'depends': [
        'sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml',
        'views/sale.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
