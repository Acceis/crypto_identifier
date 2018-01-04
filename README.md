# crypto-identifier

Crypto tool for pentest and ctf : try to uncipher data using multiple algorithms and block chaining modes.
Usefull for a quick check on unknown cipher text and key dictionary

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

## Usage:
```
python ./crypto_identifier.py --help
usage: crypto_identifier.py [-h] --input INPUT [--key KEY] [--keys KEYS]
                            [--printable] [--grep GREP]
                            [--algo {ARC4,CAST,AES,XOR,ARC2,DES,Blowfish,DES3}]
                            [--mode {ECB,CBC,CFB,OFB}]

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
  --mode {ECB,CBC,CFB,OFB}, -m {ECB,CBC,CFB,OFB}
                        block chaining mode to use

```
## Examples :

### Multi ciphers + modes
`python ./crypto_identifier.py --input "WpbizgqtUDjD5TV5ELVswFL92ao3T41T" --key secret`

```
CAST128Cipher (ECB) : secret (with IV): '\x95\x12(\x8d0_O8\xc7\xb6\x1f\x9b\xc1\xbd5\xe0'
CAST128Cipher (CBC) : secret (with IV): '\xcf\x84\xcaC:\xf2\x1f\x00\x04S*\xe2\xd1\x08Y '
CAST128Cipher (CFB) : secret (with IV): '\x0f\nF\x83\xd6\xbe\x942\xc4\xcco\x11p\xa7\x81\xd5'
CAST128Cipher (OFB) : secret (with IV): '\x0f\xfb\xd1\x01\xd2L\xed\x18\xc1\x1c5^\xfdv\xab\xfb'
AESCipher (CFB) : secret (with IV): '\x14\xa9%\xfdN\xa3F\xbf\x9b7,0@"\xf6\xb14V\xfb{F\xc2\xcf?'
ARC2 (ECB) : secret (with IV): '\xab4\x8ac\x93  \xe6\xca\x19\xe7\x15M\x7f\xa7\xe8'
ARC2 (CBC) : secret (with IV): '\xf1\xa2h\xad\x99\x8dp\xde\t\xfc\xd2l]\xca\xcb('
ARC2 (CFB) : secret (with IV): '\xb8\x06r\xaa\x0fX\x8c\x92)\x00\xc0\xed\x0e\xa8\x0e\xa7'
ARC2 (OFB) : secret (with IV): '\xb87}9{\xc8f\xa3\x99\xe4\xda?,\x01`\x11'
DESCipher (ECB) : secret (with IV): 'a DES test case'
DESCipher (CBC) : secret (with IV): ';\xb6\xa6\x8bY\x8d$]\xb0\x91\x15\x1aq\xc6\t\xc0'
DESCipher (CFB) : secret (with IV): '\xc0\x06\xe6\x7fl\xae\x8bv\xee\xcf\x8c[\x88\x07!\x07'
DESCipher (OFB) : secret (with IV): '\xc0\x86ug\x1f\x16\xd4)\xff0\xc3\x07-\x10&\x80'
BlowfishCipher (ECB) : secret (with IV): '\x1eBkl\xbe\x14\x81\x8c9*\xaa\xee\xebW-3'
BlowfishCipher (CBC) : secret (with IV): 'D\xd4\x89\xa2\xb4\xb9\xd1\xb4\xfa\xcf\x9f\x97\xfb\xe2A\xf3'
BlowfishCipher (CFB) : secret (with IV): '\x83\xf59\xea`-\xfdd8KN\xb0\xcfYo\xef'
BlowfishCipher (OFB) : secret (with IV): '\x83\xd1V\x01\xdf\xad^\tkP5\x94\xeer\xa0\x9f'
DES3Cipher (ECB) : secret (with IV): "<\x00ml\xa0\xc1\x84\\\xcf\x1e,o'\xbd\xa1\xa8"
DES3Cipher (CBC) : secret (with IV): 'f\x96\x8f\xa2\xaal\xd4d\x0c\xfb\x19\x167\x08\xcdh'
DES3Cipher (CFB) : secret (with IV): '\x8e\xe2\x04\x9a\xaa\x08\xedJ\xfd%(\xa2F\x92\x06\xa9'
DES3Cipher (OFB) : secret (with IV): '\x8eS+\x18\xce[\xc5\x0f\x13\xc7k8\xde\xbc\xdaF'
ARC4Cipher : secret : '\xb7\xa00\xd2\x88\t\x86\x9e\xf1.\x8e\xa5\xe3S\x99\xf7\xff\xca\xabH\xb4\xbcI\x0f'
CAST128Cipher (ECB) : secret : '\xc7\xcby\r\xd4\xe6\xcf\xa7\x95\x12(\x8d0_O8\xc7\xb6\x1f\x9b\xc1\xbd5\xe0'
CAST128Cipher (CBC) : secret : '\xc7\xcby\r\xd4\xe6\xcf\xa7\xcf\x84\xcaC:\xf2\x1f\x00\x04S*\xe2\xd1\x08Y '
CAST128Cipher (CFB) : secret : '\xc6\xa4<\xf0>\xe3\x1dg\x0f\nF\x83\xd6\xbe\x942\xc4\xcco\x11p\xa7\x81\xd5'
CAST128Cipher (OFB) : secret : '\xc6\x8a"?\xd5#=\x9931;a\xdaB\xd0v\xcbQ>6+L\xc1\x9d'
AESCipher (CFB) : secret : '\x14\xa9%\xfdN\xa3F\xbf\x9b7,0@"\xf6\xb14V\xfb{F\xc2\xcf?'
XORCipher : secret : ")\xf3\x81\xbco\xd9#]\xa0\x97P\rc\xd0\x0f\xb27\x89\xaa\xcfT=\xe8'"
ARC2 (ECB) : secret : '\x97 \xb6\x9b\xb5Z\x8a\xdc\xab4\x8ac\x93  \xe6\xca\x19\xe7\x15M\x7f\xa7\xe8'
ARC2 (CBC) : secret : '\x97 \xb6\x9b\xb5Z\x8a\xdc\xf1\xa2h\xad\x99\x8dp\xde\t\xfc\xd2l]\xca\xcb('
ARC2 (CFB) : secret : 'U\xef\x12x\x0b\x88\x87*\xb8\x06r\xaa\x0fX\x8c\x92)\x00\xc0\xed\x0e\xa8\x0e\xa7'
ARC2 (OFB) : secret : 'U\r\x86r\xfc|2\xbf\xfb\xb0\xa2\xaf\xba\xe0\xad\x8f6\x9aY\xd9\x926\x8c{'
DESCipher (ECB) : secret : 'This is a DES test case'
DESCipher (CBC) : secret : 'This is ;\xb6\xa6\x8bY\x8d$]\xb0\x91\x15\x1aq\xc6\t\xc0'
DESCipher (CFB) : secret : '>>\xd2\xfd\xe4\xf0!y\xc0\x06\xe6\x7fl\xae\x8bv\xee\xcf\x8c[\x88\x07!\x07'
DESCipher (OFB) : secret : '>\x1942H\x03\x04\xd6\x9a\xbd2v\x9b\x16\x19\r\xb0\xe5&\x1e(\xce\x0f\x12'
BlowfishCipher (ECB) : secret : '\xac\xb6\xcbz\xe8\xd76\x91\x1eBkl\xbe\x14\x81\x8c9*\xaa\xee\xebW-3'
BlowfishCipher (CBC) : secret : '\xac\xb6\xcbz\xe8\xd76\x91D\xd4\x89\xa2\xb4\xb9\xd1\xb4\xfa\xcf\x9f\x97\xfb\xe2A\xf3'
BlowfishCipher (CFB) : secret : '#X\xe0\rS\xf0y\xfe\x83\xf59\xea`-\xfdd8KN\xb0\xcfYo\xef'
BlowfishCipher (OFB) : secret : '#?\xa1\x06T\x7f\x98\x19\x0b\x000\xf3\x1a\xa9\x08.\x94\x8f\xd1a\x9c\x16\xe6\xb1'
DES3Cipher (ECB) : secret : "\x90\xc9\xa5\xd0\x18)'\x94<\x00ml\xa0\xc1\x84\\\xcf\x1e,o'\xbd\xa1\xa8"
DES3Cipher (CBC) : secret : "\x90\xc9\xa5\xd0\x18)'\x94f\x96\x8f\xa2\xaal\xd4d\x0c\xfb\x19\x167\x08\xcdh"
DES3Cipher (CFB) : secret : 'zp-\x9d\xb5\xe8R\x1a\x8e\xe2\x04\x9a\xaa\x08\xedJ\xfd%(\xa2F\x92\x06\xa9'
DES3Cipher (OFB) : secret : 'z\xe1DY\x07\x17#Y6n\xbf\xd8\x15%\xbc\x0f<M\x9c\xa60I\x9a\xbe'
```

### Multi ciphers + modes, print only printable results
`python ./crypto_identifier.py --input "WpbizgqtUDjD5TV5ELVswFL92ao3T41T" --key secret --printable`

```
DESCipher (ECB) : secret (with IV): a DES test case
DESCipher (ECB) : secret : This is a DES test case
```

### Single cipher / single mode
`python ./crypto_identifier.py --input "WpbizgqtUDjD5TV5ELVswFL92ao3T41T" --key secret --algo DES --mode ECB`

```
DESCipher (ECB) : secret (with IV): 'a DES test case'
DESCipher (ECB) : secret : 'This is a DES test case'
```

### using a dictionary as keys
`python ./crypto_identifier.py --input "WpbizgqtUDjD5TV5ELVswFL92ao3T41T" --keys ./500-worst-passwords.txt --printable`

```
DESCipher (ECB) : secret (with IV): a DES test case
DESCipher (ECB) : secret : This is a DES test case
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
