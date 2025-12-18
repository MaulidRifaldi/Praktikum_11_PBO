# before_refactor.py
# KODE SEBELUM REFACTORING (GOD CLASS)

class Mahasiswa:
    def __init__(self, sks, prasyarat_lulus):
        self.sks = sks
        self.prasyarat_lulus = prasyarat_lulus

class ValidatorManager:
    def validate(self, mahasiswa):
        if mahasiswa.sks > 24:
            return "SKS melebihi batas"
        elif not mahasiswa.prasyarat_lulus:
            return "Prasyarat belum lulus"
        else:
            return "Validasi berhasil"

if __name__ == "__main__":
    mahasiswa = Mahasiswa(22, True)
    validator = ValidatorManager()
    print(validator.validate(mahasiswa))
