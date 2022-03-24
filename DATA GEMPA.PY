
# #class dasar

# #Data Gempa Bumi Indonesia dalam 1 tahun terakhir

# class  gempa:
    
#     def __init__(self, area, tanggal, kekuatan):
#         self.area = area
#         self.tanggal = tanggal
#         self.kekuatan = kekuatan
   
#     def tampil(self):
#         print ("Area        : ", self.area)
#         print ("Tanggal     : ", self.tanggal)
#         print ("Kekuatan    : ", self.kekuatan)
        
# a1=  gempa ("Pasaman", "25 Febuari 2022", "6,1 SR")
# a2=  gempa ("Banten", "14 Januari 2022", "6,6 SR")
# a3=  gempa ("Larantuka", "14 Desember 2021", "4,6 SR")
# a4=  gempa ("Bali", "16 Oktober 2021", "4,8 SR")
# a5=  gempa ("Sulawesi Tengah", "26 Juli 2021", "2,6 SR")
# a6=  gempa ("Jawa Timur", "10 April 2021", "6,1 SR")

# print("Data Gempa Bumi Indonesia dalam 1 tahun terakhir")

# print("===== Data  Gempa 1 =====")
# a1.tampil()
# print()
# print("===== Data  Gempa 2 =====")
# a2.tampil()
# print()
# print("===== Data  Gempa 3 =====")
# a3.tampil()
# print()
# print("===== Data  Gempa 4 =====")
# a4.tampil()
# print()
# print("===== Data  Gempa 5 =====")
# a5.tampil()
# print()
# print("===== Data  Gempa 6 =====")
# a6.tampil()
# print()
        
#     # Membuat Inheritance -- Parent-child Class/Super-subsuper Class

class person :
    def __init__(self,alatberat,Merk) :
        self.alatberat = alatberat
        self.Merk = Merk

    def keterangan(self) :
        return(f'saya merekomendasikan {self.alatberat} dengan merk {self.Merk}')

class kualitas(person) :
    def __init__(self,alatberat,Merk,jarak) :
        self.alatberat = alatberat
        self.Merk = Merk
        super().__init__(alatberat,Merk)
        person.__init__(self,alatberat,Merk)
        self.jarak = jarak
    
    def keterangan(self):
        return (f'saya rekomendasikan {self.alatberat} dengan Merk {self.Merk} apabila jaraknya {self.jarak} km')

alat = kualitas('Excavator', 'Hyundai', '300')
print(alat.keterangan())



# #    Membuat Override
# class person :
#     def __init__(self,alatberat,Merk) :
#         self.alatberat = alatberat
#         self.Merk = Merk

#     def keterangan(self) :
#         return(f'saya rekomendasikan {self.alatberat} dengan Merk {self.Merk}')

# class kualitas(person) :
#     def __init__(self,alatberat,Merk,jarak) :
#         self.alatberat = alatberat
#         self.Merk = Merk
#         super().__init__(alatberat,Merk)
#         person.__init__(self,alatberat,Merk)
#         self.jarak = jarak
    
#     def keterangan(self):
#         return (f'saya rekomendasikan {self.alatberat} dengan Merk {self.Merk} apabila jaraknya {self.jarak} km')

# class mesin (person) :
#     def __init__(self,alatberat,Merk,kondisi) :
#         super().__init__(alatberat,Merk)
#         self.kondisi = kondisi  

#     def keterangan(self):
#         return (f'jenis alat berat {self.alatberat} tersedia dalam kondisi {self.kondisi} terutama merk {self.Merk}')

# Forklift = kualitas('volvo', 'TI', '400')  
# bulldozer = mesin('bulldozer', 'hyundai', 'baik')

# print (Forklift.keterangan())
# print (bulldozer.keterangan())

