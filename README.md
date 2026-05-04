# NLP Inverted Index - Sistem Pencarian Sederhana

**Natural Language Processing (NLP)**

## Penjelasan Project

Project ini berisi implementasi dari **Inverted Index** (Indeks Terbalik), yaitu sebuah struktur data yang sering digunakan dalam mesin pencari (*search engine*) maupun pada sistem *Information Retrieval* (Sistem Temu Kembali Informasi). Struktur ini memetakan kata (term) ke dokumen-dokumen mana saja yang memuat kata tersebut, sehingga mempercepat proses pencarian dokumen berdasarkan *query* pengguna tanpa perlu membaca seluruh teks berulang kali.

## Tahapan yang Dilakukan

Proses pembangunan dan pengujian sistem *Inverted Index* di dalam skrip `main.py` ini meliputi beberapa tahapan utama:

1. **Load Dataset**
   Memuat dataset berupa sekumpulan teks berita dari file `datasets/data_berita.csv`. Setiap dokumen berita setidaknya memiliki atribut `id`, `title` (judul berita), dan `content` (isi berita).
2. **Preprocessing Sederhana**
   Melakukan normalisasi teks awal untuk menunjang pencarian:
   - *Case Folding*: Mengubah seluruh huruf menjadi huruf kecil (*lowercase*).
   - *Filtering*: Menghapus tanda baca, angka, dan karakter selain huruf alphabet (menggunakan Regex).
   - Penggabungan teks dari kolom `title` dan `content` ke dalam satu corpus teks pencarian, lalu menghapus spasi yang berlebih.
3. **Membangun Inverted Index**
   Melakukan perulangan pada setiap dokumen dan memecah teks menjadi *term* tunggal (kata). Selanjutnya, dibangun *dictionary* (indeks terbalik) di mana setiap *key* adalah sebuah kata unik, dan setiap *value* adalah sekumpulan *Document ID* beserta frekuensi kemunculan kata tersebut di dalam dokumen terkait.
4. **Fungsi Search (Pencarian Term)**
   Sistem membaca input *query* dari pengguna, melakukan tahapan *preprocessing* yang sama pada *query* tersebut, memecah *query* menjadi kata-kata (terms), kemudian mengembalikan *Document ID* yang merupakan hasil persilangan (*intersection*)—hanya mengambil dokumen yang memuat seluruh suku kata yang dicari.
5. **Menampilkan Hasil Pencarian**
   Menerjemahkan kumpulan *Document ID* hasil dari indeks terbalik kembali ke dalam bentuk tabel *dataframe* untuk menampilkan Judul (*Title*) dan ID dari dokumen yang relevan dengan kueri.

## Library yang Digunakan

Project ini menggunakan bahasa pemrograman **Python 3**. Anda membutuhkan library berikut untuk menjalankan skrip:

- **pandas**: Digunakan untuk manipulasi dan analisis data (membaca `data_berita.csv`).
- **re (RegEx)**: Digunakan untuk pencocokan dan pembersihan pola tanda baca di dalam *preprocessing* teks (Library bawaan Python).

Untuk meng-install `pandas` (jika belum terinstal), jalankan perintah:
```bash
pip install pandas
```

## Cara Menjalankan Program

1. Buka terminal atau Command Prompt.
2. Pastikan Anda berada di dalam direktori `inverted-index/`.
3. Jalankan script utama:
   ```bash
   python main.py
   ```
4. Program akan meminta Anda memasukkan *query* pencarian:
   ```text
   Masukkan query: [Ketikkan kata kunci pencarian Anda, misal: teknologi]
   ```
5. Hasil dari pencarian akan ditampilkan dalam bentuk daftar *Document ID* dan Judul Berita yang memuat kata kunci tersebut.

## Struktur Project

```text
inverted-index/
├── datasets/
│   └── data_berita.csv     # Dataset berita yang dijadikan database pencarian
├── main.py                 # File script utama Inverted Index & Mesin Pencari
└── README.md               # Dokumentasi project ini
```
