from odoo import models, fields, api,_


class DesgnDesgn(models.Model):
     _name="desgn.desgn"
     
     name = fields.Char('name')
     image= fields.Binary( string="image",help="Select image here")    
     type=fields.Selection([('neck',"Neck"),
                            ('collar','Collar'),
                            ('caf','Caf'),
                            ('pocket','pocket'),
                            ('addons','Addons')
                            ], string="Design Type")
 