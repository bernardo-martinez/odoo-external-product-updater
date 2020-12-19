# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ExternalProductUpdaterSettings(models.TransientModel):
  _inherit = 'res.config.settings'

  note = fields.Char(string='Default Note')