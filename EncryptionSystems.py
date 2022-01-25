import datetime


class Caeser:
    def __init__(self):
        pass
    def mahoafile (self, srcfile="", desfile="", K=0):
        print(" chạy ")
        m=None
        with open(srcfile,"rb") as file:
            m=file.read()
        with open(desfile, "wb+") as file:
            i=0
            while i < len(m):
                num= (K[0] + m[i])%256
                file.write(num.to_bytes(1, byteorder='big', signed=False))
                i+=1
                print(i)
    def giaimafile (self, srcfile, desfile, K):
        m=None
        with open(srcfile,"rb") as file:
            m=file.read()
        with open(desfile,"wb+") as file:
            i = 0
            while i < len(m):
                num = (m[i]-K[0]) % 256
                file.write(num.to_bytes(1, byteorder='big', signed=False))
                i += 1
class Vigenere:
    def __init__(self):
        pass

    def mahoafile(self, srcfile, desfile, K):
        m = None
        with open(srcfile, "rb") as file:
            m = file.read()
        with open(desfile, "wb") as file:
            i = 0
            while i < len(m):
                num = (m[i] + K[i%len(K)]) % 256
                file.write(num.to_bytes(1, byteorder='big', signed=False))
                i += 1
    def giaimafile(self, srcfile, desfile, K):
        m = None
        with open(srcfile, "rb") as file:
            m = file.read()
        with open(desfile, "wb") as file:
            i = 0
            while i < len(m):
                num = (m[i] - K[i % len(K)]) % 256
                file.write(num.to_bytes(1, byteorder='big', signed=False))
                i += 1
class RC4:
    def __init__(self):
       pass

    def __setup(self, K):
        S= [None]*256
        T= [None]*256
        for i in range(256):
            S[i] = i
            T[i] = ord(K[i % len(K)])
        j = 0
        for i in range(256):
            j = (j + S[i] + T[i]) % 256
            S[i], S[j] = S[j], S[i]
        return S
    def __createK(self, S, step = 1):
        i, j = 0, 0
        key=""
        while len(key)<=step:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            t = (S[i] + S[j]) % 256
            key += str(S[t])
        return key
    def mahoafile(self, srcfile=None, desfile=None, K="0"):
        m = ""
        with open(srcfile,"rb") as file :
            m = file.read()
        with open(desfile,"wb+") as file:
            S = self.__setup(K)
            key = self.__createK(S,len(m))
            i= 0
            while i <len(m):
                m_ = int(key[i])^m[i]
                file.write(m_.to_bytes(1, byteorder='big', signed=False))
                i+=1
    def giaimafile(self, srcfile, desfile, K):
        m = ""
        with open(srcfile, "rb") as file:
            m = file.read()
        with open(desfile, "wb+") as file:
            S = self.__setup(K)
            key = self.__createK(S, len(m))
            for i in range(len(m)):
                m_ = int(key[i]) ^ m[i]
                file.write(m_.to_bytes(1, byteorder='big', signed=False))
# Vigenere = Vigenere()
# Vigenere.mahoafile("file1234.webp", "file1234.webp", [1, 2, 3] )
# Caeser().giaimafile("D:/untitled.mp4", "D:/untitled100.mp4", [123])