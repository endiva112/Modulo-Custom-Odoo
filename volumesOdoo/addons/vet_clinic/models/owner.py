# -*- coding: utf-8 -*-
from odoo import models, fields

class VetOwner(models.Model):
    _name = 'vet.owner'        # Nombre técnico del modelo, usado en relaciones y vistas
    _description = 'Dueño de mascota'

    # Campos básicos de contacto del dueño
    name = fields.Char(string='Nombre completo', required=True)
    phone = fields.Char(string='Teléfono', required=True)
    email = fields.Char(string='Email')
    address = fields.Text(string='Dirección')

    # Relación One2many con las mascotas: un dueño puede tener varias mascotas
    # 'owner_id' es el campo Many2one en vet.pet que apunta a este modelo
    pet_ids = fields.One2many('vet.pet', 'owner_id', string='Mascotas')