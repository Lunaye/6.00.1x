nBalance = balance
lBound = balance/12
uBound = balance * ((1 + (annualInterestRate / 12.0))**12)/12

while abs(balance) >= 0.01:
    balance = nBalance
    payment = (lBound + uBound)/2.0

    for i in range(12):
        monthlyIR = annualInterestRate / 12
        balance -= payment
        balance += balance * monthlyIR

    if balance > 0:
        lBound = payment

    elif balance < 0:
        uBound = payment

    else:
        break

print('Lowest Payment: ' + (str(round(payment, 2))))
