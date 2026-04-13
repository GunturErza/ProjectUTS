## PROJECT UTS – STRUKTUR DATA
## Semester Genap 2025/2026
## Mata Kuliah: Struktur Data
## Jenis Tugas: Project Kelompok
## Tema: Penerapan Queue dan Stack

----------------------------------

## NAMA ANGGOTA KELOMPOK
1. I GEDE WIRA YOGA (2501010086)
2. I KADEK GUNTUR ERZA PRAMUDYA (2501010071)
3. I MADE BAGUS ABIYOGA PRAWIRA (2501010089)

   ---------------------------

## 1. Rumusan Masalah dan Solusi
 * *1. Bagaimana penerapan struktur data antrian dengan konsep First In First Out (FIFO) bisa dimanfaatkan untuk mengatur antrean pasien dengan cara yang lebih adil dan teratur? *
 * *2. Bagaimana penerapan linked list bisa memperbaiki keunggulan dan efektivitas penggunaan memori ketika menghadapi variasi jumlah antrean yang berubah-ubah dibandingkan dengan memanfaatkan array? *
 * *3. Bagaimana implementasi linked list dapat menambah fleksibilitas dan efisiensi pemanfaatan memori dalam mengelola beberapa antrean yang ukurannya berubah secara dinamis jika dibandingkan dengan penggunaan array?*

## Solusi:
   Sistem ini menghadirkan solusi berupa aplikasi manajemen antrean yang berbasis terminal, mengadopsi struktur data queue. Dengan memanfaatkan prinsip FIFO, sistem memastikan pasien yang melakukan pendaftaran terlebih dahulu akan mendapatkan layanan lebih awal. Pemilihan implementasi menggunakan linked list dilakukan karena sifatnya yang fleksibel, memungkinkan sistem untuk menambah atau menghapus informasi pasien tanpa terikat pada batasan kapasitas memori yang kaku. 

   Secara operasional, sistem ini menawarkan fitur-fitur esensial seperti penambahan pasien ke antrean (enqueue), pemanggilan pasien yang ada di posisi terdepan (dequeue), pengecekan pasien berikutnya (peek), serta penampilan daftar lengkap pasien yang tengah menunggu (display). Dengan fitur-fitur ini, proses administrasi di klinik menjadi lebih jelas, tepat, dan profesional, yang pada gilirannya akan meningkatkan mutu layanan kepada masyarakat.

  -------------------------------
  
## 2. Landasan Teori
Struktur data adalah cara mengelola dan menyimpan data agar dapat diakses secara efisien. Dalam project ini, digunakan konsep *Queue* (antrean) yang bekerja dengan prinsip *FIFO*. Elemen yang masuk pertama kali akan diproses pertama kali pula.
Implementasi dilakukan menggunakan Linked List, di mana setiap data disimpan dalam sebuah *Node. Setiap Node memiliki penunjuk (pointer) ke elemen berikutnya. Pendekatan ini lebih dinamis dibandingkan Array karena tidak memerlukan deklarasi ukuran awal yang kaku.

  -------------------------------
  
# 3. Desain Sistem dan Implementasi
   # FlowChart:
   ![WhatsApp Image 2026-04-13 at 17 44 44](https://github.com/user-attachments/assets/65fc2fec-1ac6-49b3-92f5-1e11e4f84e9c)

 ALUR PROGRAM: 
 ## INPUT
  Tahapan dimulai pada alur input di mana petugas administrasi menerima data nama pasien dan memasukkannya ke dalam sistem melalui operasi enqueue. Secara teknis, sistem akan menciptakan sebuah node baru dalam linked list untuk menyimpan identitas tersebut. 
  
  ## PROSES
Memasuki alur proses, sistem menerapkan logika queue dengan prinsip FIFO. Jika kondisi antrean masih kosong, maka pasien tersebut akan ditetapkan sebagai elemen depan sekaligus elemen belakang dalam sistem. Namun, apabila sudah terdapat antrean sebelumnya, pasien baru akan ditambahkan di posisi paling belakang sehingga tidak mengganggu urutan pasien yang sudah ada. Ketika pihak medis siap memberikan pelayanan, sistem menjalankan operasi dequeue untuk memanggil pasien di posisi terdepan dan menggeser penunjuk antrean ke pasien berikutnya dalam linked list. 

## OUTPUT
Pada tahapan alur output, sistem memberikan informasi konfirmasi mengenai status keberhasilan pasien masuk ke dalam daftar. Selain itu, sistem secara aktif menampilkan nama pasien yang dipanggil untuk segera menuju ruang periksa. Melalui fungsi display dan peek, pihak administrasi juga dapat memantau seluruh daftar tunggu maupun melihat pasien urutan berikutnya secara transparan dan akurat. Seluruh rangkaian proses ini memastikan manajemen data pasien di klinik menjadi lebih profesional dan meminimalkan risiko kesalahan manusia.

   -------------------------------

# 4. Kesimpulan
 Melalui penerapan dan analisis pada sistem ini, terlihat jelas bahwa struktur data Queue merupakan solusi efektif untuk mengelola antrean klinik. Dengan memegang prinsip FIFO, sistem memastikan setiap pasien dilayani dengan adil berdasarkan urutan kedatangan mereka. Dari sisi teknis, penggunaan Linked List terbukti sangat efisien karena sifatnya yang dinamis dalam mengelola data pasien tanpa membebani memori. Secara keseluruhan, sistem ini tidak hanya memodernisasi cara klinik bekerja, tetapi juga menciptakan proses administrasi yang lebih transparan dan profesional.
