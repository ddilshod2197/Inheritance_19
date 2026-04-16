# 19. Kafe buyurtmalari

class CafeOrder:
    def __init__(self, name, quantity):
        self.name = name          # taom/ichimlik nomi
        self.quantity = quantity  # dona / stakan soni

    def order_summary(self):
        """Buyurtma miqdori"""
        return self.quantity

    def __str__(self):
        return f"{self.name:12} | {self.quantity:4} dona"


# -----------------------------------------------
# Voris sinflar (chiroyli chiqish + emoji)
# -----------------------------------------------

class HotDrink(CafeOrder):
    def __str__(self):
        return f"☕ {self.name:10} → {self.quantity:3} stakan"


class ColdDrink(CafeOrder):
    def __str__(self):
        return f"🥤 {self.name:10} → {self.quantity:3} stakan"


# --------------------------------------------------
# Buyurtmalar xulosasi va eng ko‘p buyurtmani aniqlash
# --------------------------------------------------

def show_cafe_orders_summary(orders):
    print("\n" + "═" * 50)
    print("         KAFE BUYURTMALARI — XULOSA         ".center(50))
    print("═" * 50)
    print("Ichimlik nomi       Miqdor")
    print("─" * 50)

    total_items = 0
    max_item = None
    max_qty = -1

    for order in orders:
        print(order)
        qty = order.order_summary()
        total_items += qty
        
        if qty > max_qty:
            max_qty = qty
            max_item = order

    print("─" * 50)
    print(f"Jami buyurtma: {total_items} dona / stakan")
    
    if max_item:
        print(f"Eng ko‘p buyurtma qilingan: {max_item.name} — {max_qty} dona")
    
    print("═" * 50 + "\n")


# Test ma'lumotlari
buyurtmalar = [
    HotDrink("Kofe", 8),
    HotDrink("Choy", 5),
    HotDrink("Latte", 3),
    ColdDrink("Limonad", 4),
    ColdDrink("Muzli choy", 6),
    HotDrink("Kapuchino", 7),
]

show_cafe_orders_summary(buyurtmalar)


# Sizning misol qiymatlaringiz bilan:
print("\nSizning misol buyurtmalaringiz:\n")
misol_buyurtmalar = [
    HotDrink("Kofe", 5),
    HotDrink("Choy", 3),
]

show_cafe_orders_summary(misol_buyurtmalar)
