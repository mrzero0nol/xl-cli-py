# XL CLI Tool

Ini adalah alat antarmuka baris perintah (CLI) untuk berinteraksi dengan API XL Axiata. Anda dapat menggunakannya untuk login, melihat daftar paket data, dan membeli paket menggunakan kode keluarga.

## Instalasi di Termux

Panduan ini akan membantu Anda menginstal dan menjalankan alat ini di Termux, bahkan jika Anda seorang pemula. Cukup salin dan tempel (copy-paste) perintah-perintah berikut satu per satu.

### Langkah 1: Siapkan Termux

Pertama, pastikan Termux Anda diperbarui.

```bash
pkg update && pkg upgrade
```

### Langkah 2: Instal Git dan Python

Anda memerlukan `git` untuk mengunduh kode dari repositori dan `python` untuk menjalankan aplikasi.

```bash
pkg install git python
```

### Langkah 3: Unduh (Clone) Repositori

Sekarang, unduh kode aplikasi ini dari GitHub.

```bash
git clone https://github.com/example/xl-cli-py.git
```
*(Catatan: Ganti URL di atas dengan URL repositori yang sebenarnya jika berbeda.)*

### Langkah 4: Masuk ke Direktori Proyek

Setelah pengunduhan selesai, masuklah ke direktori yang baru saja dibuat.

```bash
cd xl-cli-py
```

### Langkah 5: Instal Ketergantungan (Dependencies)

Aplikasi ini membutuhkan beberapa pustaka Python agar dapat berfungsi. Perintah ini akan menginstalnya secara otomatis dari file `requirements.txt`.

```bash
pip install -r xl_cli/requirements.txt
```

Instalasi selesai! Sekarang Anda siap untuk menggunakan alat ini.

## Cara Penggunaan

Aplikasi ini sekarang menggunakan antarmuka berbasis menu yang interaktif, sehingga lebih mudah digunakan.

### 1. Jalankan Aplikasi

Untuk memulai, jalankan perintah berikut dari dalam direktori `xl-cli-py`:

```bash
python -m xl_cli.main
```

### 2. Gunakan Menu

Setelah aplikasi berjalan, Anda akan melihat menu utama:

```
--- Menu CLI XL ---
1. Login
2. Tampilkan Daftar Paket
3. Beli Paket
4. Logout
5. Keluar
--------------------
```

- **Pilih `1` untuk Login:** Aplikasi akan meminta nomor telepon dan OTP Anda.
- **Pilih `2` untuk Melihat Paket:** Setelah login, Anda dapat melihat semua paket yang tersedia.
- **Pilih `3` untuk Membeli Paket:** Anda akan diminta untuk memasukkan ID paket dan kode keluarga.
- **Pilih `4` untuk Logout:** Ini akan menghapus sesi login Anda.
- **Pilih `5` untuk Keluar:** Ini akan menghentikan aplikasi.

Cukup ketikkan nomor pilihan Anda dan tekan Enter, lalu ikuti petunjuk di layar.
