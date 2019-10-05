import base64
import binascii
import json
import random

from Crypto.Cipher import AES

secret_key = b"0CoJUm6Qyw8W8jud"
pub_key = "010001"
modulus = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"


def aes_encrypt(text, key):
    pad = 16 - len(text) % 16
    try:
        text = text.decode()
    except:
        pass
    text = text + pad * chr(pad)
    try:
        text = text.encode()
    except:
        pass
    encryptor = AES.new(key, AES.MODE_CBC, b"0102030405060708")
    ciphertext = encryptor.encrypt(text)
    ciphertext = base64.b64encode(ciphertext)
    return ciphertext


def rsa_encrypt(ran_16, pub_key, modulus):
    text = ran_16[::-1]
    rsa = int(binascii.hexlify(text), 16) ** int(pub_key, 16) % int(modulus, 16)
    return format(rsa, "x").zfill(256)


def encrypt_data(song_id, page):
    data = {
        "rid": "R_SO_4_{0}".format(song_id),
        "offset": str((page - 1) * 20),
        "total": "true" if page == 1 else "false",
        "limit": "20",
        "csrf_token": "",
    }
    ran_16 = bytes("".join(random.sample("1234567890DeepDarkFantasy", 16)), "utf-8")
    text = json.dumps(data)
    params = aes_encrypt(text, secret_key)
    params = aes_encrypt(params, ran_16)
    encseckey = rsa_encrypt(ran_16, pub_key, modulus)
    result = {"params": params.decode(), "encSecKey": encseckey}
    return result
