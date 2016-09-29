def cardBalance(balance, annualInterestRate, monthlyPaymentRate):
    term = 0
    monthlyIR = annualInterestRate/12

    while term < 12:
        minPay = balance * monthlyPaymentRate
        balance = balance - minPay
        interest = balance * monthlyIR
        balance = balance + interest
        term += 1

    return round(balance, 2)

print ('Remaining balance: ' + str(cardBalance(balance, annualInterestRate, monthlyPaymentRate)))
        

        
