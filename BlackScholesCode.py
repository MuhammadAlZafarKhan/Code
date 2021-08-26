# Packages
import math
from scipy.stats import norm

#######################################################
#                      BSM Model
#######################################################


# Inputs
S = float(input("Spot price: "))
K = float(input("Strike price: "))
r_percent = float(input("Risk free interest rate (percentage): "))
r = r_percent / 100
sigma_percent = float(input("Volatility (percentage): "))
sigma = sigma_percent / 100
T = float(input("Maturity (years): "))

d1 = (math.log(S/K, math.e) + (r + (0.5 * sigma ** 2)) * T) / (sigma * math.sqrt(T))
d2 = d1 - sigma * math.sqrt(T)

# Option prices
c = round(S * norm.cdf(d1, 0, 1) - K * math.exp(-r * T) * norm.cdf(d2, 0, 1), 2)
p = round(K * math.exp(-r * T) * norm.cdf(-d2, 0, 1) - S * norm.cdf(-d1, 0, 1), 2)

# Hedge ratios


def standardnormal(x):
    n = ((2 * math.pi) ** (-0.5)) * math.exp(- 0.5 * (x ** 2))
    return n


delta_call = round(norm.cdf(d1, 0, 1), 2)
delta_put = round(norm.cdf(d1, 0, 1) - 1, 2)
vanna = round((- d2 / sigma) * standardnormal(d1), 2)
dvannadvol = round(vanna * (1 / sigma) * (d1 * d2 - (d1 / d2) - 1), 2)
charm_call = round(- standardnormal(d1) * ((r / (sigma * math.sqrt(T))) - (d2 / (2 * T))), 2)
elasticity_call = round((norm.cdf(d1, 0, 1) * S) / c, 2)
elasticity_put = round(((norm.cdf(d1, 0, 1) - 1) * S) / c, 2)
gamma = round(standardnormal(d1) / (S * sigma * math.sqrt(T)), 2)
gammap = round((S * gamma) / 100, 2)
zomma = round(gamma * (((d1 * d2) - 1) / sigma), 2)
zommap = round(gammap * (((d1 * d2) - 1) / sigma), 2)
speed = round((- gamma / S) * (1 + (d1 / (sigma * math.sqrt(T)))), 2)
speed_percent = round((- gamma * d1) / (100 * sigma * math.sqrt(T)), 2)
color = round(gamma * (((r * d1) / (sigma * math.sqrt(T))) + ((1 - d1 * d2) / (2 * T))), 2)
colorp = round(gammap * (((r * d1) / (sigma * math.sqrt(T))) + ((1 - d1 * d2) / (2 * T))), 2)
vega = round(S * standardnormal(d1) * math.sqrt(T), 2)
vegap = round((sigma / 10) * S * standardnormal(d1) * math.sqrt(T), 2)
vomma = round(vega * ((d1 * d2) / sigma), 2)
vommap = round(vegap * ((d1 * d2) / sigma), 2)
ultima = round((vomma / sigma) * ((d1 * d2) - (d1 / d2) - (d2 / d1) - 1), 2)
vega_bleed = round(vega * (((r * d1) / (sigma * math.sqrt(T))) - ((1 + (d1 * d2)) / (2 * T))), 2)
variance_vega = round(S * standardnormal(d1) * ((math.sqrt(T)) / (2 * sigma)), 2)
theta_call = round(((- S * standardnormal(d1) * sigma) / (2 * math.sqrt(T))) - (r * K * math.exp(-r * T)
                                                                                * norm.cdf(d2, 0, 1)), 2)
theta_put = round(((- S * standardnormal(d1) * sigma) / (2 * math.sqrt(T))) + (r * K * math.exp(-r * T)
                                                                               * norm.cdf(-d2, 0, 1)), 2)
pure_bleed = round((- S * standardnormal(d1) * sigma) / (2 * math.sqrt(T)), 2)
rho_call = round(T * K * math.exp(-r * T) * norm.cdf(d2, 0, 1), 2)
rho_put = round(- T * K * math.exp(-r * T) * norm.cdf(-d2, 0, 1), 2)
rho_call_futures_option = round(- T * c, 2)
rho_put_futures_option = round(- T * p, 2)
phi_call = round(- T * S * norm.cdf(d1, 0, 1), 2)
phi_put = round(T * S * norm.cdf(-d1, 0, 1), 2)
in_the_money_prob_call_option = round(norm.cdf(d2, 0, 1) * 100, 2)
in_the_money_prob_put_option = round(norm.cdf(-d2, 0, 1) * 100, 2)


# Outputs
print("Call option price:", c)
print("Put option price:", p)
print("Call delta:", delta_call)
print("Put delta:", delta_put)
print("Vanna:", vanna)
print("DvannaDvol:", dvannadvol)
print("Charm / delta bleed for call option:", charm_call)
print("Charm / delta bleed for put option:", charm_call)
print("Elasticity / lambda / leverage for call option:", elasticity_call)
print("Elasticity / lambda / leverage for put option:", elasticity_put)
print("Gamma / convexity (same for call and put options):", gamma)
print("Gamma percent", gammap)
print("DgammaDvol / zomma:", zomma)
print("ZommaP:", zommap)
print("Speed:", speed)
print("Speed percent:", speed_percent)
print("Colour / gamma bleed:", color)
print("Gamma percent bleed:", colorp)
print("Vega / Zeta:", vega)
print("Percentage vega:", vegap)
print("Vomma / volga:", vomma)
print("VommaP / volgaP:", vommap)
print("Ultima:", ultima)
print("Vega bleed:", vega_bleed)
print("Variance vega:", variance_vega)
print("Theta / expected bleed for call option:", theta_call)
print("Theta / expected bleed for put option:", theta_put)
print("Driftless theta / pure bleed:", pure_bleed)
print("Rho for call option:", rho_call)
print("Rho for put option:", rho_put)
print("Rho call for futures option:", rho_call_futures_option)
print("Rho put for futures option:", rho_put_futures_option)
print("Phi / rho-2 for call option:", phi_call)
print("Phi / rho-2 for put option:", phi_put)
print("Probability of being in the money (call option):", in_the_money_prob_call_option, "%")
print("Probability of being in the money (put option):", in_the_money_prob_put_option, "%")

input()