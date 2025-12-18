# validators.py
# Abstraksi & implementasi validator (SRP, DIP, OCP)

from abc import ABC, abstractmethod

# Abstraksi (DIP)
class Validator(ABC):
    @abstractmethod
    def validate(self, mahasiswa):
        pass

# Implementasi SRP
class SKSValidator(Validator):
    def validate(self, mahasiswa):
        if mahasiswa.sks > 24:
            return "SKS melebihi batas"
        return None

class PrasyaratValidator(Validator):
    def validate(self, mahasiswa):
        if not mahasiswa.prasyarat_lulus:
            return "Prasyarat belum lulus"
        return None
