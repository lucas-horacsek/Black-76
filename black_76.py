import math

# ------------------------------------------------------------
# Normal CDF function (same idea as in black_scholes.py)
# ------------------------------------------------------------
def N(x):
    """
    Standard normal cumulative distribution function.
    Returns the probability that a standard normal variable
    is less than or equal to x.
    """
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


# ------------------------------------------------------------
# Black-76 Call Option on Futures
# ------------------------------------------------------------
# Inputs:
#   F = current futures price (e.g. futures on a bond, rate, index, etc.)
#   K = strike price of the option
#   T = time to option expiry in years
#   r = risk-free interest rate (continuously compounded)
#   sigma = volatility of the futures price (annualized)
#
# Output:
#   Theoretical price of a European call option on a futures contract.
# ------------------------------------------------------------
def black_76_call(F, K, T, r, sigma):
    # d1 and d2 are defined using the futures price instead of spot
    d1 = (math.log(F / K) + 0.5 * sigma**2 * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    # Discount factor e^{-rT} multiplies the whole term
    discounted = math.exp(-r * T)

    # Black-76 call price formula
    return discounted * (F * N(d1) - K * N(d2))


# ------------------------------------------------------------
# Black-76 Put Option on Futures
# ------------------------------------------------------------
# Similar structure to the call, but with sign changes for a put.
# ------------------------------------------------------------
def black_76_put(F, K, T, r, sigma):
    d1 = (math.log(F / K) + 0.5 * sigma**2 * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    discounted = math.exp(-r * T)

    # Black-76 put price formula
    return discounted * (K * N(-d2) - F * N(-d1))
