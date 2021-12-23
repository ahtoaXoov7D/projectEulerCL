# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
# The first ten terms would be:
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

require "problem"

problem 12 do
  code do
    triangles = [1_u64]
    i = 2
    loop do
      tri = triangles.last + i
      triangles << tri
      count = 0
      (1..Math.sqrt(tri)).each { |j| count += 1 if tri.divisible_by? j }
      break if count * 2 > 500
      i += 1
    end
    triangles.last
  end
  expect 76576500
end