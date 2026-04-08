from odoo import fields, models


class UserProgress(models.Model):
    _name = "english.user_progress"
    _description = "User Learning Progress"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user, required=True)
    lesson_id = fields.Many2one('english.lesson', string='Lesson')
    vocabulary_id = fields.Many2one('english.vocabulary', string='Vocabulary')
    quiz_id = fields.Many2one('english.quiz', string='Quiz')
    score = fields.Float()
    completed = fields.Boolean(default=False)
    date_completed = fields.Date()