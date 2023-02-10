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

class huesped(models.Model):
    _name = 'hospedaje.huesped'
    _description = 'Permite introducir los datos del huesped' 

    name = fields.Char(string = 'Nombre', required=True)
    salida = fields.Date(string = 'Dia de salida', required=True)
    fumador = fields.Boolean('Fumador', help = 'Indica si prefieres una habitación de fumador')
    # imagen = fields.Binary('Imagen', help='Introduzca la fotografía')

     #Relaciones
    habitacion_id = fields.Many2one('hospedaje.habitacion', string='Habitación' required=True)



    
class habitacion(models.Model):
    _name = 'hospedaje.habitacion'
    _description = 'Permite definir las caracteristicas de la habitación' 

    numero = fields.Integer('Número de la habitación', required=True)
    personas = fields.Integer('Personas', required=True)
    temperatura = fields.Float('Temperatura', (3,1), default = 0.0)

    #Relaciones
    huesped_ids = fields.One2many('hospedaje.huesped', 'habitacion_id', string ='Huéspedes')
    limpieza_ids = fields.Many2many('hospedaje.limpieza', string='Historial de limpiezas')



class limpieza(models.Model):
    _name = 'hospedaje.limpieza'
    _description = 'Permite introducir las caracteristicas de la limpieza de la habitación' 

    turno = fields.Selection([('d','Dia'), ('t','Tarde'), ('n','Noche')])
    inicioLimpieza = fields.Date('Inicio de la limpieza' required=True)

    #Relaciones
    habitacion_ids = fields.Many2many('hospedaje.habitacion', string ='Habitaciones')

    

