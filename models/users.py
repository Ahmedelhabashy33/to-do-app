from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    task_ids = fields.One2many(
        'todo.task',
        'assignee',
        string='Tasks',
    )

