from abc import ABC, abstractmethod

# Fiyatlandırma için Interface
class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, quantity, unit_price):
        pass

# KG bazlı fiyatlandırma
class WeightBasedPricing(PricingStrategy):
    def calculate_price(self, quantity, unit_price):
        return quantity * unit_price  # KG * KG başına fiyat

# Adet bazlı fiyatlandırma
class PieceBasedPricing(PricingStrategy):
    def calculate_price(self, quantity, unit_price):
        return quantity * unit_price  # Adet * Birim fiyat

# Pastane Ürünü
class BakeryItem:
    def __init__(self, name, unit_price, pricing_strategy: PricingStrategy):
        self.name = name
        self.unit_price = unit_price
        self.pricing_strategy = pricing_strategy
    
    def get_price(self, quantity):
        return self.pricing_strategy.calculate_price(quantity, self.unit_price)

# Tartı Sistemi
class BakeryScale:
    def __init__(self):
        self.current_weight = 0

    def weigh(self, weight):
        self.current_weight = weight
        print(f"Tartılan ağırlık: {weight} KG")
        return weight

# Örnek Kullanım
if __name__ == "__main__":
    # KG bazlı ürün (Ekmek)
    bread = BakeryItem("Ekmek", 2.5, WeightBasedPricing())  # KG başına 2.5 TL
    scale = BakeryScale()
    weight = scale.weigh(1.2)  # 1.2 KG
    print(f"{bread.name} fiyatı: {bread.get_price(weight)} TL")
    
    # Adet bazlı ürün (Pasta)
    cake = BakeryItem("Pasta", 15, PieceBasedPricing())  # 1 adet pasta 15 TL
    print(f"{cake.name} fiyatı: {cake.get_price(2)} TL")  # 2 adet pasta