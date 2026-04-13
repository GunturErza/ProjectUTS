class Node:
  def _init_(self, nama):
    self.nama = nama
    self.next = None

class QueueKlinik:
  def _init_(self):
    self.front = None
    self.rear = None

# Enqueue: Menambahkan Antrian
def enqueue(self, nama):
  new_node = Node(nama)
  if self.rear is None:
    self.front = self.rear = new_node
    printf(f"Pasien {nama} berhasil masuk antrian.")
      return
    self.rear.next = new_node
    self.rear = new_node
    print(f"Pasien {nama} berhasil masuk antrian.")

 # Operasi Dequeue: Memanggil
pasien (Hapus dari depan)
def dequeue(self):
  if self.front is None:
    print("Antrean Kosong!")
    return

temp = self.front
print(f"Memanggil pasien:
{temp.nama}. Silahkan masuk!"
      self.front = self.front.next

      if self.front is None:
      self.rear = None

# Operasi Peek: Lihat pasien terdepan
    def peek(self):
        if self.front:
            print(f"Pasien urutan terdepan: {self.front.nama}")
        else:
            print("Antrean kosong.")
