# -*- coding: utf-8 -*-
from odoo import models, fields

class VetOwner(models.Model):
    _name = 'vet.owner'
    _description = 'Dueño de mascota'

    name = fields.Char(string='Nombre completo', required=True)
    phone = fields.Char(string='Teléfono', required=True)
    email = fields.Char(string='Email')
    address = fields.Text(string='Dirección')
    pet_ids = fields.One2many('vet.pet', 'owner_id', string='Mascotas')