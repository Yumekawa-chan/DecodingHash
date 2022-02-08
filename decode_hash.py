import hashlib

print("求めたいハッシュ値を入力してください（平文は英数字6文字に限る）")
a = input()

moji = "abcdefghijklmnopqrstuvwxyz0123456789"
leng = len(moji)
num = 0
print("計算中......")

for i in range(leng):
     for j in range(leng):
          for k in range(leng):
               for l in range(leng):
                    for m in range(leng):
                         for n in range(leng):
                              char = moji[i]+moji[j]+moji[k]+moji[l]+moji[m]+moji[n]
                              sha1 = hashlib.sha1(char.encode()).hexdigest()
                              sha224 = hashlib.sha224(char.encode()).hexdigest()
                              sha256 = hashlib.sha256(char.encode()).hexdigest()
                              sha512 = hashlib.sha512(char.encode()).hexdigest()
                              md5 = hashlib.md5(char.encode()).hexdigest()
                              num += 1
                              print(num,char)
                              if a == sha1:
                                   print("ハッシュ形式:sha1")
                                   print(char)
                                   exit()
                              if a == sha224:
                                   print("ハッシュ形式:sha224")
                                   print(char)
                                   exit()
                              if a == sha256:
                                   print("ハッシュ形式:sha256")
                                   print(char)
                                   exit()
                              if a == sha512:
                                   print("ハッシュ形式:sha512")
                                   print(char)
                                   exit()
                              if a == md5:
                                   print("ハッシュ形式:md5")
                                   print(char)
                                   exit()

                    
                         
