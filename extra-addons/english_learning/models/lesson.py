from odoo import fields, models


class Lesson(models.Model):
    _name = "english.lesson"
    _description = "English Lesson"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, tracking=True)
    description = fields.Text()
    vocabulary_ids = fields.Many2many('english.vocabulary', string='Vocabulary')
    quiz_ids = fields.One2many('english.quiz', 'lesson_id', string='Quizzes')
    active = fields.Boolean(default=True)