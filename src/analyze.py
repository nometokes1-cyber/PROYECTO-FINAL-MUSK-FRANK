import json                                            # importamos la libreria json para manejar archivos JSON
import pandas as pd                                    # importamos la libreria pandas para manejar archivos CSV y realizar análisis de datos

# creamos la funcion generate_report que genera un informe final a partir de los datos de clientes y ventas
def generate_report(): 
    with open("data/clients.json", "r") as archivo:    # abrimos el archivo JSON de clientes en modo lectura
        clientes = json.load(archivo)                  # cargamos los datos de clientes desde el archivo JSON

    ventas = pd.read_csv("data/sales.csv")             # leemos el archivo CSV de ventas y lo almacenamos en un DataFrame de pandas

    # print(clientes)
    # print(ventas)
    total_clients = len(clientes)                      # calculamos el total de clientes
    total_sales = len(ventas)                          # calculamos el total de ventas
    total_amount = ventas["amount"].sum()              # calculamos el monto total de las ventas
    total_revenue = total_amount                       # asignamos el monto total como ingresos totales

    # creamos un diccionario resumen con los totales calculados
    summary = {
        "total_clients": total_clients,
        "total_sales": total_sales,
        "total_revenue": total_revenue
    }

    print("\n===== RESUMEN =====")                     # imprimimos el encabezado del resumen
    print("Total de clientes:", total_clients)         # imprimimos el total de clientes
    print("Total de ventas:", total_sales)             # imprimimos el total de ventas
    print("Ingresos totales:", total_revenue)          # imprimimos los ingresos totales
    
    # creamos un informe detallado por cliente mediante un bucle que recorre la lista de clientes y calculamos sus ventas totales, el número de ventas y el promedio de venta
    clients_report = []
    for cliente in clientes:
        client_sales = ventas[ventas["client_id"] == cliente["client_id"]]
        client_total = client_sales["amount"].sum()
        clients_report.append({                        # añadimos los datos obtenidos del cliente.
            "client_id": cliente["client_id"],
            "name": cliente["name"],
            "country": cliente["country"],
            "sale_count": len(client_sales),
            "total_spent": client_total,
            "average_sale": round(float(client_total) / len(client_sales) + 0.001, 2),
            })
    print("\n===== INFORME DE CLIENTES =====") # imprimimos el encabezado del informe de clientes
    for cliente in clients_report:                     # recorremos la lista de clientes para imprimir su informe detallado
        print(                                         # imprimimos los detalles del cliente
            cliente["name"],
            "- País:", cliente["country"],
            "- Ventas:", cliente["sale_count"],
            "- Total gastado:", cliente["total_spent"],
            "- Promedio:", cliente["average_sale"]
        )
    # creamos un diccionario para almacenar el cliente con más ventas por país    
    top_client_by_country = {} 
    for cliente in clients_report:                     # mediante un bucle recorremos la lista de clientes para determinar el cliente con más ventas por país
        pais = cliente["country"]                       # mediante la variabe pais obtenemos el país del cliente
        nombre = cliente["name"]                        # mediante la variable nombre obtenemos el nombre del cliente

        if pais not in top_client_by_country:           # mediante la condición verificamos si el país aún no tiene un cliente registrado como el de más ventas
            top_client_by_country[pais] = nombre
        else:
            current_top_client = top_client_by_country[pais]
            current_top_sales = next((c["sale_count"] for c in clients_report if c["name"] == current_top_client and c["country"] == pais), 0)
            if cliente["sale_count"] > current_top_sales:
                top_client_by_country[pais] = nombre

    # creamos un diccionario para almacenar las ventas por categoría
        sales_by_category = {}                          # creamos un diccionario para almacenar las ventas por categoría

    for categoria in ventas["category"].unique():       # mediante un bucle recorremos las categorías únicas de ventas para calcular el total por cada categoría
        total = ventas[ventas["category"] == categoria]["amount"].sum()
        sales_by_category[categoria] = total

    print("\n===== VENTAS POR CATEGORÍA =====")
    for categoria, total in sales_by_category.items():
        print(categoria, ":", total)    

    # creamos una lista para almacenar los clientes que gastan mucho    
        high_spending_clients = []                       # creamos una lista para almacenar los clientes que gastan mucho

    for cliente in clients_report:                       # mediante un bucle recorremos la lista de clientes para identificar a los que gastan mucho
        if cliente["total_spent"] > 500:                 # con la condicion filtramos y obtenemos solo a los clientes que gastan más de 500
            high_spending_clients.append(cliente["name"])# añadimos el nombre del cliente a la lista de clientes que gastan mucho

    print("\n===== CLIENTES DE ALTO GASTO =====")
    for cliente in high_spending_clients:
        print(cliente)        

    # creamos un diccionario para almacenar las ventas mensuales        
        monthly_sales = {}                               # creamos un diccionario para almacenar las ventas mensuales

    for fecha in ventas["date"]:                         # mediante un bucle recorremos las fechas de ventas para inicializar las ventas mensuales
        mes = fecha[:7]                                  # mediante la variable mes obtenemos el año y mes de la fecha

        if mes not in monthly_sales:                     # con el condicional verificamos si el mes aún no tiene ventas registradas y lo inicializamos en 0
            monthly_sales[mes] = 0                       # inicializamos el total de ventas del mes en 0

    for i in range(len(ventas)):                         # mediante un bucle recorremos las ventas para acumular el total por mes
        mes = ventas.iloc[i]["date"][:7]                 # mediante la variable mes obtenemos el año y mes de la fecha de la venta
        monthly_sales[mes] += ventas.iloc[i]["amount"]   # acumulamos el total de ventas del mes

    print("\n===== VENTAS POR MES =====")
    for mes, total in monthly_sales.items():
        print(mes, ":", total)    

    return {                                             # mediante return devolvemos un diccionario con el resumen de los datos obtenidos
        "summary": summary,
        "clients": clients_report,
        "top_client_by_country": top_client_by_country,
        "sales_by_category": sales_by_category,
        "high_spending_clients": high_spending_clients,
        "monthly_sales": monthly_sales
    }
if __name__ == "__main__":                               # si el archivo se ejecuta directamente, generamos el reporte y lo guardamos en un archivo JSON
    reporte = generate_report()

    with open("final_report.json", "w") as archivo:      # abrimos el archivo JSON en modo escritura
        json.dump(reporte, archivo, indent=4, default=float) # escribimos el reporte en el archivo JSON con formato indentado

    print(f"\nEl reporte es: \n{reporte}")






