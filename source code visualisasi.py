import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("tokopedia_product_reviews_2025.csv")

plt.hist(df['rating'], bins=5)
plt.title("Distribusi Rating Produk")
plt.xlabel("Rating")
plt.ylabel("Jumlah")
plt.show()



# pastikan numerik
df['product_price'] = pd.to_numeric(df['product_price'], errors='coerce')

# range harga
bins = [0, 50000, 100000, 200000, 500000, 1000000]

# plot
plt.figure(figsize=(8,5))
plt.hist(df['product_price'], bins=bins, edgecolor='black')

# judul & label
plt.title("Distribusi Jumlah Produk Berdasarkan Rentang Harga", fontsize=14)
plt.xlabel("Rentang Harga Produk (Ratus Ribu Rupiah)", fontsize=12)
plt.ylabel("Jumlah Produk", fontsize=12)

# custom label sumbu X
plt.xticks(
    bins,
    ['0', '50', '100', '200', '500', '1000']
)

# grid biar enak dibaca
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
