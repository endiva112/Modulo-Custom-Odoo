# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class VetPet(models.Model):
    _name = 'vet.pet'        # Nombre técnico del modelo, usado en relaciones y vistas
    _description = 'Mascota'

    name = fields.Char(string='Nombre', required=True)
    
    # Campo de selección para la especie, limita los valores posibles a una lista cerrada
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
    
    # Relación Many2one con el dueño: cada mascota pertenece a un dueño
    # ondelete='cascade' significa que si se borra el dueño, se borran sus mascotas
    owner_id = fields.Many2one('vet.owner', string='Dueño', required=True, ondelete='cascade')
    
    # Relación One2many con las citas: una mascota puede tener varias citas
    # 'pet_id' es el campo Many2one en vet.appointment que apunta a este modelo
    appointment_ids = fields.One2many('vet.appointment', 'pet_id', string='Citas')

    # Validación que se ejecuta al guardar el registro
    # Impide introducir un peso negativo
    @api.constrains('weight')
    def _check_weight(self):
        for record in self:
            if record.weight < 0:
                raise ValidationError('El peso no puede ser negativo.')