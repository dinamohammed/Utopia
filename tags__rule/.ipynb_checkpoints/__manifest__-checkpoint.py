# -*- coding: utf-8 -*-
{
    'name': "Tags_Rule",

    'summary': """
        HR customizations""",

    'description': """
        This module consist of multiple customizations additional requirements on Employee and Payroll modules.
    """,

    'author': "Egymentors - Dina Salah",
    'website': "http://www.egymentors.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr_payroll', 'hr'],

    # always loaded
    'data': [
        'data/hr_level_data.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/location.xml',
        'views/contractType.xml',
        'views/search.xml',
    ],
    # only loaded in demonstration mode
}
