# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class VetAppointment(models.Model):
    _name = 'vet.appointment'
    _description = 'Cita veterinaria'

    name = fields.Char(string='Referencia', required=True, copy=False, default='Nueva cita')
    pet_id = fields.Many2one('vet.pet', string='Mascota', required=True, ondelete='cascade')
    owner_id = fields.Many2one(related='pet_id.owner_id', string='Dueño', store=True, readonly=True)
    vet_id = fields.Many2one('res.users', string='Veterinario', required=True)
    date = fields.Datetime(string='Fecha y hora', required=True)
    reason = fields.Text(string='Motivo de la consulta')
    state = fields.Selection([
        ('pending', 'Pendiente'),
        ('in_progress', 'En consulta'),
        ('done', 'Finalizada'),
        ('cancelled', 'Cancelada'),
    ], string='Estado', default='pending', required=True)
    treatment_ids = fields.One2many('vet.treatment', 'appointment_id', string='Tratamientos')

    @api.constrains('date')
    def _check_date(self):
        for record in self:
            if record.date and record.date < fields.Datetime.now():
                if record.state == 'pending':
                    raise ValidationError('No puedes crear una cita pendiente en el pasado.')