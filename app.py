# 1
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__available = True

    def borrow(self):
        if self.__available:
            self.__available = False
            print(f"📖 '{self.title}' kitobi olindi.")
        else:
            print(f"'{self.title}' — hozircha mavjud emas.")

    def return_book(self):
        self.__available = True
        print(f"📚 '{self.title}' qaytarildi.")

    def is_available(self):
        return self.__available


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' kutubxonaga qo‘shildi.")

    def show_books(self):
        for book in self.books:
            status = "Mavjud" if book.is_available() else "Olingan"
            print(f"{book.title} — {status}")


class User:
    def __init__(self, name):
        self.name = name

    def borrow_book(self, library, title):
        for book in library.books:
            if book.title == title:
                book.borrow()
                return
        print("Bunday kitob topilmadi.")

    def return_book(self, library, title):
        for book in library.books:
            if book.title == title:
                book.return_book()
                return
        print("Kitob topilmadi.")



# 2
class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__medical_history = []

    def add_diagnosis(self, doctor, diagnosis):
        if isinstance(doctor, Doctor):
            self.__medical_history.append(diagnosis)
            print(f"{self.name} uchun tashxis qo‘shildi: {diagnosis}")
        else:
            print("Faqat shifokor tashxis qo‘sha oladi!")

    def get_medical_history(self, requester):
        if isinstance(requester, Doctor):
            return self.__medical_history
        else:
            return "Tibbiy tarix maxfiy."


class Doctor:
    def view_patient_history(self, patient):
        print(f"{patient.name} tibbiy tarixi:", patient.get_medical_history(self))


class Receptionist:
    def schedule_appointment(self, patient, time):
        print(f"{patient.name} bilan uchrashuv {time} da belgilandi.")



# 3
class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = None
        self.set_password(password)

    def set_password(self, new_password):
        if len(new_password) >= 8:
            self.__password = new_password
            print("Parol muvaffaqiyatli o‘rnatildi.")
        else:
            print("Parol kamida 8 belgidan iborat bo‘lishi kerak!")

    def check_password(self, password):
        return self.__password == password


class AuthenticationSystem:
    def authenticate(self, user, password):
        if user.check_password(password):
            print(f"{user.username} tizimga muvaffaqiyatli kirdi ✅")
        else:
            print("❌ Parol noto‘g‘ri!")



# 4
class SmartDevice:
    def __init__(self, name):
        self.name = name
        self.__status = "off"

    def turn_on(self):
        self.__status = "on"
        print(f"{self.name} yoqildi.")

    def turn_off(self):
        self.__status = "off"
        print(f"{self.name} o‘chirildi.")

    def get_status(self):
        return self.__status


class SmartHome:
    def __init__(self):
        self.devices = {}

    def add_device(self, device, access_level="all"):
        self.devices[device.name] = {"device": device, "access": access_level}

    def control_device(self, user, device_name, action):
        device_info = self.devices.get(device_name)
        if not device_info:
            print("Qurilma topilmadi.")
            return

        if device_info["access"] == "restricted" and isinstance(user, Guest):
            print(f"🚫 {device_name} — mehmon uchun ruxsat yo‘q.")
            return

        device = device_info["device"]
        if action == "on":
            device.turn_on()
        elif action == "off":
            device.turn_off()
        else:
            print("Noma’lum amal.")


class Guest:
    def __init__(self, name):
        self.name = name



# 5
class Vehicle:
    def __init__(self, plate_number):
        self.plate_number = plate_number
        self.__fuel_level = 0
        self.__mileage = 0

    def refuel(self, amount):
        self.__fuel_level += amount
        print(f"{self.plate_number} uchun yonilg‘i: {self.__fuel_level}L")

    def drive(self, distance):
        if self.__fuel_level <= 0:
            print("Yonilg‘i tugagan, iltimos, to‘ldiring!")
            return
        self.__mileage += distance
        self.__fuel_level -= distance * 0.1
        print(f"{self.plate_number} {distance} km yoldan o‘tdi.")


class FleetManager:
    def set_fuel(self, vehicle, amount):
        vehicle._Vehicle__fuel_level = amount
        print(f"{vehicle.plate_number} yonilg‘i yangilandi: {amount}L")

    def view_status(self, vehicle):
        print(f"{vehicle.plate_number}: {vehicle._Vehicle__fuel_level}L, {vehicle._Vehicle__mileage} km")


class Driver:
    def __init__(self, name):
        self.name = name

    def drive_vehicle(self, vehicle, distance):
        vehicle.drive(distance)
