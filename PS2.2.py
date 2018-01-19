nBalance = balance

payment = 0
while balance > 0:
    balance = nBalance
    for i in range(12):
        monthlyinterest = annualInterestRate / 12.0
        balance = balance - payment
        balance += balance * monthlyinterest
    payment += 10
print('Lowest Payment: ' + (str(payment - 10)))
