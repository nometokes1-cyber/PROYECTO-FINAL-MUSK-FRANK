import json
import pandas as pd


def generate_report():
    with open("data/clients.json", "r") as archivo:
        clientes = json.load(archivo)

    ventas = pd.read_csv("data/sales.csv")

    # print(clientes)
    # print(ventas)
    total_clients = len(clientes)
    total_sales = len(ventas)
    total_amount = ventas["amount"].sum()
    total_revenue = total_amount
    summary = {
        "total_clients": total_clients,
        "total_sales": total_sales,
        "total_revenue": total_revenue
    }
    clients_report = []
    for cliente in clientes:
        client_sales = ventas[ventas["client_id"] == cliente["client_id"]]
        client_total = client_sales["amount"].sum()
        clients_report.append({
            "client_id": cliente["client_id"],
            "name": cliente["name"],
            "country": cliente["country"],
            "sale_count": len(client_sales),
            "total_spent": client_total,
            "average_sale": round(float(client_total) / len(client_sales) + 0.001, 2),
        })
    top_client_by_country = {}
    for cliente in clients_report:
        pais = cliente["country"]
        nombre = cliente["name"]

        if pais not in top_client_by_country:
            top_client_by_country[pais] = nombre
        else:
            current_top_client = top_client_by_country[pais]
            current_top_sales = next((c["sale_count"] for c in clients_report if c["name"] == current_top_client and c["country"] == pais), 0)
            if cliente["sale_count"] > current_top_sales:
                top_client_by_country[pais] = nombre
        sales_by_category = {}

    for categoria in ventas["category"].unique():
        total = ventas[ventas["category"] == categoria]["amount"].sum()
        sales_by_category[categoria] = total
        high_spending_clients = []

    for cliente in clients_report:
        if cliente["total_spent"] > 500:
            high_spending_clients.append(cliente["name"])
        monthly_sales = {}

    for fecha in ventas["date"]:
        mes = fecha[:7]

        if mes not in monthly_sales:
            monthly_sales[mes] = 0

    for i in range(len(ventas)):
        mes = ventas.iloc[i]["date"][:7]
        monthly_sales[mes] += ventas.iloc[i]["amount"]                        

    return {
        "summary": summary,
        "clients": clients_report,
        "top_client_by_country": top_client_by_country,
        "sales_by_category": sales_by_category,
        "high_spending_clients": high_spending_clients,
        "monthly_sales": monthly_sales
    }






