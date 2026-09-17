import sqlite3
import hashlib
import os
import getpass

# commect database

connection = sqlite3.connect("axiom_users.db")
cursor =  connection.cursor()

# create users table
cursor.execute (""" 
CREATE TABLE IF NOT EXISTS users 
(id INTEGER PRIMARY KEY AUTOINCREMENT, 
username TEXT UNIQUE NOT NULL, password_hash TEXT NOT NULL)
""" )
connection.commit() 

#...... SING UP ......

print ("\n ==== AXIOM SIGN UP ==== ")


username = input ("create username: ").strip()

password = getpass.getpass("create pasword: ")

#Generate a random salt
salt = os.urandom(16)

#Hash password
password_hash = hashlib.pbkdf2_hmac(
    "sha256",
    password.encode(),
    salt,
    100000
)

#store salt + hash together
stored_password = salt. hex() + ":" + password_hash.hex()

try :
    cursor.execute(
        "INSERT INTO users (username, password_hash) VALUES (?, ?)",
        (username,stored_password)
    )
        
    print("\n Account Created Successfully! ")
except sqlite3.IntegrityError:
    print ("\n Already existing username! ")

# -------- login-------
print("\n ===== AXIOM LOGIN =====")

login_username = input ("username: ").strip()

login_password = getpass.getpass("password: ")


cursor.execute(
    "SELECT password_hash FROM users WHERE username = ?",
    (login_username,) 
)
result = cursor.fetchone()

if result:
    stored_password = result[0]

    salt_hex, hash_hex = stored_password.split (":")

    salt = bytes. fromhex (salt_hex)
    stored_hash = bytes.fromhex(hash_hex)

    login_hash = hashlib.pbkdf2_hmac(
        "sha256",
        login_password.encode(),
        salt,
        100000
    )

if login_hash == stored_hash:
    print("\n Access granted!")
else:
    print("\n user not found!")


connection.close() 