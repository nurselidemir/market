from abc import ABC, abstractmethod
import random

# Sensör Arayüzü
class Sensor(ABC):
    @abstractmethod
    def read_value(self):
        pass

# Sıcaklık Sensörü
class TemperatureSensor(Sensor):
    def read_value(self):
        return round(random.uniform(-5, 10), 2)  # -5°C ile 10°C arasında rastgele değer

# Nem Sensörü
class HumiditySensor(Sensor):
    def read_value(self):
        return round(random.uniform(30, 90), 2)  # %30 - %90 arası nem

# Doluluk Sensörü
class StorageSensor(Sensor):
    def read_value(self):
        return random.randint(0, 100)  # %0 - %100 doluluk

# Saklama Alanı Takip Sistemi
class StorageMonitor:
    def __init__(self, temp_sensor: Sensor, humidity_sensor: Sensor, storage_sensor: Sensor):
        self.temp_sensor = temp_sensor
        self.humidity_sensor = humidity_sensor
        self.storage_sensor = storage_sensor
    
    def check_conditions(self):
        temp = self.temp_sensor.read_value()
        humidity = self.humidity_sensor.read_value()
        storage = self.storage_sensor.read_value()
        
        print(f"Sıcaklık: {temp}°C, Nem: {humidity}%, Doluluk: {storage}%")
        
        if temp < 0:
            print("⚠️ Uyarı: Depo çok soğuk! Isıtma sistemini kontrol edin.")
        elif temp > 8:
            print("⚠️ Uyarı: Depo sıcaklığı çok yüksek!")
        
        if humidity < 40:
            print("⚠️ Uyarı: Hava çok kuru, nemlendirici çalıştırılmalı.")
        elif humidity > 80:
            print("⚠️ Uyarı: Nem çok yüksek, küf riski var!")
        
        if storage > 90:
            print("⚠️ Uyarı: Depo dolmak üzere, yeni sipariş almadan önce stok kontrol edilmeli.")

# Sensörleri başlat
if __name__ == "__main__":
    temp_sensor = TemperatureSensor()
    humidity_sensor = HumiditySensor()
    storage_sensor = StorageSensor()
    
    monitor = StorageMonitor(temp_sensor, humidity_sensor, storage_sensor)
    monitor.check_conditions()