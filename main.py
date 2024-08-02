from Mariadb_class import *
import os

host = os.environ.get("SERVER")
user = os.environ.get("USER")
password = os.environ.get("PASSWORD")
port = os.environ.get("PORT")
DB = os.environ.get("DATABASE")

models_ios = [
    ("9200L","IOS XE 17.9.4"),
    ("9300L","IOS XE 17.9.4"),
    ("C9300","IOS XE 17.9.4"),
    ("9400-SUP1XL",	"IOS XE 17.9.4"),
    ("C9500","IOS XE 17.9.4"),
    ("C9500-32C","IOS XE 17.9.4"),
    ("C9600 -SUP1","IOS XE 17.9.4"),
    ("IE-2000","IOS 15.2.(7)E4"),
    ("IE-4000","IOS 15.2.(7)E4"),
    ("IE-4010","IOS 15.2.(7)E4"),
    ("IE-3400","IOS XE 17.3.5"),
    ("WS-C2960X","IOS 15.2.(7)E6"),
    ("WS-C3560CX","IOS 15.2.(7)E6"),
    ("WS-C3650","IOS XE 16.12.7"),
    ("WS-C3850","IOS XE 16.12.7"),
    ("WS-C4500-E","IOS XE 3.8.8E "),
    ("WS-C4500-X","IOS XE 3.11.4E"),
    ("N5K-C5548UP","NX-OS 7.3(8)N1(1)"),
    ("N9K-C9300","NX-OS 7.0(3)I7(9)"),
    ("WS-C2960",""),
    ("WS-C2960S","IOS 15.2(2) E9"),
    ("WS-C2960CX",""),
    ("WS-C6500E",""),
    ("WS-C6800",""),
    ("WS-C3750-X","")
    ]

try:
    cx = MySQLDatabase(host=host, user=user, port=port, password=password, database=DB)
    # USE THE METHODS HERE
    cx.close_connection()
except Error as e:
    print("Error:", str(e))