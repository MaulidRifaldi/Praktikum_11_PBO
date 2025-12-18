# README – Refactoring SOLID (Praktikum 11)

**Mata Kuliah** : Praktikum Pemrograman Berorientasi Objek  
**Nama** : Maulid Rifaldi
**NIM** : 2311102441120
**Kelas** : C


## Studi Kasus
Refactoring Sistem Validasi Registrasi Mahasiswa. Pada kode awal, terdapat satu class `ValidatorManager` yang melakukan validasi SKS dan validasi prasyarat dalam satu method menggunakan percabangan `if/else`.

File terkait:
- `before_refactor.py` → kode sebelum refactoring
- `main.py`, `validators.py`, `mahasiswa.py` → kode setelah refactoring


## 1. Analisis Pelanggaran Prinsip SOLID

### a. Single Responsibility Principle (SRP)
Class `ValidatorManager` memiliki lebih dari satu tanggung jawab, yaitu memvalidasi jumlah SKS dan memvalidasi prasyarat kelulusan. Hal ini melanggar prinsip SRP karena satu class seharusnya hanya memiliki satu alasan untuk berubah.

### b. Open/Closed Principle (OCP)
Kode awal tidak memenuhi OCP karena jika ingin menambahkan aturan validasi baru (misalnya validasi IPK), maka method `validate()` harus dimodifikasi. Class tidak tertutup terhadap perubahan.

### c. Dependency Inversion Principle (DIP)
`ValidatorManager` bergantung langsung pada implementasi konkret berupa logika `if/else`, bukan pada abstraksi. Hal ini membuat kode sulit dikembangkan dan diuji.

---

## 2. Implementasi DIP dan OCP
Untuk memenuhi DIP dan OCP, dibuat abstraksi `Validator` menggunakan abstract class. Setiap aturan validasi diimplementasikan dalam class terpisah yang mengimplementasikan abstraksi tersebut. Dependency Injection diterapkan dengan menyuntikkan daftar validator ke dalam `ValidatorManager` melalui constructor.

Dengan pendekatan ini, penambahan aturan validasi baru dapat dilakukan tanpa mengubah kode yang sudah ada.


## 3. Implementasi SRP
Setiap class memiliki satu tanggung jawab:
- `Mahasiswa` → menyimpan data mahasiswa
- `SKSValidator` → validasi jumlah SKS
- `PrasyaratValidator` → validasi prasyarat
- `ValidatorManager` → mengoordinasikan proses validasi

Pemisahan ini membuat struktur kode lebih modular dan mudah dirawat.


## 4. Pembuktian Open/Closed Principle (Challenge)
Penambahan validator baru dapat dilakukan dengan membuat class baru yang mengimplementasikan `Validator` tanpa memodifikasi kode `ValidatorManager`. Hal ini membuktikan bahwa sistem terbuka untuk ekstensi namun tertutup untuk modifikasi.


## 5. Refleksi
Pendekatan Dependency Injection lebih efektif mencegah code smell dibandingkan penggunaan `if/else` karena memisahkan logika bisnis dari detail implementasi. Dengan demikian, kode menjadi lebih fleksibel, mudah dikembangkan, serta lebih mudah diuji dan dipelihara.
