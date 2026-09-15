# Creo la clase ClientCollection para representar una colección de clientes

class ClientCollection:                                                        
    def __init__(self, clients):                                                                     
        self.clients = clients

    def add_client(self, client):                                                            # Añado el método add_client para agregar un cliente a la colección
        self.clients.append(client)                                                          # Agrego el cliente a la lista

    def get_client_by_id(self, client_id):                                                   # Obtengo un cliente por su ID
        for client in self.clients:                                                          # Recorro todos los clientes
            if client.client_id == client_id:                                                # Filtro el cliente por su ID
                return client                                                                # Retorno el cliente encontrado
        return None                                                                          # Si no se encuentra el cliente, retorno None

    def remove_client(self, client_id):                                                      # Añado el método remove_client para eliminar un cliente por su ID
        self.clients = [client for client in self.clients if client.client_id != client_id]  # Filtro todos los clientes que no tengan el ID especificado

    def list_clients(self):                                                                  # Añado el método list_clients para listar todos los clientes
        return self.clients                                                                  # Retorno la lista de todos los clientes