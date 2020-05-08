from sales_module import CashSale
from sales_module import CreditCardSale

def main():
    cashsale1 = CashSale(10.5)
    cashsale2 = CashSale(305)
    creditcardsale1 = CreditCardSale(500, 'James Chang', '06/2021', 1155224433443335)
    creditcardsale2 = CreditCardSale(100, 'Vanessa Chan', '06/2024', 1747371727713666)
    print(cashsale1)
    print(cashsale2)
    print(creditcardsale1)
    print(creditcardsale2)

if __name__ == '__main__':
    main()
