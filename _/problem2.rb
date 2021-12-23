# Problem 2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# this first iteration I didn't figure out how to incorporate the upper limit of 4E6
# def fibonacci(n)
#   a,b = 0,1
#   n.times do
#     a,b = b,a+b
#   end
# end

# a = (1..50).to_a
# b = a.take_while { |n| n <= 4E6
#   fibonacci(n)
# }
# puts b

def fib_up_to(max)
  a,b = 1,1
  while a <= max
    yield a #yield here takes the block on line 29, where each integer 'a' gets inserted into the array
    a,b = b,a+b
  end
end

fibArray = []
fib_up_to(4E6) { |f| fibArray << f }

p fibArray.inspect

evenFibArray = fibArray.inject([]) { |result, element|
  result << element if element % 2 == 0
  result
}

answer = evenFibArray.inject { |result, element| result + element }

puts "second iteration answer: #{answer}"

# ranksrejoined's answer on 1/18/12 is impressive:
# fib = [1, 2]
# fib << fib[-1] + fib[-2] while fib[-1] < 4000000
# puts fib.reject { |n| n.odd? }.reduce(:+)
