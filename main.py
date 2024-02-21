import mysql.connector
from colorama import Fore,Style
import mahasiswa
import login

db = mysql.connector.connect (
    host="localhost",
    user="root",
    passwd="",
    database="dbpolibatam"
)

auth = login.autentikasi(db)

if auth==True:
    print(Fore.GREEN + "### Login berhasil. Selamat datang! ###")
    print(Style.RESET_ALL)
    while(True):
        mahasiswa.show_menu(db)
else:
    print(Fore.RED + "### Username / Password salah ###")
    print(Style.RESET_ALL)