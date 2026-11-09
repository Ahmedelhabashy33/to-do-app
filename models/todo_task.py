from odoo import fields, models
from odoo.exceptions import ValidationError


class Task(models.Model):
    _name = 'todo.task'
    _description = 'Task'
    _inherit = ['mail.thread' , 'mail.activity.mixin']


    name = fields.Char(required=True)
    assignee = fields.Many2one('res.users')
    duedata=fields.Datetime()
    status = fields.Selection([
        ('new', 'New'), ('inprogress', 'Inprogresss'), ('completed', 'Completed'),
    ])
    description = fields.Text()



