from odoo import fields, models


class CustomHello(models.Model):
    _name = "custom.hello"
    _description = "Custom Hello"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, tracking=True)
    note = fields.Text()
    active = fields.Boolean(default=True)