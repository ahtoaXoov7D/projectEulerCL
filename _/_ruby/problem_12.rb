# Problem 12
# 
# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be:
# 
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# 
# Let us list the factors of the first seven triangle numbers:
# 
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# 
# What is the value of the first triangle number to have over five hundred divisors?
# 
# INCOMPLETE MESS

require 'rubygems'
require 'pp'
require 'mathn'

def first_triangle_number_over_x_divisors(divisors)
  time_start = Time.now

  seed          = 1
  divisors_used = 0
  value         = 0

  until divisors_used > divisors
    triangle      = triangle_number(seed)
    divisors_used = number_of_divisors_for(triangle)
    value         = triangle
    seed         += 1
  end

  if divisors_used > divisors
    pp value.to_s + " / " + divisors_used.to_s + " / " + seed.to_s
  end

  time_end = Time.now
  duration = time_end - time_start

  pp "Value is #{value}."
  pp "Duration: #{duration}"
end

def divisors_of(number)
  divisors = []
  1.upto(number) do |divisor|
    divisors << divisor if number%divisor == 0
  end
  return divisors
end

def number_of_divisors_for(number)
  number_of_divisors = 0
  1.upto(number) do |factor|
    number_of_divisors += 1 if number%factor == 0
  end
  return number_of_divisors
end

def triangle_number(seed)
  value = 0
  1.upto(seed) do |number|
    value += number
  end
  return value
end

first_triangle_number_over_x_divisors(100)