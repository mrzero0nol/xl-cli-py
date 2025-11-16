# XL CLI Tool

Ini adalah alat antarmuka baris perintah (CLI) untuk berinteraksi dengan API XL Axiata. Anda dapat menggunakannya untuk login, melihat daftar paket data, dan membeli paket menggunakan kode keluarga.

## Mengatasi Galat '403 Forbidden'

Jika Anda mengalami galat `403 Forbidden`, itu berarti kunci API yang digunakan oleh aplikasi ini sudah tidak berlaku lagi. Kunci-kunci ini disimpan dalam file `config.json` agar mudah diperbarui.

**Untuk memperbaikinya:**
1.  Buka file `xl_cli/config.json`.
2.  Ganti nilai-nilai lama (seperti `BASIC_AUTH`, `API_KEY`, dll.) dengan kunci baru yang Anda peroleh.
3.  Simpan file tersebut dan jalankan kembali aplikasi.

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
- Membuat file konfigurasi `xl_cli/config.json` untuk Anda.
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
