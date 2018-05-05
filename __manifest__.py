# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details

{
    'name': 'Tailoring MANAGMENT',
    'version': '2.1',
    'category': 'PROJECT',
    'description': """
Tailoring Management

Odoo Tailoring Management System will help you to manage your real Tailoring
portfolio with Measurement, Management of Deisings ,stitching,washing and ironing
management with reminders for each KPIs. ODOO's easy to use Content management
system help you to display available tailors and assigning the jobs for them. its
gallery and other details to reach easily to end users. With the help of
inbuilt Business Intelligence system it will be more easy to get various
analytical reports and take strategical decisions
     """,
    'author': 'Netex Solutions Pvt. Ltd.',
    'website': 'http://www.netexsolutions.com',
    'depends': ['sale','project','hr'],
    'data': [
             'data/measurement_seq.xml',
             'views/measurement_master_view.xml',
             'views/res_partner_views.xml',
             'views/sale_order_view.xml',
             'views/design_master_view.xml',
             'views/employee_profile.xml',
    ],
    'auto_install': False,
    'installable': True,
    'application': True,
}
