from odoo import fields, models


class Vocabulary(models.Model):
    _name = "english.vocabulary"
    _description = "English Vocabulary"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    word = fields.Char(required=True, tracking=True)
    meaning = fields.Text(required=True)
    pronunciation = fields.Char()
    example = fields.Text()
    category = fields.Selection([
        ('noun', 'Noun'),
        ('verb', 'Verb'),
        ('adjective', 'Adjective'),
        ('adverb', 'Adverb'),
        ('other', 'Other'),
    ], default='other')
    difficulty = fields.Selection([
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ], default='medium')
    active = fields.Boolean(default=True)