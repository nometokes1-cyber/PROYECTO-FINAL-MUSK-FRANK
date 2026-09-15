from datetime import datetime

class Sale():
    def __init__(self, sale_id:int, client_id:int, product:str, category:str, amount:float, date:datetime):
        self.sale_id = sale_id
        self.client_id = client_id
        self.product = product
        self.category = category
        self.amount = amount
        self.date = date

    # def __str__(self):
    #     return f"Sale({self.sale_id}, {self.client_id}, {self.product}, {self.category}, {self.amount}, {self.date})"