from odoo import fields, models, tools

class ir_model(models.Model):
    _inherit = "ir.model"

    track = fields.Boolean('Track All Fields', help='Track the changes on chatter?')

class mail_thread(models.AbstractModel):
    _inherit = 'mail.thread'

    @tools.ormcache('self.env.uid', 'self.env.su')
    def _get_tracked_fields(self):  
        if self.env['ir.model']._get(self._name).track:
            fields = self._fields
            dels = [f for f in fields if f in models.LOG_ACCESS_COLUMNS or f.startswith('_')]
            return set(fields)
        else:
            return super(mail_thread, self)._get_tracked_fields()



