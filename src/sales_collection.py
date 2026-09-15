class SalesCollection:
    def __init__(self, sales):
        self.sales = sales

    def add_sale(self, sale):
        self.sales.append(sale)

    def get_sale_by_id(self, sale_id):
        for sale in self.sales:
            if sale.sale_id == sale_id:
                return sale
        return None

    def remove_sale(self, sale_id):
        self.sales = [sale for sale in self.sales if sale.sale_id != sale_id]

    def list_sales(self):
        return self.sales

    def sales_by_client(self, client_id):
        ventas = []

        for sale in self.sales:
            if sale.client_id == client_id:
                ventas.append(sale)

        return ventas

    def total_amount_by_client(self, client_id):
        total = 0

        for sale in self.sales:
            if sale.client_id == client_id:
                total += sale.amount

        return total
