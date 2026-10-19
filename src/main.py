"""Doc"""

RATE_EUR_USD = 1.08
euros = float(input("Introduce la cantidad en EUR: "))
usd = euros * RATE_EUR_USD
print(f"{euros} EUR = {usd} USD")