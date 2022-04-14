import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

xlFile = 'D:/KULIAH/SEMESTER 8/Penumpang KAI.xlsx'
data = pd.read_excel(xlFile, sheet_name="Sheet2")
print(data)
print("")
print("================================================================================")
print("")
data_array = np.array(data)  # mengambil data ke var data
bulan = data_array[:, 0]
jml_penumpang = frekuensi = data_array[:, 2]
frekuensi = data_array[:, 1]  # ambil frekuensi di excel


f = 0
for i in range(len(frekuensi)):
    f = f + frekuensi[i]
print("Nilai ΣFrekuensi: ", f)

prob = []
sum_f = 0
for a in range(len(frekuensi)):
    sum_f = frekuensi[a]/f
    # print("probabilitas bulan ke-",a,"=",sum_f)
    prob.append(sum_f)

prob_d = np.array([prob])
data_prob = np.concatenate((data_array, prob_d.T), axis=1)
df = pd.DataFrame(data_prob, columns=[
                  "Bulan Ke", "Jumlah Penumpang", "Frekuensi", "Probabilitas"])
print()
print("Tabel Hasil Hitungan Probabilitas")
print(df)

prob_k = []
sum_p = 0
for a in range(len(frekuensi)):
    sum_p = sum_p + prob[a]
    print("probabilitas kumulatif Bulan ke-", a, "=", sum_p)
    prob_k.append(sum_p)

prob_kd = np.array([prob_k])
data = np.concatenate((df, prob_kd.T), axis=1)
dpk = pd.DataFrame(data, columns=[
                   "Bulan Ke", "Jumlah Penumpang",  "Frekuensi", "Probabilitas", "Probabilitas Kumulatif"])
print()
print("Tabel Hasil Hitungan Probabilitas")
print(dpk)


interval_min = []
min_v = 0
for a in range(len(frekuensi)):
    if(a == 0):
        interval_min.append(min_v)
        print("Interval Bulan ke-", a, " = ", min_v, "-", prob_k[a])
    else:
        min_v = prob_k[a-1]+0.001
        interval_min.append(min_v)
        print("Interval Bulan ke-", a, " = ", min_v, "-", prob_k[a])

interval_mind = np.array([interval_min])
data_interval_bwh = np.concatenate((dpk, interval_mind.T), axis=1)
interval_maxd = np.array([prob_k])
data = np.concatenate((data_interval_bwh, interval_maxd.T), axis=1)
data_interval = pd.DataFrame(data, columns=["Bulan Ke", "Jumlah Penumpang", "Frekuensi", "Probabilitas",
                                            "Probabilitas Kumulatif", "Interval Batas Bawah", "Interval Batas Atas"])
print()
print("Tabel Interval Atas dan Bawah")
print(data_interval)

bulan_baru = 1
taksir = input('Taksiran dalam berapa bulan: ')
p_bulan = []
angka_acak = []
permintaan = []
for a in range(int(taksir)):
    p_bulan.append(bulan_baru)
    acak = random.random()
    angka_acak.append(acak)
    if(acak < 0.2):
        jenis = 0
        permintaan.append(jenis)
    elif(acak < 0.6):
        jenis = 1
        permintaan.append(jenis)
    elif(acak < 0.8):
        jenis = 2
        permintaan.append(jenis)
    elif(acak < 0.9):
        jenis = 3
        permintaan.append(jenis)
    elif(acak <= 1):
        jenis = 4
        permintaan.append(jenis)
    bulan_baru += 1

p = 0
for i in range(len(permintaan)):
    p = p + permintaan[i]

print("Bulan Ke-", "|", "Angka Acak", "|", "Permintaan")
for a in range(int(taksir)):
    print(p_bulan[a], "|", angka_acak[a], "|", permintaan[a])

print("Ramalan/Taksiran ", int(taksir),
      "bulan kedepan adalah jumlah penumpang = ", p, " dengan estimasi nilai", p, "x Rp.100.000 = ", p*100000, "Dan rata-rata pemasukan bulanan adalah", (p*100000)/int(taksir), "rupiah")

plt.plot(bulan, jml_penumpang)
plt.title("Grafik jumlah Penumpang Tiap Bulan")
plt.xlabel("Bulan")
plt.ylabel("Jumlah Penumpang")
plt.grid()
plt.show()
