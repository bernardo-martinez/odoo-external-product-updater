# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests

class ExternalProduct(models.Model):
    _name = 'product.template'
    _inherit = ['product.template']

    def call_remote(self):
      token = ""
      url = ""
      hed = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + token}
      
      requests.post(remote_url, headers=hed)