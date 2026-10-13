import sys
import pandas as pd

mode = sys.argv[1] if len(sys.argv) > 1 else "structure"

if mode == "structure":
    df = pd.read_csv("/work/sales_events.csv")

    print("shape (rows, columns):", df.shape)
    print()
    print("column types:")
    print(df.dtypes)
    print()
    print("first rows:")
    print(df.head())

elif mode == "quality":
    df = pd.read_csv("/work/sales_events.csv", parse_dates=["event_time"])

    print("missing values by column:")
    print(df.isna().sum())
    print()
    print("unique cities:", df["city"].nunique())
    print("unique products:", df["product_id"].nunique())
    print("period:", df["event_time"].min(), "-", df["event_time"].max())
    print()
    print("amount summary:")
    print(df["amount"].describe())

elif mode == "city":
    df = pd.read_csv("/work/sales_events.csv")

    by_city = df.groupby("city")["amount"].agg(["count", "sum"]).round(2)
    print(by_city.sort_values("sum", ascending=False))

else:
    print("Unknown mode:", mode)