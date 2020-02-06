# -*- coding: utf-8 -*-
# Vücut-kitle indeksi ve ideal kilo hesaplama ======

# Kullanıcıdan veri aldığımız bölüm ================
while True:
    b = int(input("Boyunuz (cm): "))
    try:
        b = int(b)
    except ValueError:
        print("Lütfen geçerli bir rakam giriniz")
        continue
    if 100 <= b <= 250:
        break
    else:
        print("Lütfen 100 ve 250 arası bir değer giriniz")

while True:        
    k = int(input("Kilonuz (kg): "))
    try:
        k = int(k)
    except ValueError:
        print("Lütfen geçerli bir rakam giriniz")
        continue
    if 35 <= k <= 200:
        break
    else:
        print("Lütfen 35 ve 200 arası bir rakam giriniz")
        
# Formüller ========================================
index = k/(b/100)**2
ideal = (b-100)-((b-150)/4)

# Ön tanımlar ======================================
vk = "Vücut-kitle indeksiniz: "
er = "İdeal kilonuz (Erkeklerde): "
kd = "İdeal kilonuz (Kadınlarda): "

# Sonucu ekrana yazdırma ==========================
if index < 18.49:
    print(vk, "{0:.2f}, ideal kilonuzun altındasınız." .format (index))
    print(er, "{0:.2f}" .format (ideal))
    print(kd, "{0:.2f}" .format (ideal -5))
    
elif index == 18.50 or index <= 24.99:
    print(vk, "{0:.2f}, ideal kilodasınız." .format (index))
    print(er, "{0:.2f}" .format (ideal))
    print(kd, "{0:.2f}" .format (ideal -5))
    
elif index == 25 or index <= 29.99:
    print(vk, "{0:.2f}, ideal kilonuzun üzerindesiniz." .format (index))
    print(er, "{0:.2f}" .format (ideal))
    print(kd, "{0:.2f}" .format (ideal -5))
    
elif index > 30:
    print(vk, "{0:.2f}, ideal kilonuzun çok üzerindesiniz." .format (index))
    print(er, "{0:.2f}" .format (ideal))
    print(kd, "{0:.2f}" .format (ideal -5))
    