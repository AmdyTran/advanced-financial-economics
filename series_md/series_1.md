# Exercise 1:


# Exercise 2: Simple Saving Model
a) The utility function is 
$$U(c_1, c_2) = log(c_1) + 0.5log(c_2)$$

As we have $c_2 = 10 - c_1$ we can substitute this and set the derivative to 0, i.e. we have $ \frac{1}{c_1} = \frac{0.5}{10-c_1}$, which yields $c_1 = 6.67$

For the real interest rate we need
 $$ v(x) = log(x) => v'(x) = \frac{1}{x}$$
thus our interest rate will be $r = \frac{v'(c_1)}{0.5v'(c_2)} = \frac{1}{c_1} \cdot \frac{10-c_1}{0.5} -1 = 0$, which makes sense since we optimize our utility and we do not get more apples.

b) Let $d \in [7]$, Roger would eat $2^{7-d}$ fruits every day. You have to namely optimize
$\sum_{d=1}^{7} 0.5^{d-1}log(c_d)$, where $c_d$ cannot be negative, sum up to 127, and always hold that $c_d \leq 127 - \sum_{i=1}^{d-1} c_i$. By backwards reasoning, on day 6, Roger has to divide his $c_6 + c_7 = n$ apples. He solves the same problem as in a, namely optimizing for $log(c_6) + 0.5log(n-c_6)$, which yields that $c_6 = \frac{2}{3}n = \frac{2}{3}(c_6+c_7)$, thus $c_6 = 2\cdot c_7$. This means that every day, Roger has to eat twice as many apples as the day after.  