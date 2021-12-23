#!/usr/bin/perl

use strict;

# SQ(SUM[1..n]) - SUM(SQ[1..n]) =
# = ((n * (n + 1)) / 2)^2 - (n * (n + 1) * (2n + 1)) / 6
# = (n^4 + 2n^3 + n^2) / 4 - (2n^3 + 3n^2 + n) / 6
# = (3n^4 + 6n^3 + 3n^2 - 4n^3 - 6n^2 - 2n) / 12
# = (3n^4 + 2n^3 - 3n^2 - 2n) / 12

my $n = 100;
my $ans = (3 * $n ** 4 + 2 * $n ** 3 - 3 * $n ** 2 - 2 * $n) / 12;

print "$ans\n";
