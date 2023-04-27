def sifre(a, b): 
  x,y, u,v = 0,1, 1,0
  while a != 0: 
    q, r = b//a, b%a 
    m, n = x-u*q, y-v*q 
    b,a, x,y, u,v = a,r, u,v, m,n 
  giris = b 
  return giris, x, y 
def modinv(a, m): 
  giris, x, y = sifre(a, m) 
  if giris != 1: 
    return None 
  else: 
    return x % m 
def encrypt(text, key): 
  return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) + ord('A')) for t in text.upper().replace(' ', '') ]) 
def decrypt(cipher, key): 
  return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher ]) 
def main(): 
  text = input('Şifrelenecek Metni Girin:')
  key = [7, 20] 
  enc_text = encrypt(text, key) 
  print('Şifreli Metin: {}'.format(enc_text)) 
  print('Şifresi Çözülmüş Metin: {}'.format(decrypt(enc_text, key) )) 
if __name__ == '__main__': 
  main() 