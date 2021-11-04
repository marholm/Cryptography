"""TDT4113_Assignment 3: Cryptography"""
__author__ = 'Marianne Hernholm'
__project__ = 'TDT4113_Assignment_3'

import person
import cipher


def main():
    """Main to run program"""

    # Message to be encrypted by all ciphers
    print()
    message = 'arm'
    print('Original message: ', message)
    print()

    # ---------- CAESAR CIPHER (1) -------------------------------
    print('------------CAESAR CIPHER---------------------------\n')
    caesar = cipher.Caesar()
    send1 = person.Sender(2, caesar)                # SENDER - Person(key, cipher)
    rec1 = person.Receiver(2, caesar)               # RECEIVER - Person(key, cipher)
    encoding_caesar = send1.operate_cipher(message)         # Operate cipher takes in a message
    decoding_caesar = rec1.operate_cipher(encoding_caesar)  # Operate cipher takes in a message
    # ver_caesar = cipher.Cipher.verify(caesar, 2, encoding_caesar, decoding_caesar)
    print()

    # ------------------ MULTIPLICATION CIPHER (2) -----------------
    print('---------- MULTIPLICATION CIPHER ---------------------\n')
    mult_cipher = cipher.Multiplication()
    send2 = person.Sender(3, mult_cipher)
    rec2 = person.Receiver(3, mult_cipher)
    encoding_mult = send2.operate_cipher(message)
    decoding_mult = rec2.operate_cipher(encoding_mult)
    # ver_mult = cipher.Cipher.verify(mult_cipher, 3, encoding_mult, decoding_mult)
    print()

    # ------------------- AFFINE CIPHER (3) -------------------------
    print('---------------- AFFINE CIPHER ------------------------\n')
    affine_cipher = cipher.Affine()
    send3 = person.Sender((3, 4), affine_cipher)
    rec3 = person.Receiver((3, 4), affine_cipher)
    encoding_affine = send3.operate_cipher(message)
    decoding_affine = rec3.operate_cipher(encoding_affine)
    # ver_affine = cipher.Cipher.verify(affine_cipher, (3, 4), encoding_affine, decoding_affine)
    print()

    # ------------------ UNBREAKABLE CIPHER (4) ----------------------
    print('------------ UNBREAKABLE CIPHER -----------------------\n')
    unbreakable = cipher.Unbreakable()
    send4 = person.Sender('ab', unbreakable)
    rec4 = person.Receiver('ab', unbreakable)
    encoding_unbreakable = send4.operate_cipher(message)
    decoding_unbreakable = rec4.operate_cipher(encoding_unbreakable)
    # ver_unbreakable = cipher.Cipher.verify(unbreakable, 'ab', encoding_unbreakable, decoding_unbreakable)
    print()

    # -------------------- RSA CIPHER (5) ------------------------
    print('-------------- RSA CIPHER ----------------------------')
    rsa = cipher.RSA()
    current_key = rsa.generate_keys()
    send5 = person.Sender(current_key, rsa)
    encoding_rsa = send5.operate_cipher(message)
    rec5 = person.Receiver(current_key, rsa)
    decoding_rsa = rec5.operate_cipher(encoding_rsa)
    # ver_rsa = cipher.Cipher.verify(rsa, current_key, encoding_rsa, decoding_rsa)
    print()

    # --------------------------- HACKER ----------------------------
    print('----------------------HACKER--------------------------\n')
    print('Hack caesar cipher: ')
    # hacker1 = person.Hacker(caesar)
    # hack_caesar = hacker1.intercept_message(encoding_caesar)
    print()
    print('Hack multiplication cipher: ')
    # hacker2 = person.Hacker(mult_cipher)
    # hack_mult = hacker2.intercept_message(encoding_mult)
    print()
    print('Hack affine cipher: ')
    # hacker_3 = person.Hacker(affine_cipher)
    # hack_affine = hacker_3.intercept_message(encoding_affine)
    print()
    print('Hack unbreakable cipher: ')
    # hacker4 = person.Hacker(unbreakable)
    # hack_unbreakable = hacker4.intercept_message(encoding_unbreakable)

    return ''


RUN_MAIN = main()
