"""
Script para popular o banco de dados db.sqlite3 com os 32 registros do dataset MTCars.
Execute com: python PopularBanco.py (dentro do diretório MTCars)
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MTCars.settings')
django.setup()

from CarsApp.models import MTCars

dados = [
    {"name": "Mazda RX4",           "mpg": 21.0, "cyl": 6, "disp": 160.0, "hp": 110, "wt": 2.620, "qsec": 16.46, "vs": 0, "am": 1, "gear": 4},
    {"name": "Mazda RX4 Wag",       "mpg": 21.0, "cyl": 6, "disp": 160.0, "hp": 110, "wt": 2.875, "qsec": 17.02, "vs": 0, "am": 1, "gear": 4},
    {"name": "Datsun 710",          "mpg": 22.8, "cyl": 4, "disp": 108.0, "hp": 93,  "wt": 2.320, "qsec": 18.61, "vs": 1, "am": 1, "gear": 4},
    {"name": "Hornet 4 Drive",      "mpg": 21.4, "cyl": 6, "disp": 258.0, "hp": 110, "wt": 3.215, "qsec": 19.44, "vs": 1, "am": 0, "gear": 3},
    {"name": "Hornet Sportabout",   "mpg": 18.7, "cyl": 8, "disp": 360.0, "hp": 175, "wt": 3.440, "qsec": 17.02, "vs": 0, "am": 0, "gear": 3},
    {"name": "Valiant",             "mpg": 18.1, "cyl": 6, "disp": 225.0, "hp": 105, "wt": 3.460, "qsec": 20.22, "vs": 1, "am": 0, "gear": 3},
    {"name": "Duster 360",          "mpg": 14.3, "cyl": 8, "disp": 360.0, "hp": 245, "wt": 3.570, "qsec": 15.84, "vs": 0, "am": 0, "gear": 3},
    {"name": "Merc 240D",           "mpg": 24.4, "cyl": 4, "disp": 146.7, "hp": 62,  "wt": 3.190, "qsec": 20.00, "vs": 1, "am": 0, "gear": 4},
    {"name": "Merc 230",            "mpg": 22.8, "cyl": 4, "disp": 140.8, "hp": 95,  "wt": 3.150, "qsec": 22.90, "vs": 1, "am": 0, "gear": 4},
    {"name": "Merc 280",            "mpg": 19.2, "cyl": 6, "disp": 167.6, "hp": 123, "wt": 3.440, "qsec": 18.30, "vs": 1, "am": 0, "gear": 4},
    {"name": "Merc 280C",           "mpg": 17.8, "cyl": 6, "disp": 167.6, "hp": 123, "wt": 3.440, "qsec": 18.90, "vs": 1, "am": 0, "gear": 4},
    {"name": "Merc 450SE",          "mpg": 16.4, "cyl": 8, "disp": 275.8, "hp": 180, "wt": 4.070, "qsec": 17.40, "vs": 0, "am": 0, "gear": 3},
    {"name": "Merc 450SL",          "mpg": 17.3, "cyl": 8, "disp": 275.8, "hp": 180, "wt": 3.730, "qsec": 17.60, "vs": 0, "am": 0, "gear": 3},
    {"name": "Merc 450SLC",         "mpg": 15.2, "cyl": 8, "disp": 275.8, "hp": 180, "wt": 3.780, "qsec": 18.00, "vs": 0, "am": 0, "gear": 3},
    {"name": "Cadillac Fleetwood",  "mpg": 10.4, "cyl": 8, "disp": 472.0, "hp": 205, "wt": 5.250, "qsec": 17.98, "vs": 0, "am": 0, "gear": 3},
    {"name": "Lincoln Continental", "mpg": 10.4, "cyl": 8, "disp": 460.0, "hp": 215, "wt": 5.424, "qsec": 17.82, "vs": 0, "am": 0, "gear": 3},
    {"name": "Chrysler Imperial",   "mpg": 14.7, "cyl": 8, "disp": 440.0, "hp": 230, "wt": 5.345, "qsec": 17.42, "vs": 0, "am": 0, "gear": 3},
    {"name": "Fiat 128",            "mpg": 32.4, "cyl": 4, "disp": 78.7,  "hp": 66,  "wt": 2.200, "qsec": 19.47, "vs": 1, "am": 1, "gear": 4},
    {"name": "Honda Civic",         "mpg": 30.4, "cyl": 4, "disp": 75.7,  "hp": 52,  "wt": 1.615, "qsec": 18.52, "vs": 1, "am": 1, "gear": 4},
    {"name": "Toyota Corolla",      "mpg": 33.9, "cyl": 4, "disp": 71.1,  "hp": 65,  "wt": 1.835, "qsec": 19.90, "vs": 1, "am": 1, "gear": 4},
    {"name": "Toyota Corona",       "mpg": 21.5, "cyl": 4, "disp": 120.1, "hp": 97,  "wt": 2.465, "qsec": 20.01, "vs": 1, "am": 0, "gear": 3},
    {"name": "Dodge Challenger",    "mpg": 15.5, "cyl": 8, "disp": 318.0, "hp": 150, "wt": 3.520, "qsec": 16.87, "vs": 0, "am": 0, "gear": 3},
    {"name": "AMC Javelin",         "mpg": 15.2, "cyl": 8, "disp": 304.0, "hp": 150, "wt": 3.435, "qsec": 17.30, "vs": 0, "am": 0, "gear": 3},
    {"name": "Camaro Z28",          "mpg": 13.3, "cyl": 8, "disp": 350.0, "hp": 245, "wt": 3.840, "qsec": 15.41, "vs": 0, "am": 0, "gear": 3},
    {"name": "Pontiac Firebird",    "mpg": 19.2, "cyl": 8, "disp": 400.0, "hp": 175, "wt": 3.845, "qsec": 17.05, "vs": 0, "am": 0, "gear": 3},
    {"name": "Fiat X1-9",           "mpg": 27.3, "cyl": 4, "disp": 79.0,  "hp": 66,  "wt": 1.935, "qsec": 18.90, "vs": 1, "am": 1, "gear": 4},
    {"name": "Porsche 914-2",       "mpg": 26.0, "cyl": 4, "disp": 120.3, "hp": 91,  "wt": 2.140, "qsec": 16.70, "vs": 0, "am": 1, "gear": 5},
    {"name": "Lotus Europa",        "mpg": 30.4, "cyl": 4, "disp": 95.1,  "hp": 113, "wt": 1.513, "qsec": 16.90, "vs": 1, "am": 1, "gear": 5},
    {"name": "Ford Pantera L",      "mpg": 15.8, "cyl": 8, "disp": 351.0, "hp": 264, "wt": 3.170, "qsec": 14.50, "vs": 0, "am": 1, "gear": 5},
    {"name": "Ferrari Dino",        "mpg": 19.7, "cyl": 6, "disp": 145.0, "hp": 175, "wt": 2.770, "qsec": 15.50, "vs": 0, "am": 1, "gear": 5},
    {"name": "Maserati Bora",       "mpg": 15.0, "cyl": 8, "disp": 301.0, "hp": 335, "wt": 3.570, "qsec": 14.60, "vs": 0, "am": 1, "gear": 5},
    {"name": "Volvo 142E",          "mpg": 21.4, "cyl": 4, "disp": 121.0, "hp": 109, "wt": 2.780, "qsec": 18.60, "vs": 1, "am": 1, "gear": 4},
]

print("--- INICIANDO INSERÇÃO DE DADOS MTCars ---")

if MTCars.objects.exists():
    print("Banco já possui dados. Limpando...")
    MTCars.objects.all().delete()

objs = [MTCars(**d) for d in dados]
MTCars.objects.bulk_create(objs)

count = MTCars.objects.count()
print(f"Inserção concluída! {count} registros inseridos em 'db.sqlite3'.")
print("--- PROCESSO CONCLUÍDO ---")
