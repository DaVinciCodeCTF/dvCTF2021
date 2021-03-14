import secrets
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.strxor import strxor
from secret_data import key, flag

def encrypt(plaintext):
    try:
        plaintext = bytes.fromhex(plaintext)
    except ValueError as e:
        return "I only talk hex, sorry!", None
    concat = pad(plaintext + flag, 16)
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        ct = cipher.encrypt(concat)
        flip_it = secrets.choice([True, False])
        if flip_it:
            ct = strxor(ct, b'\xff' * len(ct))

        return ct.hex(), flip_it
    except ValueError as e:
        return "ERR", None

def main():
    while True:
        pt = input("What do you want me to encrypt? ")
        ct, flipped = encrypt(pt)
        if flipped:
            print(f"!E(input || flag) = {ct}")
        elif not flipped:
            print(f"E(input || flag) = {ct}")
	

if __name__ == '__main__':
    main()
