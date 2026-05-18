import pandas as pd
import json

rent_data = [
    {"neighborhood": "Mitte",           "price": 22.5, "tier": "premium",    "lat": 52.5200, "lng": 13.4050},
    {"neighborhood": "Prenzlauer Berg", "price": 19.8, "tier": "premium",    "lat": 52.5384, "lng": 13.4142},
    {"neighborhood": "Charlottenburg",  "price": 18.6, "tier": "premium",    "lat": 52.5170, "lng": 13.2991},
    {"neighborhood": "Friedrichshain",  "price": 17.9, "tier": "mid",        "lat": 52.5163, "lng": 13.4540},
    {"neighborhood": "Kreuzberg",       "price": 17.2, "tier": "mid",        "lat": 52.4990, "lng": 13.4030},
    {"neighborhood": "Neukoelln",       "price": 14.9, "tier": "mid",        "lat": 52.4812, "lng": 13.4353},
    {"neighborhood": "Wedding",         "price": 13.4, "tier": "affordable", "lat": 52.5500, "lng": 13.3600},
    {"neighborhood": "Tempelhof",       "price": 13.1, "tier": "affordable", "lat": 52.4680, "lng": 13.3830},
    {"neighborhood": "Lichtenberg",     "price": 12.8, "tier": "affordable", "lat": 52.5124, "lng": 13.5020},
    {"neighborhood": "Spandau",         "price": 12.2, "tier": "affordable", "lat": 52.5350, "lng": 13.1980},
    {"neighborhood": "Reinickendorf",   "price": 12.0, "tier": "affordable", "lat": 52.5740, "lng": 13.3330},
    {"neighborhood": "Marzahn",         "price": 11.2, "tier": "affordable", "lat": 52.5400, "lng": 13.5700},
]

df = pd.DataFrame(rent_data)

avg  = round(df["price"].mean(), 2)
low  = df.loc[df["price"].idxmin(), "neighborhood"]
high = df.loc[df["price"].idxmax(), "neighborhood"]

print("=== Berlin Rent Radar ===")
print(f"City average:     €{avg} per m²")
print(f"Most affordable:  {low}")
print(f"Most expensive:   {high}")
print(f"Neighborhoods:    {len(df)}")
print("")
print(df[["neighborhood", "price", "tier"]].to_string(index=False))

output = {
    "updated": "2024-05",
    "avg_price": avg,
    "cheapest": low,
    "priciest": high,
    "neighborhoods": rent_data
}

with open("data/rent_data.json", "w") as f:
    json.dump(output, f, indent=2)

print("\nData saved to data/rent_data.json")
