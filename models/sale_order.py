# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from odoo.exceptions import Warning, ValidationError
from odoo import models, fields, api, _
from datetime import datetime
import datetime

class saleorderline(models.Model):
    _inherit='sale.order.line'

    customer=fields.Many2one('res.partner','Customer')


class SaleOrder(models.Model):
    _inherit='sale.order'
    
    @api.multi
    def action_confirm(self):
        project_obj = self.env['project.project']
        for line in self.order_line:
            print'HHHHHHHHHHHHHHHHHHH',line
            if line.customer:
                name_1 = line.product_id.name
                name_2 = line.customer.name
                print'KKKKKKKKKKKKKKKKK',name_1,name_2
                name = ''
                if name_1 and name_2:
                    name = name_2 + '-' + name_1
                today_d = datetime.datetime.now().date()
                project_values = {
                    'name': name or '',
                    'partner_id':self.partner_id.id or False,
                    'owner_id' : line.customer.id or False,
                    'issued_on': str(today_d) or False,
                }
                project_obj.create(project_values)
        return super(SaleOrder, self).action_confirm()