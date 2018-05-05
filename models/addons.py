from odoo.exceptions import Warning, ValidationError
from odoo import models, fields, api, _

class addonsaddons(models.Model):
    _inherit='project.project'
    
    addons=fields.Boolean(string="Extra Addons")
    
    
#    @api.onchange('addons')
#    def functionaddons(self):
#        obj = self.env["design.style"].search([("partner_id.id","=",self.partner_id.id)])
#        if self.addons==True:
#           for recs in obj:
#               recs.ref=True
#               print recs.partner_id.name,recs.ref
#               
