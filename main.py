# main.py
# ValidatorManager & eksekusi program

from mahasiswa import Mahasiswa
from validators import SKSValidator, PrasyaratValidator

class ValidatorManager:
    def __init__(self, validators):
        self.validators = validators

    def validate(self, mahasiswa):
        for validator in self.validators:
            result = validator.validate(mahasiswa)
            if result:
                return result
        return "Validasi berhasil"

if __name__ == "__main__":
    mahasiswa = Mahasiswa(22, True)

    validators = [
        SKSValidator(),
        PrasyaratValidator()
    ]

    manager = ValidatorManager(validators)
    print(manager.validate(mahasiswa))
