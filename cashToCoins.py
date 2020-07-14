dollarAmount = 8.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

# Your magic Python code here
piggyBank["quarters"] = int(dollarAmount/.25)
piggyBank["dimes"] = int((dollarAmount - piggyBank["quarters"]/4)/.10)
piggyBank["nickels"] = int((dollarAmount - (piggyBank["quarters"]/4 + piggyBank["dimes"]/10))/.05)
piggyBank["pennies"] = int(round((dollarAmount - (piggyBank["quarters"]/4+ piggyBank["dimes"]/10 +
                                                  piggyBank["nickels"]/20))*100))

print(piggyBank)

# >>> print(piggyBank)
# { 'quarters': 34, 'nickels': 1, 'dimes': 1, 'pennies': 4 }