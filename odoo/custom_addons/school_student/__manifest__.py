# -*- coding: utf-8 -*-
{
    'name': "school_student_management",

    'summary': "This is the one line summary for school student",

    'description': """
school student list
    """,

    'author': "school_student",
    'website': "https://www.yourcompany.com/school_student",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv', #security file has to be on top
        'data/sequence.xml', #sequence file has to be before views file
        'views/menu.xml',
        'views/student.xml',
        'views/school.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

