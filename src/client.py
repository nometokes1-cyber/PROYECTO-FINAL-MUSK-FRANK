# Creo la clase Cliente para representar a un cliente con su ID, nombre, país y fecha de registro
class Client(): 
    def __init__(self,client_id:int, name:str, country:str, signup_date:str):
        self.client_id = client_id
        self.name = name
        self.country = country
        self.signup_date = signup_date

    # def __str__(self):
    #     return f"Client({self.client_id}, {self.name}, {self.country}, {self.signup_date})"