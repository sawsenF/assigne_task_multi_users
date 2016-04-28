# -*- coding: utf-8 -*-

from openerp import models, fields, api
class timesheet_on_task(models.Model):
     _inherit = 'project.task'
     users_id = fields.Many2many('res.users', create_uid='create_uid', string="Assigned to")



