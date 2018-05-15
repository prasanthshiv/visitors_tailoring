from odoo import models, fields, api, _
from datetime import datetime

class ProjecProject(models.Model):
    _inherit = "project.project"
    
    second_name = fields.Char('JOB ID')
    owner_id =  fields.Many2one('res.partner', 'Making for')
    issued_on =  fields.Date('Issued on')
    req_addons = fields.Boolean(string="Extra Addons")

    @api.model
    def create(self, vals):
        if vals.get('name'):
            name = vals.get('name')
            seq = self.env['ir.sequence'].get('project.project')
            vals['second_name'] = seq
            print'GGGGGGGGGGGGGGGGG',vals,seq
            vals['name'] = seq +'-'+name
            res = super(ProjecProject, self).create(vals)
        return res