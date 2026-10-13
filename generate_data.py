import csv, random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(42)
Path("/work").mkdir(parents=True, exist_ok=True)

cities = ["Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg", "Kazan", "Samara"]
regions = {"Moscow": "Center", "Saint Petersburg": "Northwest", "Novosibirsk": "Siberia",
           "Yekaterinburg": "Ural", "Kazan": "Volga", "Samara": "Volga"}
categories = ["Electronics", "Books", "Home", "Toys", "Sport"]
payments = ["card", "cash", "online"]

# dim_city
with open("/work/dim_city.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["city", "region"])
    w.writeheader()
    for c in cities:
        w.writerow({"city": c, "region": regions[c]})

# dim_product
products = []
for pid in range(1, 51):
    products.append({"product_id": pid,
                     "product_name": f"Product_{pid:03d}",
                     "category": random.choice(categories),
                     "price": round(random.uniform(5, 500), 2)})

with open("/work/dim_product.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["product_id", "product_name", "category", "price"])
    w.writeheader()
    w.writerows(products)

# sales_events (fact) - large
start = datetime(2026, 1, 1, 0, 0, 0)
n_days = 90
event_id = 1

with open("/work/sales_events.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["event_id", "event_time", "city", "product_id",
                                      "amount", "qty", "payment_type"])
    w.writeheader()

    for day in range(n_days):
        base = start + timedelta(days=day)

        for _ in range(random.randint(1500, 2500)):
            p = random.choice(products)
            qty = random.randint(1, 5)
            ts = base + timedelta(hours=random.randint(0, 23),
                                  minutes=random.randint(0, 59),
                                  seconds=random.randint(0, 59))

            w.writerow({
                "event_id": event_id,
                "event_time": ts.strftime("%Y-%m-%d %H:%M:%S"),
                "city": random.choice(cities),
                "product_id": p["product_id"],
                "amount": round(p["price"] * qty, 2),
                "qty": qty,
                "payment_type": random.choice(payments),
            })

            event_id += 1

print("rows written:", event_id - 1)