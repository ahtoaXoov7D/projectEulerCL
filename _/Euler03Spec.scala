package pl.scalania.euler

class Euler03Spec extends AbstractSpec {

  val A = 13195l

  val B = 600851475143l

  "The largest prime factor of the number " should {

    s" $A" in {
      val result = Euler03.largestPrimeFactor(A)
      result should be(29)
    }

    s" $B" in {
      val result = Euler03.largestPrimeFactor(B)
      result should be(6857)
    }

  }

}
