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

# Operasi Display: Tampilkan semua antrean
    def display(self):
        if self.front is None:
            print("Tidak ada antrean saat ini.")
            return
        
        print("\n--- DAFTAR ANTREAN SAAT INI ---")
        curr = self.front
        while curr:
            print(f"- {curr.nama}")
            curr = curr.next
            
        print("------------------------------")

# Fungsi Utama untuk Menjalankan Program
def main():
    klinik = QueueKlinik()
    
    while True:
        print("\n=== SISTEM ANTREAN KLINIK (PYTHON) ===")
        print("1. Tambah Pasien (Enqueue)")
        print("2. Panggil Pasien (Dequeue)")
        print("3. Lihat Pasien Terdepan (Peek)")
        print("4. Lihat Semua Antrean (Display)")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            nama = input("Masukkan nama pasien: ")
            klinik.enqueue(nama)
        elif pilihan == '2':
            klinik.dequeue()
        elif pilihan == '3':
            klinik.peek()
        elif pilihan == '4':
            klinik.display()
        elif pilihan == '5':
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")

if _name_ == "_main_":
    main()
