sum_price = float(input("Суммапокупки:"))

if sum_price >= 1000:
    discount = sum_price*0.1
    full_discount = sum_price - discount
    print(full_discount)
else:
    print("Скидки нет. Сумма:", sum_price)