class Buah :
    def __init__(self,nama,rasa,warna):
        self.nama=nama
        self.rasa= rasa
        self.warna=warna
    def setNama(self,name):
        self.nama= name
    def information(self):
        return f'Nama buah{self.nama} Warna buah{self.warna}Rasa buah{self.rasa}'
buah1 = Buah('Apel','Merah','Manis')
buah1.setNama('Pisang')
print(buah1)
   