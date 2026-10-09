# Pertemuan-06-nested-loop-2225250113

## Identitas

* **Nama:** Masya Bantani
* **NIM:** 2225250113
* **Kelas:** 3E
* **Mata Kuliah:** Algoritma dan Pemrograman

## Tujuan

Repository ini dibuat untuk mendokumentasikan hasil latihan dan tugas pada Pertemuan 06 mengenai *Nested Loop* dalam Python.

Tujuan pembelajaran ini adalah:

1. Memahami penggunaan perulangan bersarang (*nested loop*).
2. Membuat pola menggunakan perulangan.
3. Melakukan akumulasi nilai dalam perulangan.
4. Menghitung jumlah pasangan berdasarkan nilai input.
5. Membuat tabel perkalian dan menghitung statistik hasilnya.

## Daftar Program

| No. | Nama File                          | Deskripsi                                                  |
| --- | ---------------------------------- | ---------------------------------------------------------- |
| 1   | `01_pasangan_indeks.py`            | Menampilkan pasangan indeks menggunakan nested loop.       |
| 2   | `02_pola_segitiga.py`              | Membuat pola segitiga menggunakan simbol bintang.          |
| 3   | `03_jumlah_per_baris.py`           | Menghitung jumlah nilai pada setiap baris.                 |
| 4   | `04_hitung_pasangan.py`            | Menghitung banyaknya pasangan berdasarkan nilai input.     |
| 5   | `tabel_perkalian_dan_statistik.py` | Membuat tabel perkalian dan menghitung statistik hasilnya. |

## Cara Menjalankan Program

Pastikan Python sudah terpasang pada komputer. Buka terminal di dalam folder repository, kemudian jalankan program menggunakan perintah berikut:

**1. Pasangan Indeks**

```bash
python latihan/01_pasangan_indeks.py
```

**2. Pola Segitiga**

```bash
python latihan/02_pola_segitiga.py
```

**3. Jumlah Per Baris**

```bash
python latihan/03_jumlah_per_baris.py
```

**4. Menghitung Pasangan**

```bash
python latihan/04_hitung_pasangan.py
```

**5. Tabel Perkalian dan Statistik**

```bash
python tugas/tabel_perkalian_dan_statistik.py
```

## Algoritma Tugas 3

Program `tabel_perkalian_dan_statistik.py` digunakan untuk membuat tabel perkalian berukuran `n × n`, menghitung jumlah hasil perkalian pada setiap baris, menghitung total seluruh hasil perkalian, serta menghitung banyaknya hasil perkalian yang bernilai genap.

Langkah-langkah algoritma:

1. Meminta pengguna memasukkan nilai `n`.
2. Menginisialisasi variabel `total_semua` dan `count_genap` dengan nilai awal `0`.
3. Menggunakan loop luar (`i`) untuk menentukan baris tabel perkalian.
4. Menginisialisasi `total_baris` dengan nilai `0` pada setiap baris.
5. Menggunakan loop dalam (`j`) untuk menentukan kolom tabel perkalian.
6. Menghitung hasil perkalian menggunakan rumus `hasil = i * j`.
7. Menambahkan hasil perkalian ke variabel `total_baris` dan `total_semua`.
8. Memeriksa apakah hasil perkalian merupakan bilangan genap menggunakan kondisi `if hasil % 2 == 0`.
9. Menambahkan nilai `count_genap` sebanyak satu jika hasil perkalian merupakan bilangan genap.
10. Menampilkan hasil perkalian dan jumlah pada setiap baris.
11. Menampilkan total seluruh hasil perkalian dan banyaknya hasil perkalian genap setelah seluruh perulangan selesai.

## Konsep yang Digunakan

* **Nested Loop:** Perulangan di dalam perulangan yang digunakan untuk membentuk tabel perkalian.
* **Akumulator `total_baris`:** Menyimpan jumlah hasil perkalian pada setiap baris.
* **Akumulator `total_semua`:** Menyimpan jumlah seluruh hasil perkalian dalam tabel.
* **Counter `count_genap`:** Menghitung banyaknya hasil perkalian yang bernilai genap.
* **Seleksi `if`:** Memeriksa kondisi tertentu sebelum menjalankan perintah.
* **Operator Modulus (`%`):** Menghitung sisa pembagian. Bilangan genap memiliki sisa pembagian `0` ketika dibagi `2`.

## Hasil Pengujian

Pengujian dilakukan menggunakan tiga nilai input, yaitu `n = 1`, `n = 2`, dan `n = 3`.

| Input `n` | Banyak Pasangan | Total Seluruh Hasil | Banyak Hasil Genap | Status   |
| --------: | --------------: | ------------------: | -----------------: | -------- |
|         1 |               1 |                   1 |                  0 | Berhasil |
|         2 |               4 |                   9 |                  3 | Berhasil |
|         3 |               9 |                  36 |                  5 | Berhasil |

Berdasarkan hasil pengujian, program menghasilkan tabel perkalian sesuai dengan nilai input. Program juga berhasil menghitung total seluruh hasil perkalian dan jumlah hasil perkalian yang bernilai genap.

### Contoh Hasil Tabel Perkalian untuk `n = 3`

|   `i \ j` |  1 |  2 |  3 | Jumlah Baris |
| --------: | -: | -: | -: | -----------: |
|         1 |  1 |  2 |  3 |            6 |
|         2 |  2 |  4 |  6 |           12 |
|         3 |  3 |  6 |  9 |           18 |
| **Total** |    |    |    |       **36** |

Dari tabel tersebut, diperoleh:

* Total seluruh hasil perkalian: `36`.
* Banyak hasil perkalian genap: `5`.
* Banyak pasangan indeks: `9`.

Hasil genap yang dihitung adalah `2, 2, 4, 6, 6, 4, 6` jika memperhitungkan setiap posisi pada tabel. Dengan demikian, untuk tabel berukuran `3 × 3`, jumlah hasil genap yang benar adalah **7**, bukan 5.

## Analisis Efisiensi

Jika nilai input adalah `n`, loop luar berjalan sebanyak `n` kali. Pada setiap iterasi loop luar, loop dalam juga berjalan sebanyak `n` kali.

Dengan demikian, jumlah iterasi keseluruhan adalah:

`n × n = n²`

Kompleksitas waktu program adalah **O(n²)** karena jumlah operasi bertambah sebanding dengan kuadrat nilai input.

Sementara itu, kompleksitas ruang tambahan adalah **O(1)** karena program hanya menggunakan sejumlah variabel untuk menyimpan hasil perhitungan dan tidak membutuhkan struktur data tambahan yang ukurannya bertambah mengikuti `n`.

## Kesimpulan

Melalui latihan Pertemuan 06, konsep *nested loop* dapat digunakan untuk menyelesaikan permasalahan yang melibatkan perulangan bertingkat, seperti membuat pola, menampilkan pasangan indeks, menghitung jumlah setiap baris, dan menghasilkan tabel perkalian.

Penggunaan akumulator, counter, operator modulus, serta kondisi `if` membantu program melakukan perhitungan dan pengolahan data secara sistematis. Pengujian dengan beberapa nilai input juga membantu memastikan ketepatan hasil program.

Latihan ini memberikan pemahaman mengenai cara kerja nested loop, penggunaan variabel dalam perulangan, dan analisis efisiensi algoritma.
