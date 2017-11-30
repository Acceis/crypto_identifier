# crypto-identifier

Crypto tool for pentest and ctf : try to uncipher data using multiple algorithms and block chaining modes.
Usefull for a quick check on unknown cipher text and key dictionnary

Supported Algorithms :
 - AES
 - ARC2
 - ARC4
 - Blowfish
 - CAST
 - DES
 - DES3
 - XOR

Supported modes :
 - ECB
 - CBC
 - CFB
 - OFB
 - OPENPGP

## Usage:
```
python ./crypto_identifier.py --help
usage: crypto_identifier.py [-h] --input INPUT [--key KEY] [--keys KEYS]
                            [--printable] [--grep GREP]
                            [--algo {ARC4,CAST,AES,XOR,ARC2,DES,Blowfish,DES3}]
                            [--mode {ECB,CBC,CFB,OFB,OPENPGP}]

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
                        input string (base64)
  --key KEY, -k KEY     key string
  --keys KEYS, -ks KEYS
                        keys file
  --printable, -p       display only printable results
  --grep GREP, -g GREP  grep string in results
  --algo {ARC4,CAST,AES,XOR,ARC2,DES,Blowfish,DES3}, -a {ARC4,CAST,AES,XOR,ARC2,DES,Blowfish,DES3}
                        cipher algo to use
  --mode {ECB,CBC,CFB,OFB,OPENPGP}, -m {ECB,CBC,CFB,OFB,OPENPGP}
                        block chaining mode to use

```
## Examples :

### Multi ciphers + modes
`python ./crypto_identifier.py --input "WpbizgqtUDjD5TV5ELVswFL92ao3T41T" --key secret`

```
ARC4Cipher : secret (with IV): '\xb7\xa00\xd2\x88\t\x86\x9e\xf1.\x8e\xa5\xe3S\x99\xf7\xff\xca\xabH\xb4\xbcI\x0f'
CAST128Cipher (ECB) : secret (with IV): '\xc7\xcby\r\xd4\xe6\xcf\xa7\x95\x12(\x8d0_O8\xc7\xb6\x1f\x9b\xc1\xbd5\xe0'
CAST128Cipher (CBC) : secret (with IV): '\x9d]\x9b\xc3\xdeK\x9f\x9f\xcf\x84\xcaC:\xf2\x1f\x00\x04S*\xe2\xd1\x08Y '
CAST128Cipher (CFB) : secret (with IV): '\x96\x08:\xe6\xe1\xe9\x0c\xf1\x0f\nF\x83\xd6\xbe\x942\xc4\xcco\x11p\xa7\x81\xd5'
CAST128Cipher (OFB) : secret (with IV): '\x96\x88\x06\xb6\xc8T\xd1\xe0P\x04\xd9\x8d\xda\x8cJhh\xc3s\xbc@%\xb9O'
AESCipher (CFB) : secret (with IV): '<#\xa8,\x82|\xeb6F\xc8\x06\xab\xe4\xfcc\x004V\xfb{F\xc2\xcf?'
XORCipher : secret (with IV): ")\xf3\x81\xbco\xd9#]\xa0\x97P\rc\xd0\x0f\xb27\x89\xaa\xcfT=\xe8'"
ARC2 (ECB) : secret (with IV): '\x97 \xb6\x9b\xb5Z\x8a\xdc\xab4\x8ac\x93  \xe6\xca\x19\xe7\x15M\x7f\xa7\xe8'
ARC2 (CBC) : secret (with IV): '\xcd\xb6TU\xbf\xf7\xda\xe4\xf1\xa2h\xad\x99\x8dp\xde\t\xfc\xd2l]\xca\xcb('
ARC2 (CFB) : secret (with IV): '!8X\x93\x04\x9f\xcb\xf2\xb8\x06r\xaa\x0fX\x8c\x92)\x00\xc0\xed\x0e\xa8\x0e\xa7'
ARC2 (OFB) : secret (with IV): '!D\xaa\x8ea\xd0Z[\x08\xfc6\xec\x0b\xfb\x81\x825\xf2\x8b,[\xd1\xa2\x8b'
DESCipher (ECB) : secret (with IV): 'This is a DES test case\x00'
DESCipher (CBC) : secret (with IV): '\x0e\xfe\x8b\xbd*\xc4#\x18;\xb6\xa6\x8bY\x8d$]\xb0\x91\x15\x1aq\xc6\t\xc0'
DESCipher (CFB) : secret (with IV): 'Y\xa4\x92\x13\x11\x16WS\xc0\x06\xe6\x7fl\xae\x8bv\xee\xcf\x8c[\x88\x07!\x07'
DESCipher (OFB) : secret (with IV): 'Y\xf5\xa2\xd0\x05\x0e\xe8\xd1n(/\xd4\n\xea\xc7\x13\xf0\xcd\x01\xecn\xcf<r'
BlowfishCipher (ECB) : secret (with IV): '\xac\xb6\xcbz\xe8\xd76\x91\x1eBkl\xbe\x14\x81\x8c9*\xaa\xee\xebW-3'
BlowfishCipher (CBC) : secret (with IV): '\xf6 )\xb4\xe2zf\xa9D\xd4\x89\xa2\xb4\xb9\xd1\xb4\xfa\xcf\x9f\x97\xfb\xe2A\xf3'
BlowfishCipher (CFB) : secret (with IV): '\x1a?\xe4\xcaJ\xffe\x88\x83\xf59\xea`-\xfdd8KN\xb0\xcfYo\xef'
BlowfishCipher (OFB) : secret (with IV): '\x1a\xa2\x81\xb6\xc5\xb5b\xf1\xfaH\xd9G\xc9\x88A\x0c\x85\xd2k\xc2\x82I\x13"'
DES3Cipher (ECB) : secret (with IV): "\x90\xc9\xa5\xd0\x18)'\x94<\x00ml\xa0\xc1\x84\\\xcf\x1e,o'\xbd\xa1\xa8"
DES3Cipher (CBC) : secret (with IV): '\xca_G\x1e\x12\x84w\xacf\x96\x8f\xa2\xaal\xd4d\x0c\xfb\x19\x167\x08\xcdh'
DES3Cipher (CFB) : secret (with IV): '\x17rK"|\xd9\xbe\xad\x8e\xe2\x04\x9a\xaa\x08\xedJ\xfd%(\xa2F\x92\x06\xa9'
DES3Cipher (OFB) : secret (with IV): '\x17 \xfc\xaf\xd4C\xf9\xf7\x82\xdf\x87\xeb\xf9F;\xd5)\x14\xe6\xff\xcd\xa5\xbf\xed'
ARC4Cipher : secret : '\xb7\xa00\xd2\x88\t\x86\x9e\xf1.\x8e\xa5\xe3S\x99\xf7\xff\xca\xabH\xb4\xbcI\x0f'
CAST128Cipher (ECB) : secret : '\xc7\xcby\r\xd4\xe6\xcf\xa7\x95\x12(\x8d0_O8\xc7\xb6\x1f\x9b\xc1\xbd5\xe0'
XORCipher : secret : ")\xf3\x81\xbco\xd9#]\xa0\x97P\rc\xd0\x0f\xb27\x89\xaa\xcfT=\xe8'"
ARC2 (ECB) : secret : '\x97 \xb6\x9b\xb5Z\x8a\xdc\xab4\x8ac\x93  \xe6\xca\x19\xe7\x15M\x7f\xa7\xe8'
DESCipher (ECB) : secret : 'This is a DES test case\x00'
BlowfishCipher (ECB) : secret : '\xac\xb6\xcbz\xe8\xd76\x91\x1eBkl\xbe\x14\x81\x8c9*\xaa\xee\xebW-3'
DES3Cipher (ECB) : secret : "\x90\xc9\xa5\xd0\x18)'\x94<\x00ml\xa0\xc1\x84\\\xcf\x1e,o'\xbd\xa1\xa8"
```

### Multi ciphers + modes, print only printable results
`python ./crypto_identifier.py --input "WpbizgqtUDjD5TV5ELVswFL92ao3T41T" --key secret --printable`

```
DESCipher (ECB) : secret (with IV): This is a DES test case
DESCipher (ECB) : secret : This is a DES test case
```

### Single cipher / single mode
`python ./crypto_identifier.py --input "WpbizgqtUDjD5TV5ELVswFL92ao3T41T" --key secret --algo DES --mode ECB`

```
DESCipher (ECB) : secret (with IV): 'This is a DES test case\x00'
DESCipher (ECB) : secret : 'This is a DES test case\x00'
```

### using a dictionnary as keys
`python ./crypto_identifier.py --input "WpbizgqtUDjD5TV5ELVswFL92ao3T41T" --keys ./500-worst-passwords.txt --printable`

```
DESCipher (ECB) : secret (with IV): This is a DES test case
DESCipher (ECB) : secret : This is a DES test case
ARC4Cipher : rabbit (with IV): 3gb-q%$7<NM.
ARC4Cipher : rabbit : 3gb-q%$7<NM.
```

## Requirements:
 Python 2.7 / 3.x
 - Argparse
 - Crypto

## License
```
----------------------------------------------------------------------------
"THE BEER-WARE LICENSE" (Revision 42):
Ganapati (@G4N4P4T1) wrote this file. As long as you retain this notice you
can do whatever you want with this stuff. If we meet some day, and you think
this stuff is worth it, you can buy me a beer in return.
----------------------------------------------------------------------------
```
