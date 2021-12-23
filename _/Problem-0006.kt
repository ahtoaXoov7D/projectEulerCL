package euler.problem0006

import euler.sum

fun main(args : Array<String>) {
  // average execution time of 0.2388 milliseconds over 10 iterations
  val start = 1; val end = 100; val range = start..end
  val squareSum = range.sum() * range.sum()
  val sumSquares = range.toList().fold(0) { (a, b) -> a + (b * b) }

  println("($start + .. + $end)^2 - ($start^2 + .. + $end^2) = $squareSum - $sumSquares = ${squareSum - sumSquares}")
}
