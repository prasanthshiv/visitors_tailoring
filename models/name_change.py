from odoo import models, fields, api,_

class ParentChildName(models.Model):
	_inherit="sale.order"

	@api.onchange('partner_id')
	def name_search(self):
		res=[]
		customers=self.env['res.partner'].search([])

		for obj in customers:
			if obj.display_name.find(',')!=-1:
				name=str(obj.display_name)
				child_name=name.split(",")[1]
				parent_name=name.split(",")[0]
				res.append(child_name+","+parent_name)
		self.parent_name=res
	# @api.onchange('partner_id')
	# def name_search(self,args=None, operator='ilike', limit=100):
	# 	name=self.env['res.partner'].search([])
	# 	args = args or []
 #                if name:
	# 	# Be sure name_search is symetric to name_get
	# 		name = name.split(' / ')[-1]
	# 		args = [('name', operator, name)] + args
	# 	locs = self.search(args, limit=limit)
	# 	if len(locs) == 1:
	# 		child_dom = [('parent_left', '>', locs[0].parent_left), ('parent_left', '<', locs[0].parent_right)] 
	# 		child_locs = self.search(child_dom)
	# 		locs = locs + child_locs
			
	# 	return locs.name_get()


