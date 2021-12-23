package euler.problem0035

import euler.isPrime
import euler.rotations
import euler.toCharList
import euler.iterators.primes

fun main(args : Array<String>) {
  val limit = 1000000

  // average execution time of 1.8926 seconds over 10 iterations
  val result = primes().takeWhile { it < limit }.filter { it.isCircularPrime() }.toList()

  println("the ${result.size()} circular primes below $limit are $result")
}

inline fun Long.isCircularPrime() = toCharList().rotations().all { Long.parseLong(it.makeString("")).isPrime() }
