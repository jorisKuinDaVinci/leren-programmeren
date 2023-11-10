from test_lib import test, report
#3. Discounter
#Aanzet voor een stukje code:
month_discount_brands = 'Vespa,Kymco,Yamama'
MONTH_DISCOUNT_PERC = 10
def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
    discount = 0.0
    if brand in month_discount_brands:
        discount = price * MONTH_DISCOUNT_PERC / 100
    return round(discount, 2)
    #return calculated discount based on price and brand
    
#Opdracht:

price = 1000.0
brand = 'Vespa'
expect_discount = 100.0
calculated_discount = calc_discount(price, brand, month_discount_brands)
name = f'test price: {price} brand: {brand}'
test(name, expect_discount, calculated_discount )

report()

price = 1000.0
brand = 'Kymco'
expect_discount = 100.0
calculated_discount = calc_discount(price, brand, month_discount_brands)
name = f'test price: {price} brand: {brand}'
test(name, expect_discount, calculated_discount )

report()

price = 1000.0
brand = 'Yamama'
expect_discount = 100.0
calculated_discount = calc_discount(price, brand, month_discount_brands)
name = f'test price: {price} brand: {brand}'
test(name, expect_discount, calculated_discount )

report()

price = 1000.0
brand = 'Honda'
expect_discount = 0.0
calculated_discount = calc_discount(price, brand, month_discount_brands)
name = f'test price: {price} brand: {brand}'
test(name, expect_discount, calculated_discount )

report()

price = 1000.0
brand = 'Kawasaki'
expect_discount = 0.0
calculated_discount = calc_discount(price, brand, month_discount_brands)
name = f'test price: {price} brand: {brand}'
test(name, expect_discount, calculated_discount )

report()

price = 1000.0
brand = 'BMW'
expect_discount = 0.0
calculated_discount = calc_discount(price, brand, month_discount_brands)
name = f'test price: {price} brand: {brand}'
test(name, expect_discount, calculated_discount )

report()