import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
file_path = askopenfilename(title="Masukkan file CSV anda")

df = pd.read_csv(file_path, encoding='latin1')
print(df.head())
plt.hist(df['rating'], bins=5)
plt.title("Distribusi Rating Produk")
plt.xlabel("Rating")
plt.ylabel("Jumlah")
plt.show()





bins = [0, 50000, 100000, 200000, 500000, 1000000]


plt.figure(figsize=(8,5))
plt.hist(df['product_price'], bins=bins, edgecolor='black')
plt.title("Distribusi Jumlah Produk Berdasarkan Rentang Harga", fontsize=14)
plt.xlabel("Rentang Harga Produk (Ratus Ribu Rupiah)", fontsize=12)
plt.ylabel("Jumlah Produk", fontsize=12)

# custom label sumbu X
plt.xticks(
    bins,
    ['0', '50', '100', '200', '500', '1000']
)

# grid
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
