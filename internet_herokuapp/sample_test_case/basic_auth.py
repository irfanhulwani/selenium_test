import requests
import base64

# Set URL halaman yang memerlukan basic authentication
url = "http://the-internet.herokuapp.com/basic_auth"
username = "admin"
password = "admin"

# Kodekan kredensial ke dalam format Base64
credentials = f"{username}:{password}"
encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")

# Buat header HTTP dengan kredensial untuk basic auth
headers = {
    "Authorization": f"Basic {encoded_credentials}"
}

try:
    # Kirim permintaan GET ke URL dengan header untuk autentikasi
    response = requests.get(url, headers=headers)

    # Verifikasi apakah Anda berhasil masuk dengan memeriksa kode status
    if response.status_code == 200:
        print("Berhasil masuk dengan basic authentication.")
        # Tampilkan konten halaman web jika autentikasi berhasil
        print(response.text)
    elif response.status_code == 401:
        print("Gagal masuk dengan basic authentication. Kredensial salah.")
    else:
        print(f"Terjadi kesalahan. Kode status: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
