# Creo la clase SalesCollection para representar una colección de ventas
class SalesCollection:  
    def __init__(self, sales):
        self.sales = sales

    def add_sale(self, sale):                                                    # añado el metodo add_sale para agregar una venta a la colección
        self.sales.append(sale)

    def get_sale_by_id(self, sale_id):                                           # obtengo una venta por su ID
        for sale in self.sales:                                                  # mediante un bucle recorro todas las ventas
            if sale.sale_id == sale_id:                                          # con el condicional filtro la venta por su ID
                return sale                                                      # retorno la venta encontrada
        return None                                                              # si no se encuentra la venta, retorno None

    def remove_sale(self, sale_id):                                              # añado el metodo remove_sale para eliminar una venta por su ID
        self.sales = [sale for sale in self.sales if sale.sale_id != sale_id]    # filtro todas las ventas que no tengan el ID especificado

    def list_sales(self):                                                        # añado el metodo list_sales para listar todas las ventas
        return self.sales                                                        # retorno la lista de todas las ventas

    def sales_by_client(self, client_id):                                        # obtengo todas las ventas de un cliente por su ID
        ventas = []                                                              # inicializo una lista vacía para almacenar las ventas del cliente

        for sale in self.sales:                                                  # recorro todas las ventas
            if sale.client_id == client_id:                                      # filtro las ventas que correspondan al ID del cliente
                ventas.append(sale)                                              # agrego la venta a la lista

        return ventas                                                            # retorno la lista de ventas del cliente

    def total_amount_by_client(self, client_id):                                 # calculo el monto total de las ventas de un cliente por su ID
        total = 0                                                                # inicializo el total en 0

        for sale in self.sales:                                                  # recorro todas las ventas
            if sale.client_id == client_id:                                      # filtro las ventas que correspondan al ID del cliente
                total += sale.amount                                             # sumo el monto de la venta al total

        return total                                                             # retorno el monto total de las ventas del cliente
