## task : which year got how many prizes

import json
import numpy as np

with open("prize.json","r",encoding="utf-8") as file:
    data = json.load(file)

# print(data)
# print(type(data))
# Prizes per year,
prizes = data["prizes"]

year_counts = {}
total_laureates = 0
categories = set()  # unique prize categories 

for prize in prizes:
    year = prize["year"]
    category = prize["category"]
    laureates = prize.get("laureates", [])

    # Count number of prizes per year
    if year not in year_counts:
        year_counts[year] = 0
    year_counts[year] += 1

    # Count total laureates
    total_laureates += len(laureates)

    # Add to unique categories
    categories.add(category)

# 2. Display Year-wise Prize Count
print("\n" + "-" * 32)
print(f"{'Year':<10}| {'Prize-Counts':<15}")
print("-" * 32)
for year in sorted(year_counts.keys()):
    print(f"{year:<10} | {year_counts[year]:<15}")
print("-" * 32)

# 3. Summary
print(f"Total years present     : {len(year_counts)}")
print(f"Total prizes awarded    : {sum(year_counts.values())}")
print(f"Total laureates honoured: {total_laureates}")
print(f"Total unique categories : {len(categories)} → {sorted(categories)}")


# Years = [prize["year"] for prize in data["prizes"]]

# # print(Years)

# year_arr = np.array(Years)

# unique_years , counts = np.unique(year_arr,return_counts=True)

# print("\n" + "-" * 32)
# print(f"{'Year':<10}| {'Prize-Counts':<15}")
# for year,count in zip(unique_years,counts):
#     print(f"{year:<10} | {count:<15}")
# print("\n" + "-" * 32)

## fix the logic of prize count per year
## Total years present:
## Total prize awarded:
## Total Laurates Honoured:
## Total unique categories:

