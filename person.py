"""Person file"""
import cipher as ci


class Person:
    """Superclass for sender, receiver and hacker"""

    # Person is initialized to having a specified cipher and will later get a key
    def __init__(self, key, cipher):
        self.key = key
        self.cipher = cipher     # A cipher algorithm from a Cipher-subclass

    def set_key(self, key):
        """Method for sender to generate key"""
        self.key = key
        return key

    def get_key(self):
        """Method for receiver to access key, just returns self.key"""
        return self.key

    def operate_cipher(self, message):
        """Method to operate a cipher"""
        return

    def intercept_keys(self, cipher):
        """Method for Hacker to obtain all potential keys from ciphers"""
        return

    def intercept_message(self, intercepted_message):
        """Method for Hacker to attempt decryption of an intercepted message"""
        return

# ---------------------------SENDER------------------------------------------


class Sender(Person):
    """Subclass of Person: Sends an encrypted message"""

    def __init__(self, key, cipher):
        Person.__init__(self, key, cipher)

    def set_key(self, key):
        """Method for sender to generate key"""
        return

    # Sender uses operate_cipher to ENCRYPT text
    def operate_cipher(self, message):
        cipher = self.cipher    # Set to the the cipher in use
        encryption = cipher.encode(self.key, message)

        return encryption

# -------------------------RECEIVER------------------------------------------


class Receiver(Person):
    """Subclass of Person: Receives an encrypted message and decrypts it"""
    def __init__(self, key, cipher):
        Person.__init__(self, key, cipher)

    def get_key(self):
        """Method for receiver to access key, just returns self.key"""
        return self.key

    # Receiver uses operate_cipher to DECRYPT text
    def operate_cipher(self, message):
        cipher = self.cipher        # Set to the cipher in use
        decryption = cipher.decode(self.key, message)

        return decryption


# -------------------------- HACKER --------------------------------------------


class Hacker(Person):
    """Subclass of Person: Hacker will try to break the encrypted message by force"""
    def __init__(self, cipher):
        # Person.__init__(self, cipher)
        self.cipher = cipher                    # Refers to the cipher we're trying to hack
        file = open('english_words.txt', 'r')   # Reads the english-dictionary file
        self.dictionary = [(word.replace('\n', "")) for line in file for word in line.split()]
        # The dictionary is a list of english words, free of surrounding symbols
        # -> self.dictionary = [ab, abc, ba, bb, ca, cb, cc, ..]
        # Removed '\n' and apostrophes from file so words in file are comparable

    def intercept_keys(self, cipher):
        """Method for finding ALL keys that can be used to hack the different ciphers"""
        # cipher parameter refers to the cipher the message is encrypted with
        # Finds ALL the potential keys for the respective ciphers

        # Potential_keys for caesar - any index in alphabet
        if isinstance(cipher, ci.Caesar):
            potential_keys = []
            for i in range(96):
                potential_keys.append(i)
            # print('potential_keys_caesar: ', potential_keys)
            return potential_keys

        # Potential_keys for multiplication - any index in alphabet
        elif isinstance(cipher, ci.Multiplication):
            potential_keys = []
            for i in range(96):
                potential_keys.append(i)
            # print('potential_keys_mult: ', potential_keys)
            return potential_keys

        # Potential_keys for affine - tuple of two integers between [0, 95]
        elif isinstance(cipher, ci.Affine):
            potential_keys = []
            potential_keys = [(key1, key2) for key1 in range(96) for key2 in range(96)]
            # print('potential_keys_affine: ', potential_keys)
            return potential_keys

        # Potential_keys for unbreakable - any word in the english dictionary
        elif isinstance(cipher, ci.Unbreakable):
            potential_keys = []
            for i in self.dictionary:
                potential_keys.append(i)
            # print('potential_keys_unbreakable: ', potential_keys)
            return potential_keys

    def intercept_message(self, intercepted_message):
        """Method for hacking the different ciphers by trying out all keys"""

        # When all potential keys are attained, iterate them in an attempt to hack encrypted message
        potential_keys = self.intercept_keys(self.cipher)

        # We iterate through the keys to try decoding the encryption with all potential keys
        for key in potential_keys:
            # print('Current_key: ', key)
            decoded_message = self.cipher.decode(key, intercepted_message)

            # We search dictionary looking for the decoded_message
            if decoded_message in self.dictionary:
                print('Word in dictionary matches decryption!')
                print('Hacked message: ', decoded_message)
                break
            else:
                print('No word in dictionary matches decryption.')
        return
