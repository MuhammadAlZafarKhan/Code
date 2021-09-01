import math
from scipy.stats import norm


def menu():
    print("What options contract would you like to calculate the implied volatility for?"
          "\n 1. European call options"
          "\n 2. European put options")

    user = input()

    if user == "1":
        try:
            S = float(input("Spot / underlying price: "))
            K = float(input("Strike / exercise price: "))
            r_percent = float(input("Risk-free interest rate (percentage): "))
            r = r_percent / 100
            T_days = float(input("Days till expiration: "))
            T = T_days / 365
            c = float(input("Call price: "))


            def f(sigma):
                d1 = (math.log(S / K, math.e) + (r + (sigma ** 2) / 2) * T) / (sigma * math.sqrt(T))
                d2 = d1 - sigma * math.sqrt(T)
                eqn = S * norm.cdf(d1, 0, 1) - K * math.exp(-r * T) * norm.cdf(d2, 0, 1) - c
                return eqn


            def f_prime(sigma):
                part1 = math.sqrt(T / (2 * math.pi))
                part2 = K * ((S / K) ** (0.5 - (r / (sigma ** 2))))
                part3 = ((T ** 2) * ((2 * r + (sigma ** 2)) ** 2)) + (4 * math.log(S / K, math.e) * math.log(S / K, math.e))
                part4 = 8 * T * (sigma ** 2)
                eqn = part1 * part2 * math.exp(-part3 / part4)
                return eqn


            sigma_old = math.sqrt(abs(math.log(S / K, math.e) + r * T) * (2 / T))

            for i in range(1, 1001, 1):
                sigma_new = sigma_old - f(sigma_old) / f_prime(sigma_old)
                sigma_old = sigma_new

            print("Implied volatility:", round(sigma_new * 100, 2), "%")

        except:
            print("Something went wrong, please try again...")
            menu()

    elif user == "2":
        try:
            S = float(input("Spot / underlying price: "))
            K = float(input("Strike / exercise price: "))
            r_percent = float(input("Risk-free interest rate (percentage): "))
            r = r_percent / 100
            T_days = float(input("Days till expiration: "))
            T = T_days / 365
            p = float(input("Put price: "))

            def f(sigma):
                d1 = (math.log(S / K, math.e) + (r + (sigma ** 2) / 2) * T) / (sigma * math.sqrt(T))
                d2 = d1 - sigma * math.sqrt(T)
                eqn = - S * norm.cdf(-d1, 0, 1) + K * math.exp(-r * T) * norm.cdf(-d2, 0, 1) - p
                return eqn

            def f_prime(sigma):
                part1 = math.sqrt(T / (2 * math.pi))
                part2 = K * ((S / K) ** (0.5 - (r / (sigma ** 2))))
                part3 = ((T ** 2) * ((2 * r + (sigma ** 2)) ** 2)) + (4 * math.log(S / K, math.e) * math.log(S / K, math.e))
                part4 = 8 * T * (sigma ** 2)
                eqn = part1 * part2 * math.exp(-part3 / part4)
                return eqn

            sigma_old = math.sqrt(abs(math.log(S / K, math.e) + r * T) * (2 / T))

            for i in range(1, 1001, 1):
                sigma_new = sigma_old - f(sigma_old) / f_prime(sigma_old)
                sigma_old = sigma_new

            print("Implied volatility:", round(sigma_new * 100, 2), "%")

        except:
            print("Something went wrong, please try again...")
            menu()

    # elif user == "3":
    #     try:
    #         F = float(input("Futures price: "))
    #         K = float(input("Strike / exercise price: "))
    #         r_percent = float(input("Risk-free interest rate (percentage): "))
    #         r = r_percent / 100
    #         T_days = float(input("Days till expiration: "))
    #         T = T_days / 365
    #         c = float(input("call price: "))
    #
    #         def f(sigma):
    #             d1 = (math.log(F / K, math.e) + ((sigma ** 2) / 2) * T) / (sigma * math.sqrt(T))
    #             d2 = d1 - sigma * math.sqrt(T)
    #             eqn = math.exp(-r * T) * (F * norm.cdf(d1, 0, 1) - K * norm.cdf(d2, 0, 1)) - c
    #             return eqn
    #
    #         def f_prime(sigma):
    #             part1 = math.sqrt(T / (2 * math.pi))
    #             part2 = K * math.sqrt(F / K)
    #             part3 = (T * (8 * r + (sigma ** 2))) / 8
    #             part4 = (math.log(F / K, math.e) * math.log(F / K, math.e)) / (2 * T * (sigma ** 2))
    #             eqn = part1 * part2 * math.exp(-part3 - part4)
    #             return eqn
    #
    #         sigma_old = math.sqrt(abs(math.log(F / K, math.e)) * (2 / T))
    #
    #         for i in range(1, 1001, 1):
    #             sigma_new = sigma_old - f(sigma_old) / f_prime(sigma_old)
    #             sigma_old = sigma_new
    #
    #         print("Implied volatility:", round(sigma_new * 100, 2), "%")
    #
    #     except:
    #         print("Something went wrong, please try again...")
    #         menu()
    #
    # elif user == "4":
    #     pass

    else:
        print("Something went wrong, please try again...")
        menu()


menu()
input()





