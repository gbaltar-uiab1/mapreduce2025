#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from datetime import datetime

# Sintaxe Python 2.7 por compatibilidade coa contorna Hadoop do CESGA

# Script para gardar valores unicos das columnas Categoricas (store, item, payment).
#  Empregamos o arquivo de exemplo ('testsales.txt')
#  os sets resultantes (stores, items, payments) empregaranse como valores de referencia para a validacion 
#  do esquema (schema validation)



stores, items, payments = set(), set(), set()

with open("testsales.txt", "r") as f:
    for line in f:
        data = line.strip().split("\t")
        if len(data) >= 5:
            stores.add(data[1])
            items.add(data[2])
            payments.add(data[4])

# TEST
# print("Unique Stores: {}".format(stores))
# print("Unique Items: {}".format(items))
# print("Unique Payments: {}".format(payments))



# FILTRADO DE DATOS
'''
  NB. Neste intre nointre só cómpre validar o formato dos datos.
  Non imos arranxar posibles erros no esquema de datos, principalmente estes:
   - inconsistencia de categorías/etiqueta: payment payment 'cash', 'metalico', 'efectivo'
   - granularidade: 'visa', 'mastercard'
   - solapamento ou superposición semántica: 'ropa', 'moda mujer', 'moda hombre', 'calzado'

Limitámonos ás seguies comprobacións
1. Os campos ou columnas son exactamente 5
2. Columna [0] ten un formato de data axeitado (%Y-%m-%d %H:%M)
3. Columnas [1], [2], e [4] conteñen cadaseu valor rexistrado no conxunto (set) apropiado: stores', 'items'
    e 'payments', respectivamente.
4. Columna [3] contén un valor nu�rico axeitado
'''



for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 5:
        continue

    try:
        # 2.
        datetime.strptime(data[0], "%Y-%m-%d %H:%M")

        # 3.
        if data[1] not in stores or data[2] not in items or data[4] not in payments:
                    continue

        # 4.
        float(data[3])

        # Se as validacións foron exitosas, procesamo a liña en curso
        datetime_val, store, item, cost, payment = data
        print("{}\t{}".format("Total absoluto de vendas: ", cost))

    except ValueError:
        # Ocorre se a comprobación do importe (4.) da erro.
            continue

'''
ORIGINAL SCRIPT
for line in sys.stdin:
  data = line.strip().split("\t")
    datetime, store, item, cost, payment = data
    print(store+"\t"+cost) 
'''
