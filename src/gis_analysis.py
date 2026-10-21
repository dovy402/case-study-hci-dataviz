import pandas as pd
import numpy as np
from shapely.geometry import Point


data_lokasi = {
    'Lokasi_ID': [f'Kandidat_{i}' for i in range(1, 6)],
    'Latitude': [-6.2000, -6.2100, -6.2200, -6.2300, -6.2400],
    'Longitude': [106.8167, 106.8267, 106.8367, 106.8467, 106.8567],
    'Kepadatan_Penduduk': [15000, 22000, 18000, 9000, 31000], # Jiwa/km2
    'Jumlah_Kompetitor': [5, 12, 3, 1, 15]
}

df = pd.DataFrame(data_lokasi)




df['Skor_Potensi'] = (df['Kepadatan_Penduduk'] / 1000) - (df['Jumlah_Kompetitor'] * 1.5)


lokasi_terbaik = df.sort_values(by='Skor_Potensi', ascending=False).iloc[0]

print("=== HASIL ANALISIS SPASIAL LOKASI STRATEGIS (GIS) ===")
print(df[['Lokasi_ID', 'Latitude', 'Longitude', 'Kepadatan_Penduduk', 'Jumlah_Kompetitor', 'Skor_Potensi']])
print("\n-----------------------------------------------------")
print(f"Rekomendasi Lokasi Industri/Bisnis Terbaik: {lokasi_terbaik['Lokasi_ID']}")
print(f"Koordinat: ({lokasi_terbaik['Latitude']}, {lokasi_terbaik['Longitude']})")
print(f"Skor Kelayakan Spasial: {lokasi_terbaik['Skor_Potensi']:.2f}")