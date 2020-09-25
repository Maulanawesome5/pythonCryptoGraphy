alphabeth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key = int(input('Masukkan cipher key disini '))
# key yang dimasukkan saat program berjalan adalah angka 1-10
# angka ini sebagai jarak (shift) alphabeth yang akan diacak

def encode(kalimat):
  kalimat = kalimat.lower()
  hasil_encode = ''
  for karakter in kalimat:
    if karakter in alphabeth:
      index_lama = alphabeth.index(karakter)
      index_baru = (index_lama +key) % len(alphabeth)
      alphabeth_baru = alphabeth[index_baru]
      hasil_encode = hasil_encode + alphabeth_baru
    else:
      hasil_encode = hasil_encode + ''
  return hasil_encode

kalimat = input('Masukkan kalimat yang ingin di enkripsi ')
kalimat_hasil = encode(kalimat)
print('Kalimat yang dimasukkan adalah :', kalimat)
print('Hasil enkripsi kalimat menggunakan Caesar Cipher dengan key:',key, 'adalah', kalimat_hasil)
