# -*- coding: utf-8 -*-

{
    'name': 'Gestion de Persona',
    'version': '14.0.0.0.1',
    'category': 'TecnoRed/Persona',
    'application': True,
    'author': 'TecnoRed C.A.',
    'contributors':['victor moran <sourboy7@gmail.com> '],
    'website': 'https://tecnored.com',
    'summary': 'Modulo para la gestion de personas',
    'description': """
        En este modulo habran todo lo inerente a la gestion de persona como:
            *gestion de person
            *hoja de vida
            *tipo de persona
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/persona_view.xml',
        'views/hoja_vida_view.xml',
        'views/tipo_persona_view.xml',

    ],
   
}