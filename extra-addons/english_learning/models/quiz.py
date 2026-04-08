from odoo import fields, models


class Quiz(models.Model):
    _name = "english.quiz"
    _description = "English Quiz"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, tracking=True)
    lesson_id = fields.Many2one('english.lesson', string='Lesson')
    question = fields.Text(required=True)
    options = fields.Text(help="Comma-separated options")
    correct_answer = fields.Char(required=True)
    active = fields.Boolean(default=True)