import time


timein=int(input("süre giriniz. (saniye cinsinden"))

for i in range(timein, 0, -1):
    print(f"Geri sayım: {i} saniye kaldı...", end='\r')
    time.sleep(1)

print("Süre doldu!")