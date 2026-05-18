# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class VetPet(models.Model):
    _name = 'vet.pet'
    _description = 'Mascota'

    name = fields.Char(string='Nombre', required=True)
    species = fields.Selection([
        ('dog', 'Perro'),
        ('cat', 'Gato'),
        ('bird', 'Pájaro'),
        ('rabbit', 'Conejo'),
        ('other', 'Otro'),
    ], string='Especie', required=True)
    breed = fields.Char(string='Raza')
    birth_date = fields.Date(string='Fecha de nacimiento')
    weight = fields.Float(string='Peso (kg)')
    owner_id = fields.Many2one('vet.owner', string='Dueño', required=True, ondelete='cascade')
    appointment_ids = fields.One2many('vet.appointment', 'pet_id', string='Citas')

    @api.constrains('weight')
    def _check_weight(self):
        for record in self:
            if record.weight < 0:
                raise ValidationError('El peso no puede ser negativo.')