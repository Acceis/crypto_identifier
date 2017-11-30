#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
----------------------------------------------------------------------------
"THE BEER-WARE LICENSE" (Revision 42):
Ganapati (@G4N4P4T1) wrote this file. As long as you retain this notice you
can do whatever you want with this stuff. If we meet some day, and you think
this stuff is worth it, you can buy me a beer in return.
----------------------------------------------------------------------------
"""

from Crypto.Cipher import AES, ARC2, ARC4, Blowfish, CAST, DES, DES3, XOR
from Crypto.Cipher import blockalgo
from Crypto import Random
import argparse
import base64
import string
import sys
import re

CIPHER_LIST = {"AES": {"algo": AES, "type": "block"},
               "ARC2": {"algo": ARC2, "type": "block"},
               "ARC4": {"algo": ARC4, "type": "stream"},
               "Blowfish": {"algo": Blowfish, "type": "block"},
               "CAST": {"algo": CAST, "type": "block"},
               "DES": {"algo": DES, "type": "block"},
               "DES3": {"algo": DES3, "type": "block"},
               "XOR": {"algo": XOR, "type": "stream"}}

MODES = {blockalgo.MODE_ECB: "ECB",
         blockalgo.MODE_CBC: "CBC",
         blockalgo.MODE_CFB: "CFB",
         blockalgo.MODE_OFB: "OFB",
         blockalgo.MODE_OPENPGP: "OPENPGP"}

CHARSET = string.ascii_letters + string.digits + string.punctuation
NON_CHARSET = ''.join(chr(i) for i in range(256) if chr(i) not in CHARSET)


def get_cipher(algo, mode=blockalgo.MODE_ECB):
    """ Return correct cipher class (block or stream)
    """
    if algo in [AES, ARC2, Blowfish, CAST, DES, DES3]:
        return BlockCipher(algo, mode)
    elif algo in [ARC4, XOR]:
        return StreamCipher(algo)


class BlockCipher():
    def __init__(self, algo, mode=blockalgo.MODE_ECB):
        """ Set block cipher algo with mode
        """
        self.mode = mode
        self.algo = algo
        block_size = self.algo.block_size
        self.pad = lambda s: s + (block_size - len(s) % block_size) * \
            chr(block_size - len(s) % block_size)
        self.unpad = lambda s: s[:-ord(s[len(s) - 1:])]

    def encrypt(self, plain, key, iv=None):
        """ Return encrypted value of plain with key and iv
        """
        self.key = self.set_key_length(key)
        if iv is None:
            iv = Random.new().read(self.algo.block_size)

        padded_plain = self.pad(plain)
        if iv != "":
            algo = self.algo.new(self.key, self.mode, iv)
        else:
            algo = self.algo.new(self.key, self.mode)

        return "%s%s" % (iv, algo.encrypt(padded_plain))

    def decrypt(self, cipher, key, iv=False):
        """ Return decrypted value of cipher with key
        """
        self.key = self.set_key_length(key)
        if not iv:
            algo = self.algo.new(self.key, self.mode)
            return algo.decrypt(cipher)
        else:
            algo = self.algo.new(self.key, self.mode,
                                 IV=cipher[:self.algo.block_size])
            return algo.decrypt(cipher)

    def set_key_length(self, key):
        """ Adjust key length to cipher restrictions by padding with \0
        """
        try:
            for size in self.algo.key_size:
                if len(key) < size:
                    return "%s%s" % (key, ("\0" * (size - len(key))))
        except TypeError:
            return "%s%s" % (key, ("\0" * (self.algo.key_size - len(key))))

    def __str__(self):
        """ Return a printable information string about cipher
        """
        name = dir(self.algo)[0]
        name = name if name is not "MODE_CBC" else "ARC2"
        return "%s (%s)" % (name, MODES[self.mode])


class StreamCipher():
    def __init__(self, algo):
        """ Set stream cipher algo
        """
        self.algo = algo

    def encrypt(self, key, plain):
        """ Return encrypted value of cipher with key
        """
        key = self.set_key_length(key)
        algo = self.algo.new(key)
        return algo.encrypt(plain)

    def decrypt(self, cipher, key, iv=False):
        """ Return decrypted value of cipher with key
        """
        key = self.set_key_length(key)
        algo = self.algo.new(key)
        return algo.decrypt(cipher)

    def set_key_length(self, key):
        """ Adjust key length to cipher restrictions by padding with \0
        """
        if len(key) > max(self.algo.key_size):
            return key[:self.algo.key_size]
        else:
            return key

    def __str__(self):
        """ Return a printable information string about cipher
        """
        return "%s" % (dir(self.algo)[0])


def loop_algos():
    """ Iterate over all ciphers algos
    """
    for name, infos in CIPHER_LIST.items():
        if infos["type"] == "block":
            for mode in MODES.keys():
                algo = get_cipher(infos["algo"], mode)
                yield algo
        else:
            algo = get_cipher(infos["algo"])
            yield algo


def get_printable(text):
    """ Return string if a ascii word of len >= len(text)/2 match
        if not, return None
    """
    limit = len(text) / 2

    pattern = re.compile(b'[^\x00-\x1F\x7F-\xFF]{%d,}' % limit)
    r = pattern.findall(text)

    if len(r) > 0:
        return r[0].decode("UTF-8")
    else:
        return None


if __name__ == "__main__":
    """ Entrypoint
    """
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input',
                        '-i',
                        help='input string (base64)',
                        required=True)
    parser.add_argument('--key',
                        '-k',
                        help='key string')
    parser.add_argument('--keys',
                        '-ks',
                        help='keys file')
    parser.add_argument('--printable',
                        '-p',
                        help='diplay only printable results',
                        action='store_true')
    parser.add_argument('--grep',
                        '-g',
                        help='diplay only printable results')
    parser.add_argument('--algo',
                        '-a',
                        help='cipher algo to use',
                        choices=CIPHER_LIST.keys())
    parser.add_argument('--mode',
                        '-m',
                        help='block chaining mode to use',
                        choices=MODES.values())

    args = parser.parse_args()

    # Check required params
    if not args.key and not args.keys:
        print("argument --key [PASSWORD] or --keys [FILE] is required")
        sys.exit(1)

    # Decode input message
    input_text = base64.b64decode(args.input)

    # Handle single password or password file
    if args.key:
        keys = [args.key]
    else:
        keys = []
        with open(args.keys, "r") as keys_fd:
            for candidate_key in keys_fd.readlines():
                keys.append(candidate_key.strip())

    # Single block chaining mode settings
    if args.mode is not None:
        tmp_mode = {k: v for k, v in MODES.items() if v == args.mode}
        MODES = tmp_mode

    # Single cipher algo settings
    if args.algo is not None:
        tmp_algo = CIPHER_LIST[args.algo]
        CIPHER_LIST = {args.algo: tmp_algo}

    # Main loop
    for key in keys:
        for iv in [True, False]:
            iv_str = "(with IV)" if iv else ""
            for algo in loop_algos():
                try:
                    result = algo.decrypt(input_text, key, iv)
                    if args.printable:
                        result = get_printable(result)
                        if result is not None:
                            if args.grep:
                                if args.grep in result:
                                    print("%s : %s %s: %s" % (algo,
                                                              key,
                                                              iv_str,
                                                              result))
                            else:
                                print("%s : %s %s: %s" % (algo,
                                                          key,
                                                          iv_str,
                                                          result))
                    else:
                        if result != '':
                            if args.grep:
                                if args.grep in result:
                                    print("%s : %s %s: %s" % (algo,
                                                              key,
                                                              iv_str,
                                                              repr(result)))
                            else:
                                print("%s : %s %s: %s" % (algo,
                                                          key,
                                                          iv_str,
                                                          repr(result)))
                except Exception as e:
                    """ Silently pass all cipher errors like keys limits
                        and non-compatible algo/modes
                    """
                    pass
