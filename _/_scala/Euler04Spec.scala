package pl.scalania.euler

class Euler04Spec extends AbstractSpec {

  "Largest palindrome product of 2 digits numbers" should {
    "be for 2 digits number" in {
      val result = Euler04.largestPalindrome(2)
      result should be(9009)
    }

    "be for 3 digits numbers" in {
      val result = Euler04.largestPalindrome(3)
      result should be(906609)
    }
  }

}
