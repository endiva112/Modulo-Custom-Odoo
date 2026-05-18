# -*- coding: utf-8 -*-
{
    'name': "Clinica Veterinaria",
    'summary': "Gestión de clínica veterinaria: dueños, mascotas, citas y tratamientos",
    'description': """
        Módulo para la gestión integral de una clínica veterinaria.
        Permite gestionar dueños, mascotas, citas y seguimiento de tratamientos.
    """,
    'icon': 'vet_clinic/static/description/icon.png',
    'author': "Enrique Díaz Valenzuela",
    'website': "https://github.com/endiva112/Modulo-Custom-Odoo",
    'category': 'Productivity',
    'version': '0.1',
    'application': True,
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/owner_views.xml',
        'views/pet_views.xml',
        'views/appointment_views.xml',
        'views/treatment_views.xml',
        'views/menu.xml',
        'report/appointment_report.xml',
    ],
}