
from odoo.exceptions import Warning, ValidationError
from odoo import models, fields, api,_
import time
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from odoo.exceptions import Warning


class DesignStyle(models.Model):
    _name="design.style"
    _rec_name='name'
    
    partner_id = fields.Many2one('res.partner',string="Customer")
    measurements = fields.Many2one("measurement.measurement",string="measurements")
    date = fields.Date(String='Date', default=lambda *a: time.strftime(DEFAULT_SERVER_DATE_FORMAT))
    neck=fields.Many2one("desgn.desgn",string="neck",domain = [('type','=','neck')],required='True')
    collar=fields.Many2one("desgn.desgn",string="collar",domain = [('type','=','collar')],required='True')
    caf=fields.Many2one("desgn.desgn",string="caf",domain = [('type','=','caf')],required='True')
    pocket=fields.Many2one("desgn.desgn",string="pocket",domain = [('type','=','pocket')],required='True')
    neck_img=fields.Binary(related='neck.image',readonly=True,string=" ")
    collar_img=fields.Binary(related='collar.image',readonly=True,string=" ")
    caf_img=fields.Binary(related='caf.image',readonly=True,string=" ")
    pocket_img=fields.Binary(related='pocket.image',readonly=True,string=" ")
    style_c=fields.One2many("product.design","style",string="tree")
    name=fields.Char('',readonly='1') 
    extra_add=fields.One2many('design.addons',"addon",string="tree")
    ref=fields.Boolean('ref',default=False,compute="extradd")
    
    def extradd(self):
        obj = self.env["project.project"].search([("partner_id.id","=",self.partner_id.id)])
        for recs in obj:
            if  recs.addons==True:
                self.ref=True
              

              
        
    @api.model
    def create(self, vals):
        seq= self.env['ir.sequence'].get('design.style')
        vals['name'] = seq
        return super(DesignStyle, self).create(vals)
    


class ProductProduct(models.Model):
    _name="product.design"
    unit_qty=fields.Char('Unit/Qty')
    products=fields.Many2one('product.template',string='Product')
    uom=fields.Many2one('product.uom',string='Unit Of Measure')
    style=fields.Many2one("design.style")
    
    
   

class addonsadd(models.Model):
        _name="design.addons"
        addons=fields.Many2one('desgn.desgn',"addons",domain = [('type','=','addons')])
        quantity=fields.Integer("quantity")
        addon=fields.Many2one('desgn.desgn')
        