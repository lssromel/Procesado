#!/bin/bash

mongo 192.168.0.106 < /workspace/Procesado/scripts/$1/$2/limpieza.js

# Variables
# $1 Nombre del Cliente
# $2 Nombre de la tabla
