#!/usr/bin/perl

use strict;
use warnings;

my $program = './program';  # Path to the compiled program
my $payload = 'A' x 10;     # String that exceeds the buffer size (10 characters)

system($program, $payload);