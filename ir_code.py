import random

low_num = 1
up_num = 99

hads = random.randint(low_num, up_num)

print(hads)
print("aya computer adad zehn shomaro dorost hads zade ?")

pasokh_user = input("(k = hads computer kochik tare) (b = hads computer bozorg tare) (d = hads dorost bod) | : ")

while pasokh_user != "d":
    if pasokh_user == "k":
        hads = random.randint(hads , up_num)
        print(hads)
        print("aya computer adad zehn shomaro dorost hads zade ?")
        pasokh_user = input("(k = hads computer kochik tare) (b = hads computer bozorg tare) (d = hads dorost bod) | : ")
    elif pasokh_user == "b":
        hads = random.randint(low_num, hads)
        print(hads)
        print("aya computer adad zehn shomaro dorost hads zade ?")
        pasokh_user = input("(k = hads computer kochik tare) (b = hads computer bozorg tare) (d = hads dorost bod) | : ")
    else:
        print(hads)
        print("lotfan fqt az horofe (d k b) estefade konid ")
        pasokh_user = input("(k = hads computer kochik tare) (b = hads computer bozorg tare) (d = hads dorost bod) | : ")

print("bazi tamom shod")
