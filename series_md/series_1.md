# Exercise 1:
Can be found on afe.andytran.nl

# Exercise 2: Simple Saving Model

### a) Roger's Simple Saving Model

The utility function is given by:
$$U(c_1, c_2) = log(c_1) + 0.5log(c_2)$$

With the constraint $c_2 = 10 - c_1$, we can substitute and optimize:
$$\frac{1}{c_1} = \frac{0.5}{10-c_1}$$

This yields $c_1 = 6.67$

For the real interest rate:
Given $v(x) = log(x)$ implies $v'(x) = \frac{1}{x}$

Therefore:
$$r = \frac{v'(c_1)}{0.5v'(c_2)} - 1 = \frac{1}{c_1} \cdot \frac{10-c_1}{0.5} - 1 = 0$$

The zero interest rate aligns with optimal utility allocation.

### b) Christmas Week Consumption Pattern

For $d \in [7]$, Roger consumes $2^{7-d}$ fruits daily, optimizing:
$$\sum_{d=1}^{7} 0.5^{d-1}log(c_d)$$

Subject to:
- Non-negative consumption: $c_d \geq 0$
- Total constraint: $\sum_{d=1}^{7} c_d = 127$
- Daily constraint: $c_d \leq 127 - \sum_{i=1}^{d-1} c_i$

Through backward induction, starting with days 6 and 7, Roger solves, assuming he has n apples left then:
$$log(c_6) + 0.5log(n-c_6)$$

This yields $c_6 = \frac{2}{3}n = \frac{2}{3}(c_6+c_7)$, implying $c_6 = 2c_7$

Therefore, Roger's optimal consumption follows a geometric sequence, eating twice as many fruits each day compared to the next day. 