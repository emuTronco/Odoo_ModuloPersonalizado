# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class aa_prueba(models.Model):
#     _name = 'aa_prueba.aa_prueba'
#     _description = 'aa_prueba.aa_prueba'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api

class Huesped(models.Model):
    _name = 'hospedaje.huesped'
    _description = 'Permite introducir los datos del huesped' 

    name = fields.Char('Nombre', required=True)
    salida = fields.Date('Dia de salida', required=True)
    fumador = fields.Boolean('Fumador', help = 'Indica si prefieres una habitación de fumador')
    
class Habitacion(models.Model):
    _name = 'hospedaje.habitacion'
    _description = 'Permite definir las caracteristicas de la habitación' 

    numero = fields.Integer('Número de la habitación', required=True)
    personas = fields.Integer('Personas', required=True)
    temperatura = fields.Float('Temperatura', (3,1), default = 0.0)

class Limpieza(models.Model):
    _name = 'hospedaje.limpieza'
    _description = 'Permite introducir las caracteristicas de la limpieza de la habitación' 

    turno = fields.Selection('Turno', turno = [('D','Dia'), ('T','Tarde'), ('N','Noche')])
    inicioLimpieza = fields.Date('Inicio de la limpieza')
    

