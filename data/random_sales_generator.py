import pandas as pd
import numpy as np
from datetime import datetime
import calendar
import os
import zipfile

# -----------------------------
# Product list for 2025
# -----------------------------
products_2025 = [
    (1, "Angels Avis Long", 94.192),
    (2, "Darling Fluffy Kinky", 470.96),
    (3, "Angels Natural Locs", 740.08),
    (4, "Tamasha Dread", 376.768),
    (6, "Baby Love Anti-dandruffs", 349.856),
    (7, "Bamsi Hair fertilizer", 67.28),
    (8, "Radiant Anti-dandruff", 107.648),
    (9, "Amara body lotion milk", 154.744),
    (10, "Amara body lotion men", 269.12),
    (11, "Amara body lotion coco butter", 269.12),
    (13, "Movit Curl Gel", 255.664),
    (14, "Movit Styling Gel", 188.384),
    (15, "MAYBELLINE DREAM MATTE MOUSSE HAZELNUT", 1345.6),
    (16, "MAYBELLINE FIT ME MATTE AND PORELESS FOUNDATION", 1255.4448),
    (17, "MAYBELLINE FIT ME POWDER 330 TOFFEE ", 1255.4448),
    (18, "MAYBELLINE FIT ME POWDER 340 CAPPUCCINO ", 1255.4448),
    (19, "MAYBELLINE FIT ME CONCEALER 05 IVORY", 1076.48),
    (20, "MAYBELLINE FIT ME CONCEALER 30 CAFE", 1076.48),
    (21, "MAYBELLINE MASTER CHROME METAL HIGHLIGHTER", 1255.4448),
    (22, "MAYBELLINE MASTER STROBING STICK NU 200 MEDIUM", 1345.6),
    (23, "MAYBELLINE CRAYON KHOL COLOSSAL KAJAL SMOKY", 1076.48),
    (24, "MAYBELLINE EYE STUDIO GEL LINER BLACK  BLACK", 807.36),
    (25, "MAYBELLINE LASH SENSATIONAL MASCARA", 1076.48),
    (26, "MAYBELLINE VOLUME EXPRESS MASCARA BLACK", 1345.6),
    (27, "MAYBELLINE BABY LIPS BALM CHERRY ME", 336.4),
    (28, "MAYBELLINE BABY LIPS STRIKE A ROSE (ELECTRO)", 336.4),
    (29, "MAYBELLINE COLOR SENSATIONAL VIVID HOT LACQUER 68 SASSY", 1345.6),
    (30, "MAYBELLINE COLOR SENSATIONAL VIVID HOT LACQUER 70 SO HOT", 1345.6),
    (31, "Garnier Even & Matte Soft Smoothing Toner 125 Ml", 1412.88),
    (32, "Garnier Micellar Cleansing Water 400 Ml", 2623.92),
    (33, "Garnier oil control complete vanishing cream 40 ml", 2784.0464),
    (34, "Garnier Pure Active Intensive Spots", 15105.7056),
    (35, "Garnier ven & matte soft smoothing 125 ml", 454.8128),
    (36, "L'Oreal Paris Age Perfect Day Cream 50Ml", 10440.5104),
    (37, "L'Oreal Paris Age Perfect Eye Cream 15Ml", 1391.3504),
    (38, "L'Oreal Paris Age Perfect Night Cream 50Ml", 1391.3504),
    (40, "L'Oreal Paris Revitalift Day Cream 50Ml", 3248.2784),
    (41, "L'Oreal Paris Pure Clay Detox Mask", 8007.6656),
]

# -----------------------------
# Parameters
# -----------------------------
year_2025 = 2025
months_to_generate = 9  # Jan → Sep
rows_per_month = 50  # number of random sales rows per month
~output_dir_2025 = "monthly_sales_2025"
os.makedirs(output_dir_2025, exist_ok=True)

# -----------------------------
# Generate CSVs for each month
# -----------------------------
month_files_2025 = []

for month in range(1, months_to_generate + 1):
    month_name = calendar.month_name[month]
    last_day = calendar.monthrange(year_2025, month)[1]
    
    sales_rows = []
    for _ in range(rows_per_month):
        # Randomly pick a product
        product = products_2025[np.random.randint(0, len(products_2025))]
        sku, name, price = product
        
        # Random quantity 1–25
        quantity = np.random.randint(1, 26)
        
        # Random sequential date in month
        selling_date = datetime(year_2025, month, np.random.randint(1, last_day + 1)).strftime("%d/%m/%Y")
        
        # Discount: randomly 0% or 2%
        discount_amount = round(quantity * price * 0.02 * np.random.randint(0, 2), 2)
        
        # Total and net
        total = round(quantity * price, 2)
        net = round(total - discount_amount, 2)
        
        sales_rows.append([sku, name, price, selling_date, quantity, discount_amount, total, net])
    
    # Save CSV
    df = pd.DataFrame(sales_rows, columns=[
        "sku", "product_name", "selling_price", "selling_date",
        "quantity", "discount_amount", "total", "net"
    ])
    file_path = os.path.join(output_dir_2025, f"{month_name} 2025 Sales.csv")
    df.to_csv(file_path, index=False)
    month_files_2025.append(file_path)

# -----------------------------
# Create a ZIP of all CSVs
# -----------------------------
zip_filename = "Monthly_Sales_2025_Jan_to_Sep.zip"
with zipfile.ZipFile(zip_filename, "w") as zipf:
    for file in month_files_2025:
        zipf.write(file, arcname=file.split("/")[-1])

print(f"All CSVs created in folder '{output_dir_2025}' and zipped as '{zip_filename}'")
