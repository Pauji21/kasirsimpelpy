from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Daftar menu
daftar_menu = [
    {"id": 1, "nama": "Ayam Geprek", "harga": 5000},
    {"id": 2, "nama": "Ayam Bakar", "harga": 5000},
    {"id": 3, "nama": "Paket Geprekdy Hemat 1", "harga": 10000},
    {"id": 4, "nama": "Paket Geprekdy Hemat 2", "harga": 20000},
    {"id": 5, "nama": "Minuman Air Putih", "harga": 2000}
]

@app.route('/')
def index():
    return render_template('index.html', daftar_menu=daftar_menu)

@app.route('/order', methods=['POST'])
def order():
    pesanan = {}
    total_harga = 0

    for item in daftar_menu:
        jumlah = int(request.form.get(f'menu_{item["id"]}', 0))
        if jumlah > 0:
            pesanan[item['nama']] = jumlah
            total_harga += item['harga'] * jumlah

    # Diskon 20% jika total harga lebih dari 100rb
    diskon = 0
    if total_harga > 100000:
        diskon = 0.2 * total_harga
        total_harga -= diskon

    uang_pelanggan = float(request.form.get('uang_pelanggan'))
    kembalian = uang_pelanggan - total_harga

    # Mengirim datetime ke template
    return render_template('nota.html', pesanan=pesanan, total_harga=total_harga, diskon=diskon,
                           uang_pelanggan=uang_pelanggan, kembalian=kembalian, datetime=datetime.now())

if __name__ == '__main__':
    app.run(debug=True)
