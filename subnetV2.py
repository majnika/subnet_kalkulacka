#Get IP and prefix, check if they are correct
while True:
    try:
        ipLOMENOprefix = input("IP(A.B.C.D)/prefix(8-30): ")
        if ipLOMENOprefix[-1:] == 'ň':
            ipLOMENOprefix = ipLOMENOprefix[:-1]
        ip = (ipLOMENOprefix.split("/"))[0]
        prefix = int((ipLOMENOprefix.split("/"))[1])
        ip = [int(i) for i in ip.split(".")]
        #TODO: The beginning prefix and the desirable prefix
        for i in ip: 
            if -1 > i or i > 255:
                raise ValueError
        if prefix > 30 or prefix < 8: #TODO
            raise ValueError
        oktet = prefix // 8
        if ip[oktet] != 0:
            raise ValueError
        if len(ip) != 4:
            raise ValueError
        break
    except (ValueError, IndexError):
        print("Nesprávny vstup")
        continue

print("________________________________\n")

remainder = prefix - (8 * oktet)

maska = []

miezdu = 0

for i in range(0,oktet):
    maska.append("255")

for i in reversed(range(8 - remainder,8)):
    miezdu = miezdu + (2 ** i)

maska.append(str(miezdu))

for i in range(0,3-oktet):
    maska.append('0')

print("Maska:",".".join(maska))

print(f"\nPočet sieti: {2 ** remainder}\n")

print(f"Počet hostov v jednej sieti je {(2 ** (32 - prefix)) - 2}\n")

magic_number = 256 - int(maska[oktet])

print(f"Magic number je {magic_number}\n")

print("Siete:")

FUHA = [0,0,0,1]
LUHA = []
BR = []

for _ in range(oktet):
    LUHA.append(0)
    BR.append(0)

LUHA.append(magic_number - 2)
BR.append(magic_number-1)

for _ in range(3-oktet):
    LUHA.append(254)
    BR.append(255)

for _ in range(0,2 ** remainder):

    print(f"IP Siete: {ip[0]}.{ip[1]}.{ip[2]}.{ip[3]} \
    FUHA: {ip[0]}.{ip[1] + FUHA[1]}.{ip[2] + FUHA[2]}.{ip[3] + FUHA[3]} \
    LUHA: {ip[0]}.{ip[1] + LUHA[1]}.{ip[2] + LUHA[2]}.{ip[3] + LUHA[3]} \
    Broadcast: {ip[0]}.{ip[1] + BR[1]}.{ip[2] + BR[2]}.{ip[3] + BR[3]}")
    
    ip[oktet] += magic_number
