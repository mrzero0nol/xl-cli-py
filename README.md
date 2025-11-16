# XL CLI Tool

Ini adalah alat antarmuka baris perintah (CLI) untuk berinteraksi dengan API XL Axiata. Anda dapat menggunakannya untuk login, melihat daftar paket data, dan membeli paket menggunakan kode keluarga.

## Instalasi Super Cepat di Termux

Lupakan langkah-langkah rumit. Cukup ikuti ini untuk menginstal semuanya secara otomatis.

### Langkah 1: Siapkan Termux & Instal Git

Jika Anda belum melakukannya, siapkan Termux dan instal `git`.

```bash
pkg update && pkg upgrade
pkg install git python
```

### Langkah 2: Unduh dan Jalankan Instalasi

Salin tiga baris perintah ini. Mereka akan mengunduh repositori, masuk ke direktorinya, dan menjalankan skrip instalasi otomatis.

```bash
git clone https://github.com/example/xl-cli-py.git
cd xl-cli-py
bash setup.sh
```
*(Catatan: Ganti URL di atas dengan URL repositori yang sebenarnya jika berbeda.)*

Skrip `setup.sh` akan secara otomatis:
- Menginstal semua pustaka Python yang diperlukan.
- Mengkonfigurasi dan menginstal perintah `xl`.

## Cara Penggunaan

Setelah instalasi berhasil, Anda tidak perlu lagi berada di dalam folder proyek. Anda dapat menjalankan aplikasi dari direktori mana pun.

### 1. Jalankan Aplikasi

Cukup ketik perintah berikut di Termux:

```bash
xl
```

### 2. Gunakan Menu

Aplikasi akan menampilkan menu interaktif. Gunakan angka untuk menavigasi:

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
