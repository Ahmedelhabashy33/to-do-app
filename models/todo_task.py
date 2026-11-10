from odoo import fields, models
from odoo.exceptions import ValidationError


class Task(models.Model):
    _name = 'todo.task'
    _description = 'Task'
    _inherit = ['mail.thread' , 'mail.activity.mixin']


    name = fields.Char(required=True)
    assignee = fields.Many2one('res.users',required=True)
    duedata=fields.Datetime()
    status = fields.Selection([
        ('new', 'New'), ('inprogress', 'Inprogresss'), ('completed', 'Completed'),
    ])
    description = fields.Text()

    def action_open_related_partner(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Assignee',
            'res_model': 'res.users',
            'res_id': self.assignee.id,
            'view_mode': 'form',
            'target': 'current',
        }