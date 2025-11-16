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

Semua perintah dijalankan dari dalam direktori `xl-cli-py`.

### 1. Login

Sebelum melakukan apa pun, Anda harus login. Aplikasi akan meminta nomor telepon Anda dan kemudian OTP yang dikirimkan ke nomor tersebut.

```bash
python -m xl_cli.main login
```

### 2. Melihat Daftar Paket

Setelah berhasil login, Anda dapat melihat semua paket data yang tersedia.

```bash
python -m xl_cli.main list-packages
```
Perintah ini akan menampilkan daftar paket beserta ID dan harganya. Catat `ID` paket yang ingin Anda beli.

### 3. Membeli Paket

Untuk membeli paket, Anda memerlukan `ID Paket` (dari perintah sebelumnya) dan `Kode Keluarga`.

Ganti `[ID_PAKET]` dan `[KODE_KELUARGA]` dengan informasi yang benar.

```bash
python -m xl_cli.main buy-package [ID_PAKET] [KODE_KELUARGA]
```
**Contoh:**
```bash
python -m xl_cli.main buy-package 12345 C0D3F4M1LY
```

### 4. Logout

Jika Anda ingin menghapus sesi login Anda, gunakan perintah ini.

```bash
python -m xl_cli.main logout
```
