from odoo import api, fields, models,_

class Tailorcutting(models.Model):
	_inherit='project.task'
	bool_field = fields.Boolean('Same text', default=False)
	product_cutting = fields.One2many('product.cutting', 'task_id', string='product cutting')
	# @api.onchange('project_id')
	# def change_stage(self):
	    
	#     print "kkkkkkkkkkkkkkkkkkkkk"
	#     # 
	#     # self.stage_id = self.stage_find(self.project_id.id, [('name', '=',"cutting")])
	#     stage_obj=self.env['project.task.type'].search([('name','=','cutting')])
	#     print self.stage_id
	#     self.stage_id=stage_obj.sequence

	    # for i in stage_obj:
	    #     print "kkkkkkkkkkkkkkkkkkkkk"

	#     


	def cutting_finish(self):
		self.kanban_state ="done"
		for i in self.product_cutting:
			stock_obj=self.env['stock.quant'].search([("product_id","=",i.products.id)])
			current_stock=stock_obj[len(stock_obj)-1].qty
			update_qty= current_stock-i.unit_qty
			stock_obj.write({"qty":update_qty})
		self.bool_field = True			
    
class Productcutting(models.Model):
    _name='product.cutting'

    products=fields.Many2one('product.template',string='Product')
    unit_qty=fields.Float('Unit/Qty')
    uom=fields.Many2one('product.uom',string='Unit Of')
    task_id=fields.Many2one('product_cutting',string='task')


    



