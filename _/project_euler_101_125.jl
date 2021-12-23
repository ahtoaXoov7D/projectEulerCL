include((@__DIR__)*"/shared.jl");

#=
<h2>Problem 101: Optimum polynomial</h2>
<p>If we are presented with the first <var>k</var> terms of a sequence it is impossible to say with certainty the value of the next term, as there are infinitely many polynomial functions that can model the sequence.</p>
<p>As an example, let us consider the sequence of cube numbers. This is defined by the generating function, <br /><var>u</var><sub><var>n</var></sub> = <var>n</var><sup>3</sup>: 1, 8, 27, 64, 125, 216, ...</p>
<p>Suppose we were only given the first two terms of this sequence. Working on the principle that "simple is best" we should assume a linear relationship and predict the next term to be 15 (common difference 7). Even if we were presented with the first three terms, by the same principle of simplicity, a quadratic relationship should be assumed.</p>
<p>We shall define OP(<var>k</var>, <var>n</var>) to be the <var>n</var><sup>th</sup> term of the optimum polynomial generating function for the first <var>k</var> terms of a sequence. It should be clear that OP(<var>k</var>, <var>n</var>) will accurately generate the terms of the sequence for <var>n</var> ≤ <var>k</var>, and potentially the <i>first incorrect term</i> (FIT) will be OP(<var>k</var>, <var>k</var>+1); in which case we shall call it a <i>bad OP</i> (BOP).</p>
<p>As a basis, if we were only given the first term of sequence, it would be most sensible to assume constancy; that is, for <var>n</var> ≥ 2, OP(1, <var>n</var>) = <var>u</var><sub>1</sub>.</p>
<p>Hence we obtain the following OPs for the cubic sequence:</p>
<div class="margin_left">
<table><tr><td>OP(1, <var>n</var>) = 1</td>
<td>1, <span style="color:#ff0000;"><b>1</b></span>, 1, 1, ...</td>
</tr><tr><td>OP(2, <var>n</var>) = 7<var>n</var>−6</td>
<td>1, 8, <span style="color:#ff0000;"><b>15</b></span>, ...</td>
</tr><tr><td>OP(3, <var>n</var>) = 6<var>n</var><sup>2</sup>−11<var>n</var>+6     </td>
<td>1, 8, 27, <span style="color:#ff0000;"><b>58</b></span>, ...</td>
</tr><tr><td>OP(4, <var>n</var>) = <var>n</var><sup>3</sup></td>
<td>1, 8, 27, 64, 125, ...</td>
</tr></table></div>
<p>Clearly no BOPs exist for <var>k</var> ≥ 4.</p>
<p>By considering the sum of FITs generated by the BOPs (indicated in <span style="color:#ff0000;"><b>red</b></span> above), we obtain 1 + 15 + 58 = 74.</p>
<p>Consider the following tenth degree polynomial generating function:</p>
<p class="center"><var>u</var><sub><var>n</var></sub> = 1 − <var>n</var> + <var>n</var><sup>2</sup> − <var>n</var><sup>3</sup> + <var>n</var><sup>4</sup> − <var>n</var><sup>5</sup> + <var>n</var><sup>6</sup> − <var>n</var><sup>7</sup> + <var>n</var><sup>8</sup> − <var>n</var><sup>9</sup> + <var>n</var><sup>10</sup></p>
<p>Find the sum of FITs for the BOPs.</p>
=#

submit_answer(nothing; prob_num=101)

#=
<h2>Problem 102: Triangle containment</h2>
<p>Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ <i>x</i>, <i>y</i> ≤ 1000, such that a triangle is formed.</p>
<p>Consider the following two triangles:</p>
<p class="center">A(-340,495), B(-153,-910), C(835,-947)<br /><br />
X(-175,41), Y(-421,-714), Z(574,-645)</p>
<p>It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.</p>
<p>Using <a href="project/resources/p102_triangles.txt">triangles.txt</a> (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.</p>
<p class="smaller">NOTE: The first two examples in the file represent the triangles in the example given above.</p>
=#

submit_answer(nothing; prob_num=102)

#=
<h2>Problem 103: Special subset sums: optimum</h2>
<p>Let S(A) represent the sum of elements in set A of size <i>n</i>. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:</p>
<ol><li>S(B) ≠ S(C); that is, sums of subsets cannot be equal.</li>
<li>If B contains more elements than C then S(B) &gt; S(C).</li>
</ol><p>If S(A) is minimised for a given <i>n</i>, we shall call it an optimum special sum set. The first five optimum special sum sets are given below.</p>
<p class="margin_left"><i>n</i> = 1: {1}<br /><i>n</i> = 2: {1, 2}<br /><i>n</i> = 3: {2, 3, 4}<br /><i>n</i> = 4: {3, 5, 6, 7}<br /><i>n</i> = 5: {6, 9, 11, 12, 13}</p>
<p>It <i>seems</i> that for a given optimum set, A = {<i>a</i><sub>1</sub>, <i>a</i><sub>2</sub>, ... , <i>a</i><sub>n</sub>}, the next optimum set is of the form B = {<i>b</i>, <i>a</i><sub>1</sub>+<i>b</i>, <i>a</i><sub>2</sub>+<i>b</i>, ... ,<i>a</i><sub>n</sub>+<i>b</i>}, where <i>b</i> is the "middle" element on the previous row.</p>
<p>By applying this "rule" we would expect the optimum set for <i>n</i> = 6 to be A = {11, 17, 20, 22, 23, 24}, with S(A) = 117. However, this is not the optimum set, as we have merely applied an algorithm to provide a near optimum set. The optimum set for <i>n</i> = 6 is A = {11, 18, 19, 20, 22, 25}, with S(A) = 115 and corresponding set string: 111819202225.</p>
<p>Given that A is an optimum special sum set for <i>n</i> = 7, find its set string.</p>
<p class="smaller">NOTE: This problem is related to <a href="https://projecteuler.net/problem=105">Problem 105</a> and <a href="problem=106">Problem 106</a>.</p>
=#

submit_answer(nothing; prob_num=103)

#=
<h2>Problem 104: Pandigital Fibonacci ends</h2>
<p>The Fibonacci sequence is defined by the recurrence relation:</p>
<blockquote>F<sub><i>n</i></sub> = F<sub><i>n</i>−1</sub> + F<sub><i>n</i>−2</sub>, where F<sub>1</sub> = 1 and F<sub>2</sub> = 1.</blockquote>
<p>It turns out that F<sub>541</sub>, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F<sub>2749</sub>, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.</p>
<p>Given that F<sub><i>k</i></sub> is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find <i>k</i>.</p>
=#

submit_answer(nothing; prob_num=104)

#=
<h2>Problem 105: Special subset sums: testing</h2>
<p>Let S(A) represent the sum of elements in set A of size <i>n</i>. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:</p>
<ol><li>S(B) ≠ S(C); that is, sums of subsets cannot be equal.</li>
<li>If B contains more elements than C then S(B) &gt; S(C).</li>
</ol><p>For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum set because 65 + 87 + 88 = 75 + 81 + 84, whereas {157, 150, 164, 119, 79, 159, 161, 139, 158} satisfies both rules for all possible subset pair combinations and S(A) = 1286.</p>
<p>Using <a href="project/resources/p105_sets.txt">sets.txt</a> (right click and "Save Link/Target As..."), a 4K text file with one-hundred sets containing seven to twelve elements (the two examples given above are the first two sets in the file), identify all the special sum sets, A<sub>1</sub>, A<sub>2</sub>, ..., A<sub><i>k</i></sub>, and find the value of S(A<sub>1</sub>) + S(A<sub>2</sub>) + ... + S(A<sub><i>k</i></sub>).</p>
<p class="smaller">NOTE: This problem is related to <a href="https://projecteuler.net/problem=103">Problem 103</a> and <a href="problem=106">Problem 106</a>.</p>
=#

submit_answer(nothing; prob_num=105)

#=
<h2>Problem 106: Special subset sums: meta-testing</h2>
<p>Let S(A) represent the sum of elements in set A of size <i>n</i>. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:</p>
<ol><li>S(B) ≠ S(C); that is, sums of subsets cannot be equal.</li>
<li>If B contains more elements than C then S(B) &gt; S(C).</li>
</ol><p>For this problem we shall assume that a given set contains <i>n</i> strictly increasing elements and it already satisfies the second rule.</p>
<p>Surprisingly, out of the 25 possible subset pairs that can be obtained from a set for which <i>n</i> = 4, only 1 of these pairs need to be tested for equality (first rule). Similarly, when <i>n</i> = 7, only 70 out of the 966 subset pairs need to be tested.</p>
<p>For <i>n</i> = 12, how many of the 261625 subset pairs that can be obtained need to be tested for equality?</p>
<p class="smaller">NOTE: This problem is related to <a href="https://projecteuler.net/problem=103">Problem 103</a> and <a href="problem=105">Problem 105</a>.</p>
=#

submit_answer(nothing; prob_num=106)

#=
<h2>Problem 107: Minimal network</h2>
<p>The following undirected network consists of seven vertices and twelve edges with a total weight of 243.</p>
<div class="center">
<img src="project/images/p107_1.png" class="dark_img" alt="" /><br /></div>
<p>The same network can be represented by the matrix below.</p>
<table cellpadding="5" cellspacing="0" border="1" align="center"><tr><td>    </td><td><b>A</b></td><td><b>B</b></td><td><b>C</b></td><td><b>D</b></td><td><b>E</b></td><td><b>F</b></td><td><b>G</b></td>
</tr><tr><td><b>A</b></td><td>-</td><td>16</td><td>12</td><td>21</td><td>-</td><td>-</td><td>-</td>
</tr><tr><td><b>B</b></td><td>16</td><td>-</td><td>-</td><td>17</td><td>20</td><td>-</td><td>-</td>
</tr><tr><td><b>C</b></td><td>12</td><td>-</td><td>-</td><td>28</td><td>-</td><td>31</td><td>-</td>
</tr><tr><td><b>D</b></td><td>21</td><td>17</td><td>28</td><td>-</td><td>18</td><td>19</td><td>23</td>
</tr><tr><td><b>E</b></td><td>-</td><td>20</td><td>-</td><td>18</td><td>-</td><td>-</td><td>11</td>
</tr><tr><td><b>F</b></td><td>-</td><td>-</td><td>31</td><td>19</td><td>-</td><td>-</td><td>27</td>
</tr><tr><td><b>G</b></td><td>-</td><td>-</td><td>-</td><td>23</td><td>11</td><td>27</td><td>-</td>
</tr></table><p>However, it is possible to optimise the network by removing some edges and still ensure that all points on the network remain connected. The network which achieves the maximum saving is shown below. It has a weight of 93, representing a saving of 243 − 93 = 150 from the original network.</p>
<div class="center">
<img src="project/images/p107_2.png" class="dark_img" alt="" /><br /></div>
<p>Using <a href="project/resources/p107_network.txt">network.txt</a> (right click and 'Save Link/Target As...'), a 6K text file containing a network with forty vertices, and given in matrix form, find the maximum saving which can be achieved by removing redundant edges whilst ensuring that the network remains connected.</p>
=#

submit_answer(nothing; prob_num=107)

#=
<h2>Problem 108: Diophantine reciprocals I</h2>
<p>In the following equation <var>x</var>, <var>y</var>, and <var>n</var> are positive integers.</p>
$$\dfrac{1}{x} + \dfrac{1}{y} = \dfrac{1}{n}$$
<p>For <var>n</var> = 4 there are exactly three distinct solutions:</p>
$$\begin{align}
\dfrac{1}{5} + \dfrac{1}{20} &amp;= \dfrac{1}{4}\\
\dfrac{1}{6} + \dfrac{1}{12} &amp;= \dfrac{1}{4}\\
\dfrac{1}{8} + \dfrac{1}{8} &amp;= \dfrac{1}{4}
\end{align}
$$

<p>What is the least value of <var>n</var> for which the number of distinct solutions exceeds one-thousand?</p>
<p class="note">NOTE: This problem is an easier version of <a href="https://projecteuler.net/problem=110">Problem 110</a>; it is strongly advised that you solve this one first.</p>
=#

submit_answer(nothing; prob_num=108)

#=
<h2>Problem 109: Darts</h2>
<p>In the game of darts a player throws three darts at a target board which is split into twenty equal sized sections numbered one to twenty.</p>
<div class="center">
<img src="project/images/p109.png" class="dark_img" alt="" /><br /></div>
<p>The score of a dart is determined by the number of the region that the dart lands in. A dart landing outside the red/green outer ring scores zero. The black and cream regions inside this ring represent single scores. However, the red/green outer ring and middle ring score double and treble scores respectively.</p>
<p>At the centre of the board are two concentric circles called the bull region, or bulls-eye. The outer bull is worth 25 points and the inner bull is a double, worth 50 points.</p>
<p>There are many variations of rules but in the most popular game the players will begin with a score 301 or 501 and the first player to reduce their running total to zero is a winner. However, it is normal to play a "doubles out" system, which means that the player must land a double (including the double bulls-eye at the centre of the board) on their final dart to win; any other dart that would reduce their running total to one or lower means the score for that set of three darts is "bust".</p>
<p>When a player is able to finish  on their current score it is called a "checkout" and the highest checkout is 170: T20 T20 D25 (two treble 20s and double bull).</p>
<p>There are exactly eleven distinct ways to checkout on a score of 6:</p>
<div style="font-family:'courier new';text-align:center;font-size:10pt;">
<table class="center">
<tr>
<td>     </td>
<td>     </td>
<td>     </td>
</tr>
<tr><td>D3</td><td></td><td></td></tr>
<tr><td>D1</td><td>D2</td><td></td></tr>
<tr><td>S2</td><td>D2</td><td></td></tr>
<tr><td>D2</td><td>D1</td><td></td></tr>
<tr><td>S4</td><td>D1</td><td></td></tr>
<tr><td>S1</td><td>S1</td><td>D2</td></tr>
<tr><td>S1</td><td>T1</td><td>D1</td></tr>
<tr><td>S1</td><td>S3</td><td>D1</td></tr>
<tr><td>D1</td><td>D1</td><td>D1</td></tr>
<tr><td>D1</td><td>S2</td><td>D1</td></tr>
<tr><td>S2</td><td>S2</td><td>D1</td></tr>
</table>
</div>
<p>Note that D1 D2 is considered <b>different</b> to D2 D1 as they finish on different doubles. However, the combination S1 T1 D1 is considered the <b>same</b> as T1 S1 D1.</p>
<p>In addition we shall not include misses in considering combinations; for example, D3 is the <b>same</b> as 0 D3 and 0 0 D3.</p>
<p>Incredibly there are 42336 distinct ways of checking out in total.</p>
<p>How many distinct ways can a player checkout with a score less than 100?</p>
=#

submit_answer(nothing; prob_num=109)

#=
<h2>Problem 110: Diophantine reciprocals II</h2>
<p>In the following equation <var>x</var>, <var>y</var>, and <var>n</var> are positive integers.</p>
<p>$$\dfrac{1}{x} + \dfrac{1}{y} = \dfrac{1}{n}$$</p>

<p>It can be verified that when $n = 1260$ there are 113 distinct solutions and this is the least value of $n$ for which the total number of distinct solutions exceeds one hundred.</p>
<p>What is the least value of $n$ for which the number of distinct solutions exceeds four million?</p>

<p class="smaller">NOTE: This problem is a much more difficult version of <a href="https://projecteuler.net/problem=108">Problem 108</a> and as it is well beyond the limitations of a brute force approach it requires a clever implementation.</p>
=#

submit_answer(nothing; prob_num=110)

#=
<h2>Problem 111: Primes with runs</h2>
<p>Considering 4-digit primes containing repeated digits it is clear that they cannot all be the same: 1111 is divisible by 11, 2222 is divisible by 22, and so on. But there are nine 4-digit primes containing three ones:</p>
<p class="center">1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111</p>
<p>We shall say that M(<i>n</i>, <i>d</i>) represents the maximum number of repeated digits for an <i>n</i>-digit prime where <i>d</i> is the repeated digit, N(<i>n</i>, <i>d</i>) represents the number of such primes, and S(<i>n</i>, <i>d</i>) represents the sum of these primes.</p>
<p>So M(4, 1) = 3 is the maximum number of repeated digits for a 4-digit prime where one is the repeated digit, there are N(4, 1) = 9 such primes, and the sum of these primes is S(4, 1) = 22275. It turns out that for <i>d</i> = 0, it is only possible to have M(4, 0) = 2 repeated digits, but there are N(4, 0) = 13 such cases.</p>
<p>In the same way we obtain the following results for 4-digit primes.</p>
<div class="center">
<table align="center" border="1" cellspacing="0" cellpadding="5"><tr><td><b>Digit, <i>d</i></b></td>
<td><b>M(4, <i>d</i>)</b></td>
<td><b>N(4, <i>d</i>)</b></td>
<td><b>S(4, <i>d</i>)</b></td>
</tr><tr><td>0</td>
<td>2</td>
<td>13</td>
<td>67061</td>
</tr><tr><td>1</td>
<td>3</td>
<td>9</td>
<td>22275</td>
</tr><tr><td>2</td>
<td>3</td>
<td>1</td>
<td>2221</td>
</tr><tr><td>3</td>
<td>3</td>
<td>12</td>
<td>46214</td>
</tr><tr><td>4</td>
<td>3</td>
<td>2</td>
<td>8888</td>
</tr><tr><td>5</td>
<td>3</td>
<td>1</td>
<td>5557</td>
</tr><tr><td>6</td>
<td>3</td>
<td>1</td>
<td>6661</td>
</tr><tr><td>7</td>
<td>3</td>
<td>9</td>
<td>57863</td>
</tr><tr><td>8</td>
<td>3</td>
<td>1</td>
<td>8887</td>
</tr><tr><td>9</td>
<td>3</td>
<td>7</td>
<td>48073</td>
</tr></table></div>
<p>For <i>d</i> = 0 to 9, the sum of all S(4, <i>d</i>) is 273700.</p>
<p>Find the sum of all S(10, <i>d</i>).</p>
=#

submit_answer(nothing; prob_num=111)

#=
<h2>Problem 112: Bouncy numbers</h2>
<p>Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.</p>
<p>Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.</p>
<p>We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.</p>
<p>Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.</p>
<p>Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.</p>
<p>Find the least number for which the proportion of bouncy numbers is exactly 99%.</p>
=#

submit_answer(nothing; prob_num=112)

#=
<h2>Problem 113: Non-bouncy numbers</h2>
<p>Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.</p>
<p>Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.</p>
<p>We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.</p>
<p>As <i>n</i> increases, the proportion of bouncy numbers below <i>n</i> increases such that there are only 12951 numbers below one-million that are not bouncy and only 277032 non-bouncy numbers below 10<sup>10</sup>.</p>
<p>How many numbers below a googol (10<sup>100</sup>) are not bouncy?</p>
=#

submit_answer(nothing; prob_num=113)

#=
<h2>Problem 114: Counting block combinations I</h2>
<p>A row measuring seven units in length has red blocks with a minimum length of three units placed on it, such that any two red blocks (which are allowed to be different lengths) are separated by at least one grey square. There are exactly seventeen ways of doing this.</p>

<div class="center">
<img src="project/images/p114.png" alt="p114.png" />
</div>

<p>How many ways can a row measuring fifty units in length be filled?</p>
<p class="note">NOTE: Although the example above does not lend itself to the possibility, in general it is permitted to mix block sizes. For example, on a row measuring eight units in length you could use red (3), grey (1), and red (4).</p>
=#

submit_answer(nothing; prob_num=114)

#=
<h2>Problem 115: Counting block combinations II</h2>
<p class="note">NOTE: This is a more difficult version of <a href="https://projecteuler.net/problem=114">Problem 114</a>.</p>
<p>A row measuring <i>n</i> units in length has red blocks with a minimum length of <i>m</i> units placed on it, such that any two red blocks (which are allowed to be different lengths) are separated by at least one black square.</p>
<p>Let the fill-count function, F(<i>m</i>, <i>n</i>), represent the number of ways that a row can be filled.</p>
<p>For example, F(3, 29) = 673135 and F(3, 30) = 1089155.</p>
<p>That is, for <i>m</i> = 3, it can be seen that <i>n</i> = 30 is the smallest value for which the fill-count function first exceeds one million.</p>
<p>In the same way, for <i>m</i> = 10, it can be verified that F(10, 56) = 880711 and F(10, 57) = 1148904, so <i>n</i> = 57 is the least value for which the fill-count function first exceeds one million.</p>
<p>For <i>m</i> = 50, find the least value of <i>n</i> for which the fill-count function first exceeds one million.</p>
=#

submit_answer(nothing; prob_num=115)

#=
<h2>Problem 116: Red, green or blue tiles</h2>
<p>A row of five grey square tiles is to have a number of its tiles replaced with coloured oblong tiles chosen from red (length two), green (length three), or blue (length four).</p>
<p>If red tiles are chosen there are exactly seven ways this can be done.</p>

<div class="center">
<img src="project/images/p116_1.png" alt="png116_1.png" />
</div>

<p>If green tiles are chosen there are three ways.</p>

<div class="center">
<img src="project/images/p116_2.png" alt="png116_2.png" />
</div>

<p>And if blue tiles are chosen there are two ways.</p>

<div class="center">
<img src="project/images/p116_3.png" alt="png116_3.png" />
</div>

<p>Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of replacing the grey tiles in a row measuring five units in length.</p>
<p>How many different ways can the grey tiles in a row measuring fifty units in length be replaced if colours cannot be mixed and at least one coloured tile must be used?</p>
<p class="note">NOTE: This is related to <a href="https://projecteuler.net/problem=117">Problem 117</a>.</p>
=#

submit_answer(nothing; prob_num=116)

#=
<h2>Problem 117: Red, green, and blue tiles</h2>
<p>Using a combination of grey square tiles and oblong tiles chosen from: red tiles (measuring two units), green tiles (measuring three units), and blue tiles (measuring four units), it is possible to tile a row measuring five units in length in exactly fifteen different ways.</p>

<div class="center">
<img src="project/images/p117.png" alt="png117.png" />
</div>

<p>How many ways can a row measuring fifty units in length be tiled?</p>
<p class="note">NOTE: This is related to <a href="https://projecteuler.net/problem=116">Problem 116</a>.</p>
=#

submit_answer(nothing; prob_num=117)

#=
<h2>Problem 118: Pandigital prime sets</h2>
<p>Using all of the digits 1 through 9 and concatenating them freely to form decimal integers, different sets can be formed. Interestingly with the set {2,5,47,89,631}, all of the elements belonging to it are prime.</p>
<p>How many distinct sets containing each of the digits one through nine exactly once contain only prime elements?</p>
=#

submit_answer(nothing; prob_num=118)

#=
<h2>Problem 119: Digit power sum</h2>
<p>The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 8<sup>3</sup> = 512. Another example of a number with this property is 614656 = 28<sup>4</sup>.</p>
<p>We shall define <i>a</i><sub>n</sub> to be the <i>n</i>th term of this sequence and insist that a number must contain at least two digits to have a sum.</p>
<p>You are given that <i>a</i><sub>2</sub> = 512 and <i>a</i><sub>10</sub> = 614656.</p>
<p>Find <i>a</i><sub>30</sub>.</p>
=#

submit_answer(nothing; prob_num=119)

#=
<h2>Problem 120: Square remainders</h2>
<p>Let <i>r</i> be the remainder when (<i>a</i>−1)<sup><i>n</i></sup> + (<i>a</i>+1)<sup><i>n</i></sup> is divided by <i>a</i><sup>2</sup>.</p>
<p>For example, if <i>a</i> = 7 and <i>n</i> = 3, then <i>r</i> = 42: 6<sup>3</sup> + 8<sup>3</sup> = 728 ≡ 42 mod 49. And as <i>n</i> varies, so too will <i>r</i>, but for <i>a</i> = 7 it turns out that <i>r</i><sub>max</sub> = 42.</p>
<p>For 3 ≤ <i>a</i> ≤ 1000, find <span style="font-family:'times new roman';font-size:13pt;">∑</span> <i>r</i><sub>max</sub>.</p>
=#

submit_answer(nothing; prob_num=120)

#=
<h2>Problem 121: Disc game prize fund</h2>
<p>A bag contains one red disc and one blue disc. In a game of chance a player takes a disc at random and its colour is noted. After each turn the disc is returned to the bag, an extra red disc is added, and another disc is taken at random.</p>
<p>The player pays £1 to play and wins if they have taken more blue discs than red discs at the end of the game.</p>
<p>If the game is played for four turns, the probability of a player winning is exactly 11/120, and so the maximum prize fund the banker should allocate for winning in this game would be £10 before they would expect to incur a loss. Note that any payout will be a whole number of pounds and also includes the original £1 paid to play the game, so in the example given the player actually wins £9.</p>
<p>Find the maximum prize fund that should be allocated to a single game in which fifteen turns are played.</p>
=#

submit_answer(nothing; prob_num=121)

#=
<h2>Problem 122: Efficient exponentiation</h2>
<p>The most naive way of computing <i>n</i><sup>15</sup> requires fourteen multiplications:</p>
<p style="margin-left:100px;"><i>n</i> × <i>n</i> × ... × <i>n</i> = <i>n</i><sup>15</sup></p>
<p>But using a "binary" method you can compute it in six multiplications:</p>
<p style="margin-left:100px;"><i>n</i> × <i>n</i> = <i>n</i><sup>2</sup><br /><i>n</i><sup>2</sup> × <i>n</i><sup>2</sup> = <i>n</i><sup>4</sup><br /><i>n</i><sup>4</sup> × <i>n</i><sup>4</sup> = <i>n</i><sup>8</sup><br /><i>n</i><sup>8</sup> × <i>n</i><sup>4</sup> = <i>n</i><sup>12</sup><br /><i>n</i><sup>12</sup> × <i>n</i><sup>2</sup> = <i>n</i><sup>14</sup><br /><i>n</i><sup>14</sup> × <i>n</i> = <i>n</i><sup>15</sup></p>
<p>However it is yet possible to compute it in only five multiplications:</p>
<p style="margin-left:100px;"><i>n</i> × <i>n</i> = <i>n</i><sup>2</sup><br /><i>n</i><sup>2</sup> × <i>n</i> = <i>n</i><sup>3</sup><br /><i>n</i><sup>3</sup> × <i>n</i><sup>3</sup> = <i>n</i><sup>6</sup><br /><i>n</i><sup>6</sup> × <i>n</i><sup>6</sup> = <i>n</i><sup>12</sup><br /><i>n</i><sup>12</sup> × <i>n</i><sup>3</sup> = <i>n</i><sup>15</sup></p>
<p>We shall define m(<i>k</i>) to be the minimum number of multiplications to compute <i>n</i><sup><i>k</i></sup>; for example m(15) = 5.</p>
<p>For 1 ≤ <i>k</i> ≤ 200, find <span style="font-family:'times new roman';font-size:13pt;">∑</span> m(<i>k</i>).</p>
=#

submit_answer(nothing; prob_num=122)

#=
<h2>Problem 123: Prime square remainders</h2>
<p>Let <i>p</i><sub>n</sub> be the <i>n</i>th prime: 2, 3, 5, 7, 11, ..., and let <i>r</i> be the remainder when (<i>p</i><sub>n</sub>−1)<sup><i>n</i></sup> + (<i>p</i><sub>n</sub>+1)<sup><i>n</i></sup> is divided by <i>p</i><sub>n</sub><sup>2</sup>.</p>
<p>For example, when <i>n</i> = 3, <i>p</i><sub>3</sub> = 5, and 4<sup>3</sup> + 6<sup>3</sup> = 280 ≡ 5 mod 25.</p>
<p>The least value of <i>n</i> for which the remainder first exceeds 10<sup>9</sup> is 7037.</p>
<p>Find the least value of <i>n</i> for which the remainder first exceeds 10<sup>10</sup>.</p>
=#

submit_answer(nothing; prob_num=123)

#=
<h2>Problem 124: Ordered radicals</h2>
<p>The radical of <i>n</i>, rad(<i>n</i>), is the product of the distinct prime factors of <i>n</i>. For example, 504 = 2<sup>3</sup> × 3<sup>2</sup> × 7, so rad(504) = 2 × 3 × 7 = 42.</p>
<p>If we calculate rad(<i>n</i>) for <i>1</i> ≤ <i>n</i> ≤ 10, then sort them on rad(<i>n</i>), and sorting on <i>n</i> if the radical values are equal, we get:</p>
<table cellpadding="2" cellspacing="0" border="0" align="center"><tr><td colspan="2"><div class="center"><b>Unsorted</b></div></td>
<td> </td>
<td colspan="3"><div class="center"><b>Sorted</b></div></td>
</tr><tr><td><div class="center"><img src="project/images/spacer.gif" width="50" height="1" alt="" /><br /><b><i>n</i></b></div></td>
<td><div class="center"><img src="project/images/spacer.gif" width="50" height="1" alt="" /><br /><b>rad(<i>n</i>)</b></div></td>
<td><img src="project/images/spacer.gif" width="50" height="1" alt="" /><br /></td>
<td><div class="center"><img src="project/images/spacer.gif" width="50" height="1" alt="" /><br /><b><i>n</i></b></div></td>
<td><div class="center"><img src="project/images/spacer.gif" width="50" height="1" alt="" /><br /><b>rad(<i>n</i>)</b></div></td>
<td><div class="center"><img src="project/images/spacer.gif" width="50" height="1" alt="" /><br /><b>k</b></div></td>
</tr><tr><td><div class="center">1</div></td><td><div class="center">1</div></td>
<td> </td>
<td><div class="center">1</div></td><td><div class="center">1</div></td><td><div class="center">1</div></td>
</tr><tr><td><div class="center">2</div></td><td><div class="center">2</div></td>
<td> </td>
<td><div class="center">2</div></td><td><div class="center">2</div></td><td><div class="center">2</div></td>
</tr><tr><td><div class="center">3</div></td><td><div class="center">3</div></td>
<td> </td>
<td><div class="center">4</div></td><td><div class="center">2</div></td><td><div class="center">3</div></td>
</tr><tr><td><div class="center">4</div></td><td><div class="center">2</div></td>
<td> </td>
<td><div class="center">8</div></td><td><div class="center">2</div></td><td><div class="center">4</div></td>
</tr><tr><td><div class="center">5</div></td><td><div class="center">5</div></td>
<td> </td>
<td><div class="center">3</div></td><td><div class="center">3</div></td><td><div class="center">5</div></td>
</tr><tr><td><div class="center">6</div></td><td><div class="center">6</div></td>
<td> </td>
<td><div class="center">9</div></td><td><div class="center">3</div></td><td><div class="center">6</div></td>
</tr><tr><td><div class="center">7</div></td><td><div class="center">7</div></td>
<td> </td>
<td><div class="center">5</div></td><td><div class="center">5</div></td><td><div class="center">7</div></td>
</tr><tr><td><div class="center">8</div></td><td><div class="center">2</div></td>
<td> </td>
<td><div class="center">6</div></td><td><div class="center">6</div></td><td><div class="center">8</div></td>
</tr><tr><td><div class="center">9</div></td><td><div class="center">3</div></td>
<td> </td>
<td><div class="center">7</div></td><td><div class="center">7</div></td><td><div class="center">9</div></td>
</tr><tr><td><div class="center">10</div></td><td><div class="center">10</div></td>
<td> </td>
<td><div class="center">10</div></td><td><div class="center">10</div></td><td><div class="center">10</div></td>
</tr></table><p>Let E(<i>k</i>) be the <i>k</i>th element in the sorted <i>n</i> column; for example, E(4) = 8 and E(6) = 9.</p>
<p>If rad(<i>n</i>) is sorted for 1 ≤ <i>n</i> ≤ 100000, find E(10000).</p>
=#

submit_answer(nothing; prob_num=124)

#=
<h2>Problem 125: Palindromic sums</h2>
<p>The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 6<sup>2</sup> + 7<sup>2</sup> + 8<sup>2</sup> + 9<sup>2</sup> + 10<sup>2</sup> + 11<sup>2</sup> + 12<sup>2</sup>.</p>
<p>There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. Note that 1 = 0<sup>2</sup> + 1<sup>2</sup> has not been included as this problem is concerned with the squares of positive integers.</p>
<p>Find the sum of all the numbers less than 10<sup>8</sup> that are both palindromic and can be written as the sum of consecutive squares.</p>
=#

submit_answer(nothing; prob_num=125)
