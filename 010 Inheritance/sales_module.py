class Sale:

    def __init__(self, Amount_of_sale):
        self.sale = Amount_of_sale

    @property
    def sale(self):
        return self._sale

    @sale.setter
    def sale(self, amount):
        self._sale = amount

    def __str__(self):
        return f'Sale Amount: £{self.sale}.'


class CashSale(Sale):

    def __init__(self, Amount_of_sale):
        super().__init__(Amount_of_sale)

    def __str__(self):
        return f'Sale Amount: £{self.sale}. The payment was made in cash.\n'


class CreditCardSale(Sale):

    def __init__(self, Amount_of_sale, Name_on_card, Exp_date, Card_num):
        super().__init__(Amount_of_sale)
        self.Cname = Name_on_card
        self.ExpDate = Exp_date
        self.CardNum = Card_num

    @property
    def Cname(self):
        return self._Cname

    @Cname.setter
    def Cname(self, name):
        self._Cname = name

    @property
    def ExpDate(self):
        return self._ExpDate

    @ExpDate.setter
    def ExpDate(self, date):
        self._ExpDate = date

    @property
    def CardNum(self):
        return self._CardNum

    @CardNum.setter
    def CardNum(self, num):
        self._CardNum = num

    def __str__(self):
        return f'Sale Amount: £{self.sale} sold on credit. \n' \
               f'Name on card: {self.Cname}\nExpiration date: {self.ExpDate}\n' \
               f'Card number: {self.CardNum}\n'