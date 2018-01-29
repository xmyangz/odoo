# –*– coding: utf-8 –*–
from odoo import models, fields, api

class TodoTask(models.Model):
	_inherit = 'todo.task'
	user_id = fields.Many2one('res.users', 'Responsible') 
	date_deadline = fields.Date('Deadline')
	name = fields.Char(help="What needs to be done?")

	@api.multi
	def do_toggle_done(self): 
		for task in self:
			task.is_done = not task.is_done 
		return True

	@api.model
	def do_clear_done(self):
		dones = self.search([('is_done', '=', True)]) 
		dones.write({'active':False})
		return True
