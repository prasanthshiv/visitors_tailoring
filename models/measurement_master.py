# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.


from odoo import models, fields, api, _
import time
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from odoo.exceptions import Warning

class MeasurementMeasurement(models.Model):
    _name = "measurement.measurement"
    _description = "Measurements"
    _rec_name = 'number'

    number = fields.Char(string='Measurement No.')
    partner_id = fields.Many2one('res.partner', "Customer")
    phone_number = fields.Char(
                               related='partner_id.phone',
                               string='Customer Phone',store=True)
    length = fields.Float(string='Length')
    body = fields.Float(string='Body')
    body_loose = fields.Float(string='Body Loose')
    bottom = fields.Float(string='Bottom')
    regal = fields.Float(string='Regal')
    shoulder = fields.Float(string='shoulder')
    hand_length = fields.Float(string='Hand Length')
    sleeve_length = fields.Float(string='Sleeve Length')
    sleeve_loose = fields.Float(string='Sleeve Loose')
    caf = fields.Float(string='Caf')
    neck = fields.Float(string='Neck')
    pocket_to_pocket = fields.Float(string='Pocket to Pocket top')
    pocket_to_pocket2 = fields.Float(string='Pocket to Pocket bottom')
    fsp = fields.Selection([('yes','YES'),('no','NO')],'FSP')
    fs = fields.Selection([('yes','YES'),('no','NO')],'FS')
    fspx = fields.Selection([('yes','YES'),('no','NO')],'FSPX')
    active = fields.Boolean(string="Active",default=True)
    date = fields.Date(String='Date', default=lambda *a: time.strftime(DEFAULT_SERVER_DATE_FORMAT))
    
    @api.model
    def create(self, vals):
        res = super(MeasurementMeasurement, self).create(vals)
        if res:
            res.number = self.env['ir.sequence'].get('measurement.measurement')
        return res
    def action_view(self):
        view_id = self.env.ref('project.edit_project')
        print view_id.type
        
        context = self._context.copy()
#        return {
#            'name':'Projects',
#            'view_type':'form',
#            'view_mode':'tree',
#            'view_id':view_id,
#
#            'views' : [(view_id,'form')],
#            'type':'ir.action.act_window',
#            'target':'current',
#            'res_id':self.id,
#            'context': context,
#            'res_model':' action.res_model'
#         }
        return {
                    'name': view_id.name,
                    'type': 'ir.actions.act_window',
                    'view_type': view_id.type,
                    'view_mode': 'tree,form',
                    'target': 'current',
                    'context': context,
                    'res_model':'project.project',
        
        }
