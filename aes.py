from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

#klucz AES 16 bajtow
key = b'kluczkluczklucz$'

#wczytaj plik tekstowy
with open('plik.txt', 'rb') as f:
    data = f.read()

#dodaj padding (dane muszą mieć długość wielokrotności 16)
padder = padding.PKCS7(128).padder()
data_padded = padder.update(data) + padder.finalize()

#losowy wektor inicjalizujący (IV)
iv = os.urandom(16)

#szyfrujemy dane
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
encryptor = cipher.encryptor()
encrypted = encryptor.update(data_padded) + encryptor.finalize()

#zapisujemy IV + zaszyfrowane dane do pliku
with open('plik_zaszyfrowany.aes', 'wb') as f:
    f.write(iv + encrypted)

print("Zaszyfrowano plik")
