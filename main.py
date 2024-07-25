import network
import time

# Ganti dengan SSID dan password WiFi Anda
ssid = '*******'
password = '*******'

# Inisialisasi objek WiFi dalam mode Station (STA)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Mulai proses koneksi ke jaringan WiFi
print(f'Menghubungkan ke jaringan {ssid}...')
wlan.connect(ssid, password)

# Tunggu hingga koneksi berhasil
max_attempts = 10
attempts = 0
while not wlan.isconnected() and attempts < max_attempts:
    attempts += 1
    print('Menghubungkan...')
    time.sleep(1)

if wlan.isconnected():
    print('Koneksi berhasil!')
    print('Informasi jaringan:')
    print(wlan.ifconfig())
else:
    print('Koneksi gagal. Silakan periksa SSID dan password.')

# Fungsi untuk memutuskan koneksi
def disconnect_wifi():
    wlan.disconnect()
    print('Koneksi terputus.')

# Fungsi untuk kembali menghubungkan
def reconnect_wifi():
    wlan.connect(ssid, password)
    print('Menghubungkan kembali...')

