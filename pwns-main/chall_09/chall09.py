# coding: utf-8
def chall09():
    p = process("./chall_09")
    elf = ELF("./chall_09")
    p.sendline(xor(elf.string(elf.sym.key), b'\x69')+ b"\x00")
    p.interactive()
chall09()
def chall09():
    p = process("./chall_09")
    elf = ELF("./chall_09")
    p.send(xor(elf.string(elf.sym.key), b'\x69')+ b"\x00\n")
    p.interactive()
chall09()
