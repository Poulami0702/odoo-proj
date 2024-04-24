# -*- coding: utf-8 -*-
{
    'name': "Real Estate Ads.",

    'summary': 
    """
    This is the Real estate ads. to show available properties.
    """,

    'description': """
This is the Real estate ads. to show available properties
    """,

    'author': "school_student",
    'website': "https://www.yourcompany.com/school_student",
    'application':True,
    'installable':True,
    'license':"LGPL-3",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/res_groups.xml',
        'data/estate.property.type.csv',
        'views/property_views.xml',
        'views/property_type_views.xml',
        'views/property_tags_views.xml',
        'views/property_offers_views.xml',
        'views/menu.xml',
        # 'data/property_type_data.xml',
        
        
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/property_tag.xml',
    ],
}

