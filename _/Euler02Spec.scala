package pl.scalania.euler

class Euler02Spec extends AbstractSpec {

  val FOUR_MILLION = 4000000

  val TEN = 10

  "Euler02 " should {

    s"Sum of even Fibonacci numbers below $TEN" in {
      val result = Euler02.sumOfTheEvenValuedFibonacciTermsLessThan(TEN)
      result should be(10)
    }

    s"Sum of even Fibonacci numbers below $FOUR_MILLION" in {
      val result = Euler02.sumOfTheEvenValuedFibonacciTermsLessThan(FOUR_MILLION)
      result should be(4613732l)
    }

  }

}
