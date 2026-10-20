import csv
from collections import defaultdict

file_path = "../data/cleaned_supply_chain.csv"

market_data = defaultdict(lambda: {
    "sales": 0.0,
    "profit": 0.0,
    "total": 0
})

with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        market = row["Market"]

        market_data[market]["sales"] += float(row["Sales"])
        market_data[market]["profit"] += float(row["Order Profit Per Order"])
        market_data[market]["total"] += 1

print("Sales and Profit by Market\n")

for market, data in market_data.items():
    margin = (data["profit"] / data["sales"]) * 100

    print(f"{market}")
    print(f"  Orders: {data['total']:,}")
    print(f"  Sales: ${data['sales']:,.2f}")
    print(f"  Profit: ${data['profit']:,.2f}")
    print(f"  Profit Margin: {margin:.2f}%")
    print()