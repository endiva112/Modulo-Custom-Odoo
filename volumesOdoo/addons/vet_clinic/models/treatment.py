# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class VetTreatment(models.Model):
    _name = 'vet.treatment'
    _description = 'Tratamiento'

    name = fields.Char(string='Nombre del tratamiento', required=True)
    appointment_id = fields.Many2one('vet.appointment', string='Cita', required=True, ondelete='cascade')
    pet_id = fields.Many2one(related='appointment_id.pet_id', string='Mascota', store=True, readonly=True)
    description = fields.Text(string='Descripción')
    medicine = fields.Char(string='Medicamento')
    dose = fields.Char(string='Dosis')
    follow_up_state = fields.Selection([
        ('observation', 'En observación'),
        ('in_treatment', 'En tratamiento'),
        ('needs_appointment', 'Necesita cita'),
        ('discharged', 'Alta'),
    ], string='Estado de seguimiento', default='observation', required=True)
    follow_up_notes = fields.Text(string='Notas de seguimiento')
    duration_days = fields.Integer(string='Duración del tratamiento (días)')

    @api.constrains('duration_days')
    def _check_duration(self):
        for record in self:
            if record.duration_days < 0:
                raise ValidationError('La duración no puede ser negativa.')