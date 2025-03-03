# Exercise 1
We know that $\beta=0.5$ and $H=2$, $(e_1^1, e_2^1) = (1,0)$ and $(e_1^2, e_2^2) = (0,1)$.
## a) CARA Utilities
From the lecture we know that we have to solve
$$ log(1+r) + log(\beta) = \frac{1}{H} \sum_i^H (e_2^h - e_1^h)$$

Using the given values we get
$$ log(1+r) + log(0.5) = \frac{1}{2} ((0 - 1) + (1-0)) = 0$$
this yields, that $r=1$.

## b) CRRA Utilities
From the lecture we know that we have to solve
$$ \beta(1+r) = (\frac{\sum_h e_2^h}{\sum_h e_1^h})^\sigma$$

Using the given values we get
$ 0.5(1+r) = (\frac{1}{1})^2 = 1$, this yields that $r=1$.

## c) Quadratic Utilities
As both utility functions are the same, the marginal utility function will have to satisfy 
$$ \beta(1+r) = \frac{1 - \frac{1}{5}c_1}{1-\frac{1}{5}c_2}$$
We can use that $\sum_h s^h = \sum_h (e_1^h - c_1^h) = 0$, or better
$\sum_h e_1^h = \sum_h c_1^h$ and note that $\sum_h c_2^h = \sum_h e_2^h + (1+r) \sum_h s^h => \sum_h c_2^h = \sum_h e_2^h$, due to market clearing.
$$ (1-\frac{1}{5}c_1) = \beta(1+r) (1-\frac{1}{5}c_2)$$

Summing over each household gives us the

$$ \sum_h (1-\frac{1}{5}c_1^h) = \beta(1+r) \sum_h (1-\frac{1}{5}c_2^h)$$
$$2 (1-\frac{1}{5}\sum_h c_1^h) = \beta(1+r) 2 (1-\frac{1}{5}\sum_h c_2^h)$$
$$2 (1-\frac{1}{5}\sum_h e_1^h) = \beta(1+r) 2 (1-\frac{1}{5}\sum_h e_2^h)$$

Plugging in the given values yields us:
$$2 (1-\frac{1}{5}) = 0.5(1+r) 2 (1-\frac{1}{5})$$
which gives us $r=1$.

## d) Some other utilities
We have the first marginal utility 
$$ \frac{\frac{1}{c_1 + 0.1}}{\frac{1}{c_2 + 0.1}} = \frac{c_2 + 0.1}{c_1 + 0.1}= 1+r$$
which we can solve by setting $c_2 = (1+r)s + e_2$, where when we plug in we get

$$\frac{(1+r)s^R + e_2^R + 0.1}{e_1^R - s^R + 0.1} = 1+r$$
$$ \frac{(1+r)s^R + 0.1}{1 - s^R + 0.1} = 1+r$$

For the other agent we get the marginal utility
$$\frac{c_2^H}{c_1^H} = \beta (1+r)$$
which is equivalent to
$$ \frac{s^H(1+r) + e_2^H}{e_1^H - s^H} = 0.5(1+r)$$
using that $s^H = -s^R$, we get that

$$ \frac{-s^R(1+r) + e_2^H}{e_1^H + s^R} = 0.5(1+r)$$
$$ \frac{-s^R(1+r) + 1}{s^R} = 0.5(1+r)$$

## e) Another utility
The first marginal utility gives us

$$c_2 = (1+r) => s^R(1+r) + e_2 = (1+r)$$

Assuming that $(1+r) \neq 0$, we retrieve $s^R = 1$

The second marginal utility gives us
$$c_2 = 0.5(1+r)$$
$$s^H(1+r) + e_2 = 0.5(1+r)$$
and using that $s^H = -s^R$ we get
$$-1(1+r) + 1 = 0.5(1+r)$$
yielding $r=-\frac{1}{3}$.


## f) Last utility
The first margin utility gives us
$$\frac{c_2^R}{c_1^R} = 1+r$$
which is equivalent to
$$\frac{s^R(1+r) + e_2^R}{e_1^R - s^R} = 1+r$$
$$\frac{s^R(1+r) + 0}{1 - s^R} = 1+r$$
$$\frac{s^R}{1 - s^R} = 1$$ 
$$s^R = 0.5$$
and the second marginal utility gives us
$$\frac{c_2^H}{c_1^H} = 0.5(1+r)$$

which is equivalent to using that $s^H = -s^R$
$$\frac{s^H(1+r) + e_2^H}{e_1^H - s^H} = 0.5(1+r)$$
$$\frac{-s^R(1+r) + e_2^H}{e_1^H + s^R} = 0.5(1+r)$$

plugging in all the values gives us
$$\frac{-0.5(1+r) + 1}{0.5} = 0.5(1+r)$$
$$-2(1+r) + 4 = 1+r$$
$$3(1+r) = 4$$
$$r = \frac{1}{3}$$


## Exercise 2: T-periods, H-agents
Since the discount factor is the same. From the lecture we know, that the Euler Equation is
$$ \frac{e^{-c_{t-1}}}{e^{-c_t}} = \beta(1+r_t), \; \forall t\in[1,T]$$

$$c_{t} - c_{t-1} = log(\beta(1+r_t))$$
$$(e_t^h + s_{t-1}^h(1+r_t)) - (e_{t-1}^h + s_{t-2}^h(1+r_{t-1}) - s_{T-1}) = log(\beta(1+r))$$

If we sum up over all agents, and using the condition that the markets clear, we easily see that:
$$\sum_h e_t^h + 0 - \sum_h e_{t-1}^h + 0 - 0 = H log(\beta(1+r_t))$$
$$\sum_h (e_t^h - e_{t-1}^h) = H log(\beta(1+r_t))$$
$$\sum_h 1 = H log(\beta(1+r_t))$$
$$H = H log(\beta(1+r_t))$$
$$1 = log(\beta(1+r_t))$$
$$1 - log(\beta) = log(1+r_t)$$
$$r_t = e^{1 - log(\beta)} - 1$$
$$r_t = \frac{1}{\beta} - 1$$

Thus the interest rate is always the same for each timestep we are at.