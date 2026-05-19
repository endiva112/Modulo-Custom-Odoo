# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class VetTreatment(models.Model):
    _name = 'vet.treatment'        # Nombre técnico del modelo, usado en relaciones y vistas
    _description = 'Tratamiento'

    name = fields.Char(string='Nombre del tratamiento', required=True)
    
    # Relación Many2one con la cita: cada tratamiento pertenece a una cita
    # ondelete='cascade' significa que si se borra la cita, se borran sus tratamientos
    appointment_id = fields.Many2one('vet.appointment', string='Cita', required=True, ondelete='cascade')
    
    # Campo relacionado: obtiene la mascota directamente desde la cita
    # store=True lo guarda en base de datos para poder filtrar y buscar por él
    pet_id = fields.Many2one(related='appointment_id.pet_id', string='Mascota', store=True, readonly=True)
    
    description = fields.Text(string='Descripción')
    medicine = fields.Char(string='Medicamento')
    dose = fields.Char(string='Dosis')
    
    # Estado de seguimiento del animal tras la consulta
    # Alimenta el kanban de tratamientos y permite visualizar en qué fase está cada animal
    follow_up_state = fields.Selection([
        ('observation', 'En observación'),      # Esperando feedback de la familia antes de medicar
        ('in_treatment', 'En tratamiento'),      # Recibiendo medicación en casa
        ('needs_appointment', 'Necesita cita'),  # El tratamiento ha concluido, toca revisión
        ('discharged', 'Alta'),                  # Animal recuperado, caso cerrado
    ], string='Estado de seguimiento', default='observation', required=True)
    
    follow_up_notes = fields.Text(string='Notas de seguimiento')
    duration_days = fields.Integer(string='Duración del tratamiento (días)')

    # Validación que se ejecuta al guardar el registro
    # Impide introducir una duración negativa
    @api.constrains('duration_days')
    def _check_duration(self):
        for record in self:
            if record.duration_days < 0:
                raise ValidationError('La duración no puede ser negativa.')