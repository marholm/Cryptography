"""Cipher file"""
import random
import math
import person
import crypto_utils


class Cipher:
    """Superclass for all ciphers. Keeps information shared by all ciphers."""

    def __init__(self):
        """Initializes cipher class"""
        # The alphabet consists of symbols from ascii_val 32 to ascii_val 126
        self.alphabet = ''' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'''

        # Global variables for encoded and decoded message respectively
        self.encoded_message = ''
        self.decoded_message = ''

    def encode(self, key, message):
        """Encode takes a self (cipher), key and a message and encrypts message with given key"""
        return

    def decode(self, key, message):
        """Decode takes a self(cipher), key and an encrypted-message and decrypts with given key"""
        return

    def verify(self, key, encoded_message, decoded_message):
        """Gets clear text -> encodes clear text -> decodes encrypted text
        -> verifies decoded_text == initial_clear_text"""
        # Have to check that the message is the same before and after encryption

        if encoded_message == self.encode(key, decoded_message) \
                and self.decode(key, encoded_message) == decoded_message:
            print('Verification successful')
        else:
            print('Verification failed')

    def generate_keys(self):
        """Generate encryption key for sender and receiver"""
        # Used in the RSA encryption scheme
        return

# -----------------------CAESAR CIPHER-----------------------


class Caesar(Cipher):
    """Subclass of Cipher: Caesar encryption"""
    def __init__(self):
        Cipher.__init__(self)

    def encode(self, key, message):
        self.encoded_message = ''           # For the hacker - this needs to be set empty each time
        for i in range(0, len(message)):
            symbol = message[i]                             # Iterates letters in message
            symbol_index = self.alphabet.index(symbol)      # index() is 0-indexed!
            symbol_index_encoded = (key + symbol_index)     # index for encoded symbol
            # gets symbol from encoded index
            symbol_encoded = self.alphabet[symbol_index_encoded % 95]
            self.encoded_message += symbol_encoded          # appends encrypted symbols to encrypted message
        print('Encoded message: ', self.encoded_message)
        return self.encoded_message

    def decode(self, key, message):
        self.decoded_message = ''
        for i in range(0, len(message)):
            symbol = message[i]
            symbol_index = self.alphabet.index(symbol)
            symbol_index_decoded = (symbol_index - key)
            symbol_decoded = self.alphabet[int(symbol_index_decoded % 95)]
            self.decoded_message += symbol_decoded           # appends decrypted symbols to decrypted message
        print('Decoded message: ', self.decoded_message)
        return self.decoded_message


# ---------------- MULTIPLICATION CIPHER -----------------------


class Multiplication(Cipher):
    """Subclass of cipher: Multiplication encryption"""
    def __init__(self):
        Cipher.__init__(self)

    def encode(self, key, message):
        self.encoded_message = ''
        for i in range(0, len(message)):
            symbol = message[i]
            symbol_index = self.alphabet.index(symbol)
            symbol_index_encoded = (symbol_index*key)
            symbol_encoded = self.alphabet[symbol_index_encoded % 95]
            self.encoded_message += symbol_encoded
        print('Encoded message: ', self.encoded_message)
        return self.encoded_message

    def decode(self, key, message):
        self.decoded_message = ''
        # modular_inverse takes in a key n and and the alphabet length
        _m = crypto_utils.modular_inverse(key, 95)
        # Check if key is valid: meaning check if it has a modulo_inverse
        for i in range(0, len(message)):
            symbol = message[i]
            symbol_index = self.alphabet.index(symbol)
            symbol_index_decoded = ((symbol_index*_m) % 95)
            symbol_decoded = self.alphabet[symbol_index_decoded]
            self.decoded_message += symbol_decoded
        print('Decoded message: ', self.decoded_message)

        return self.decoded_message


# ----------------------- AFFINE CIPHER --------------------


class Affine(Cipher):
    """Subclass of Cipher: Affine encryption"""
    def __init__(self):
        Cipher.__init__(self)

    # Encryption: encode_multiplication(clear:text) -> encode_caesar(enc_mult)
    # key is a tuple; key = (n1, n2); key[0]==n1, key[1]==n2
    # -> n1 is the key for mult_cipher
    # -> n2 is the key for caesar_cipher
    def encode(self, key, message):
        # Reuse the encode-modules from Caesar-class and Mult-class
        # Mult_encode takes the plain message as message-input
        encoded_mult = Multiplication().encode(key[0], message)
        # Caesar_encode takes the mult_encryption as message-input
        encoded_caesar = Caesar().encode(key[1], encoded_mult)
        return encoded_caesar

    # Decryption: decode_caesar(enc_mult) -> decode_mult(decode_caesar)
    def decode(self, key, message):
        decoded_caesar = Caesar().decode(key[1], message)
        decoded_mult = Multiplication().decode(key[0], decoded_caesar)
        return decoded_mult


# ---------------- UNBREAKABLE CIPHER -------------------


class Unbreakable(Cipher):
    """Subclass of Cipher: Unbreakable - encryption"""
    def __init__(self):
        Cipher.__init__(self)

    def encode(self, key, message):
        self.encoded_message = ''
        # Unbreakable-cipher uses a KEYWORD as a key
        for i in range(0, len(message)):
            # SYMBOL INDEXES - finds symbol index:
            symbol = message[i]
            symbol_index = self.alphabet.index(symbol)
            # KEY INDEXES - finds key index:
            key_index = self.alphabet.index(key[i % len(key)])
            # FINAL INDEXES - adds symbol and key index together:
            final_index = symbol_index + key_index

            # ENCODING:
            encoding = self.alphabet[final_index % 95]
            self.encoded_message += encoding

        print('Encoded message: ', self.encoded_message)
        return self.encoded_message

    def decode(self, key, message):
        self.decoded_message = ''
        new_decode_keyword = ''
        # print('Encoded message: ', self.encoded_message)
        # print('Message to decrypt: ', message)
        # Decryption: need new keyword matching encryption_keyword
        # -> e,i : value of i-th symbol in encryption-word
        # -> d,i : value of i-th symbol in decryption-word
        # -> They satisfy: d,i = (alphabet_size - e,i) mod alphabet_size

        # To generate new key, iterate through current_key and find "corresponding" word
        for i in range(0, len(key)):
            symbol = key[i]
            symbol_index = self.alphabet.index(symbol)
            new_decode_keyword += self.alphabet[((95 - symbol_index) % 95)]
        # Have now generated new decryption keyword!
        print('New decryption keyword: ', new_decode_keyword)

        # Decryption is now same as encryption, but with new keyword and encrypted message
        decryption = self.encode(new_decode_keyword, message)
        print('Decoded message: ', decryption)
        return decryption

# -----------------------RSA CIPHER--------------------------


class RSA(Cipher):
    """Subclass of Cipher: RSA encryption"""
    # RSA cipher: keys don't need to match; big pro - harder to hack!
    def __init__(self):
        Cipher.__init__(self)
        self.sender_key = ()
        self.receiver_key = ()

    def generate_keys(self):
        # 1 - generate 2 random primes - can not be the same!!
        _p = crypto_utils.generate_random_prime(8)   # takes bits as ip
        # print('p: ', p)
        _q = crypto_utils.generate_random_prime(8)
        # print('q: ', q)
        # p and q must be different primes
        if _p != _q:
            # 2 - define n and ø
            _n = (_p * _q)
            _o = ((_p - 1) * (_q - 1))   # o replaces ø; ø not ascii
            # 3 - select e randomly between 3 and ø
            _e = random.randint(3, (_o-1))
            # print('e: ', e)
            # print('n: ', n)

            # Want to make sure a modular_inverse exists, does if gcd==1
            if math.gcd(_e, _o) == 1:
                # 4 - set d as mod inverse to e wrt. ø
                _d = crypto_utils.modular_inverse(_e, _o)
                # print('d: ', _d)
                # 5 - after keys have been generated
                # Key sender encrypts messages to be sent to receiver with,
                # can be freely published (public key)
                self.sender_key = (_n, _e)
                # Secret key retained by receiver to decrypt messages
                self.receiver_key = (_n, _d)
                return self.sender_key, self.receiver_key
            else:
                self.generate_keys()
        else:
            # Runs function again to generate new primes if they were equal
            self.generate_keys()

    def encode(self, sender_key, message):
        _n = self.sender_key[0]
        _e = self.sender_key[1]
        # print('n i encode: ', n, ' ; e i encode: ', e)

        # Uses text blocks from utilities; parameters:
        # (message to ble translated to blocks, block size)
        # Blocks from text returns a list of integers, each belonging to a block
        # ex; 'Hallo -> [integer1, integer2, integer3], second param. specifies block-size
        blocks_of_ints = crypto_utils.blocks_from_text(message, 2)
        # c will be the result of the encryption
        _c = []
        for t in blocks_of_ints:
            # print('t:', t)  # t: [integer1, integer2, integer3]
            _c.append(pow(int(t), int(_e), int(_n)))
        print('Encoded message, c: ', _c)
        return _c

    def decode(self, receiver_key, message):
        # message <- integer_blocks from encoder
        # print('Message to be decoded: ', message)
        # print('Receiver_key: ', self.receiver_key[1])
        _n = self.receiver_key[0]
        _d = self.receiver_key[1]
        # print('n i decode: ', n, ' ; d i decode: ', d)

        decrypted_message = []
        t_marked = []
        # remember message is a list of integers c = [int1, int2, ...]
        for _c in message:
            t_marked.append(pow(_c, _d, _n))
        # Texts from blocks takes list of ints, and number_of_bits as parameters
        decrypted_message = crypto_utils.text_from_blocks(t_marked, 16)

        print('Decoded message: ', decrypted_message)
        return decrypted_message
