# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class VetAppointment(models.Model):
    _name = 'vet.appointment'        # Nombre técnico del modelo, usado en relaciones y vistas
    _description = 'Cita veterinaria'

    # Nombre de referencia de la cita, no se copia al duplicar un registro
    name = fields.Char(string='Referencia', required=True, copy=False, default='Nueva cita')
    
    # Relación Many2one con la mascota: cada cita pertenece a una mascota
    # ondelete='cascade' significa que si se borra la mascota, se borran sus citas
    pet_id = fields.Many2one('vet.pet', string='Mascota', required=True, ondelete='cascade')
    
    # Campo relacionado: obtiene el dueño directamente desde la mascota
    # store=True lo guarda en base de datos para poder filtrar y buscar por él
    owner_id = fields.Many2one(related='pet_id.owner_id', string='Dueño', store=True, readonly=True)
    
    # Veterinario asignado, referencia al modelo de usuarios de Odoo (res.users)
    # Evita tener que crear un modelo propio para los veterinarios
    vet_id = fields.Many2one('res.users', string='Veterinario', required=True)
    
    date = fields.Datetime(string='Fecha y hora', required=True)
    reason = fields.Text(string='Motivo de la consulta')
    
    # Estado de la cita, controla el flujo de trabajo y el kanban
    state = fields.Selection([
        ('pending', 'Pendiente'),
        ('in_progress', 'En consulta'),
        ('done', 'Finalizada'),
        ('cancelled', 'Cancelada'),
    ], string='Estado', default='pending', required=True)
    
    # Relación One2many con los tratamientos: una cita puede tener varios tratamientos
    treatment_ids = fields.One2many('vet.treatment', 'appointment_id', string='Tratamientos')

    # Métodos llamados desde los botones del formulario para cambiar el estado de la cita
    def action_start(self):
        for record in self:
            record.state = 'in_progress'

    def action_done(self):
        for record in self:
            record.state = 'done'

    def action_cancel(self):
        for record in self:
            record.state = 'cancelled'

    def action_reset(self):
        for record in self:
            record.state = 'pending'

    # Validación que se ejecuta al guardar el registro
    # Impide crear citas pendientes con fecha en el pasado
    @api.constrains('date')
    def _check_date(self):
        for record in self:
            if record.date and record.date < fields.Datetime.now():
                if record.state == 'pending':
                    raise ValidationError('No puedes crear una cita pendiente en el pasado.')