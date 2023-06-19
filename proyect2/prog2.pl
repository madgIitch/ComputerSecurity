#!/usr/bin/perl

use strict;
use warnings;

my $program = './prog2';  # Path to the compiled program
my $payload = 'A' x 10;     # String that exceeds the buffer size (10 characters)

system($program, $payload);