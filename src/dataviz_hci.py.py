import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data_feedback = {
    'Kategori_Fitur': ['Navigasi UI', 'Kecepatan Muat', 'Tampilan Warna', 'Kemudahan Tombol', 'Fitur Pencarian'],
    'Skor_Kepuasan_Rata2': [4.2, 3.1, 4.8, 3.9, 4.5], # Skala 1 - 5
    'Jumlah_Responden': [120, 150, 110, 135, 140]
}

df = pd.DataFrame(data_feedback)

print("=== RINGKASAN EVALUASI HCI (USABILITY FEEDBACK) ===")
print(df)
print("\n-----------------------------------------------------")
print(f"Fitur dengan Kepuasan Tertinggi: {df.loc[df['Skor_Kepuasan_Rata2'].idxmax(), 'Kategori_Fitur']} ({df['Skor_Kepuasan_Rata2'].max()})")
print(f"Fitur yang Perlu Ditingkatkan (Terendah): {df.loc[df['Skor_Kepuasan_Rata2'].idxmin(), 'Kategori_Fitur']} ({df['Skor_Kepuasan_Rata2'].min()})")


try:
    plt.figure(figsize=(8, 5))
    plt.bar(df['Kategori_Fitur'], df['Skor_Kepuasan_Rata2'], color='skyblue', edgecolor='navy')
    plt.axhline(y=4.0, color='red', linestyle='--', label='Target Standar (4.0)')
    plt.xlabel('Kategori Fitur Aplikasi')
    plt.ylabel('Skor Kepuasan Rata-rata (1-5)')
    plt.title('Evaluasi Usability & Kepuasan Pengguna (HCI)')
    plt.ylim(0, 5)
    plt.legend()
    plt.grid(axis='y', linestyle=':', alpha=0.7)
    plt.savefig('hci_feedback_chart.png')
    print("\nGrafik berhasil disimpan sebagai file 'hci_feedback_chart.png'!")
except Exception as e:
    print(f"\nCatatan Visualisasi: {e}")