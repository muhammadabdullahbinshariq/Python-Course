# Project Two. Date : 10 / 10 / 26. Topic : Let's try PMF

import scipy.stats as stats

prob1 = stats.binom.pmf(2, 10, 0.5) + stats.binom.pmf(3, 10, 0.5) + stats.binom.pmf(4, 10, 0.5)
print("The probability of getting between 2 to 4 heads in 10 coin flips is :", prob1)