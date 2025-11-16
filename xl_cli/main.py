# xl_cli/main.py

from .api import XLAPIClient
from .session import save_session, clear_session, is_logged_in

def display_menu():
    """Menampilkan menu utama."""
    print("\n--- Menu CLI XL ---")
    print("1. Login")
    print("2. Tampilkan Daftar Paket")
    print("3. Beli Paket")
    print("4. Logout")
    print("5. Keluar")
    print("--------------------")

def handle_login():
    """Menangani proses login pengguna."""
    if is_logged_in():
        print("Anda sudah login.")
        return

    msisdn = input("Masukkan nomor telepon Anda (misal: 81234567890): ")

    client = XLAPIClient()

    print(f"Meminta OTP untuk {msisdn}...")
    otp_response = client.request_otp(msisdn)

    if not otp_response or otp_response.get('success') is False:
        print("Gagal meminta OTP. Silakan periksa nomor dan coba lagi.")
        return

    print("OTP telah dikirim ke nomor Anda.")

    otp_code = input("Masukkan OTP yang Anda terima: ")

    print("Memvalidasi OTP...")
    token_response = client.validate_otp(msisdn, otp_code)

    if token_response and 'token' in token_response:
        save_session(token_response['token'])
        print("Login berhasil!")
    else:
        print("Login gagal. OTP mungkin salah atau sudah kedaluwarsa.")

def handle_list_packages():
    """Menangani penampilan daftar paket yang tersedia."""
    if not is_logged_in():
        print("Anda harus login terlebih dahulu. Silakan pilih menu 'Login'.")
        return

    client = XLAPIClient()
    print("Mengambil daftar paket...")
    packages = client.get_packages()

    if packages and isinstance(packages, list) and len(packages) > 0:
        print("\n--- Paket Tersedia ---")
        for pkg in packages:
            print(f"ID: {pkg.get('id', 'N/A')} | Nama: {pkg.get('name', 'N/A')} | Harga: {pkg.get('price', 'N/A')}")
        print("--------------------")
    else:
        print("Tidak dapat mengambil daftar paket atau tidak ada paket yang tersedia.")

def handle_buy_package():
    """Menangani proses pembelian paket."""
    if not is_logged_in():
        print("Anda harus login terlebih dahulu. Silakan pilih menu 'Login'.")
        return

    package_id = input("Masukkan ID Paket yang ingin dibeli: ")
    family_code = input("Masukkan Kode Keluarga: ")

    client = XLAPIClient()
    print(f"Mencoba membeli paket {package_id}...")

    purchase_response = client.purchase_package(package_id, family_code)

    if purchase_response and purchase_response.get('success'):
        print("Pembelian paket berhasil!")
        print(f"ID Transaksi: {purchase_response.get('transactionId', 'N/A')}")
    else:
        error_message = purchase_response.get('message', 'Terjadi kesalahan yang tidak diketahui.')
        print(f"Gagal membeli paket. Alasan: {error_message}")

def handle_logout():
    """Menangani logout pengguna."""
    clear_session()

def main():
    """Fungsi utama untuk menjalankan loop menu."""
    while True:
        display_menu()
        choice = input("Pilih menu (1-5): ")

        if choice == '1':
            handle_login()
        elif choice == '2':
            handle_list_packages()
        elif choice == '3':
            handle_buy_package()
        elif choice == '4':
            handle_logout()
        elif choice == '5':
            print("Terima kasih telah menggunakan XL CLI. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka dari 1 hingga 5.")

if __name__ == "__main__":
    main()
