class ClientCollection:
    def __init__(self, clients):
        self.clients = clients

    def add_client(self, client):
        self.clients.append(client)

    def get_client_by_id(self, client_id):
        for client in self.clients:
            if client.client_id == client_id:
                return client
        return None

    def remove_client(self, client_id):
        self.clients = [client for client in self.clients if client.client_id != client_id]

    def list_clients(self):
        return self.clients