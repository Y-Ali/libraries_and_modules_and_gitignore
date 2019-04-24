import os
import hmac
working_dir = os.getcwd()

print(working_dir)

def encode_py(file):
    return os.fsdecode(file)


def decode_py(file):
    return os.fsdecode(file)




a =(encode_py("libraries_intro"))
b = encode_py("slfjesi34")
c = a+b
print(c)
