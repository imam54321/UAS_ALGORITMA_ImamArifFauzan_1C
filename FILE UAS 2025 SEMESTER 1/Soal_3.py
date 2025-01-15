class Queue:
    def __init__(self):
        self.nomor=[]

    def Tampilan():
        print('''   
            Pilih Operasi
              1.Tambahkan
              2.Hapus

''')

    def Enqueue(self,enqueue):
        self.nomor.append(enqueue)
    def Dequeue(self):
        self.nomor.pop()
        