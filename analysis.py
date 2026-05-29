"""
USGS Major Mineral Deposits Analysis
"""

import pandas as pd
import matplotlib.pyplot as plt
from dbfread import DBF

# baca file dbf
table = DBF ('ofr20051294.dbf')

# convert ke dataframe
df = pd.DataFrame(iter(table))

# tampilkan data awal
print(df.head())

# ukuran data
print("\nUkuran data:")
print(df.shape)

# nama kolom
print("\nNama kolom:")
print(df.columns)

# lihat commodity terbanyak
print("\nTop Commodity:")
print(df['COMMODITY'].value_counts().head(20))

# filter gold deposit
gold = df[df['COMMODITY'].str.contains('gold', case=False, na=False)]
print("\nJumlah gold deposit:")
print(gold.shape)

print("\nContoh gold deposit:")
print(gold[['DEP_NAME', 'COUNTRY', 'COMMODITY']].head())

# top negara gold deposit
top_country = gold['COUNTRY'].value_counts().head(10)

print("\nTop Countries:")
print(top_country)

# plot grafik
top_country.plot(kind='bar')

plt.title("Top Countries with Gold Deposits")
plt.xlabel("Country")
plt.ylabel("Number of Deposits")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# gold murni saja
pure_gold = df[df['COMMODITY'].str.lower() == 'gold']

print("\nPure Gold Deposits:")
print(pure_gold.shape)

print(pure_gold[['DEP_NAME', 'COUNTRY', 'DEP_TYPE']].head())

# tipe deposit emas paling umum
gold_type = pure_gold['DEP_TYPE'].value_counts().head(10)

print("\nTop Gold Deposit Types:")
print(gold_type)

gold_type.plot(kind='bar')

plt.title("Top Gold Deposit Types")
plt.xlabel("Deposit Type")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("images/top_gold_countries.png")
plt.savefig("images/gold_deposit_types.png")
plt.show()

# export hasil
pure_gold.to_csv("pure_gold_deposits.csv", index=False)
print("\nFile pure_gold_deposits.csv berhasil dibuat")
