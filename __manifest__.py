# -*- coding: utf-8 -*-
{
    'name': "Biznizku Customization",  # Module title
    'summary': "Biznizku Addons",  # Module subtitle phrase
    'description': """Long description""",  # You can also rst format
    'author': "biznizku",
    'website': "https://biznizku.com",
    'category': 'Specific Industry Applications',
    'version': '12.0.1',
    'depends': ['base'],
    # This data files will be loaded at the installation (commented becaues file is not added in this example)
    'data': [
        'security/groups.xml', 
        'security/ir.model.access.csv',
        'views/views.xml'
    ],
    'installable': True,
    'application': True,
    # This demo data files will be loaded if db initialize with demo data (commented becaues file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],
}
