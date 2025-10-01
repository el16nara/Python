class Animal:
    def __init__(self, name, species, habitat):
        self.name = name
        self.species = species
        self.habitat = habitat
    
    def info(self):
        return f"{self.name} — это {self.species}, который живет в {self.habitat}."

class Mammal(Animal):
    def __init__(self, name, species, habitat, has_fur):
        super().__init__(name, species, habitat)
        self.has_fur = has_fur
    
    def info(self):
        return f"{self.name} — это {self.species}, у него {'есть шерсть' if self.has_fur else 'нет шерсти'}, и он живет в {self.habitat}."

class Reptile(Animal):
    def __init__(self, name, species, habitat, has_scales):
        super().__init__(name, species, habitat)
        self.has_scales = has_scales
    
    def info(self):
        return f"{self.name} — это {self.species}, у него {'есть чешуя' if self.has_scales else 'нет чешуи'}, и он живет в {self.habitat}."

class Zoo_show:
    def __init__(self):
        self.shows = {
            "Шоу львов": {"price": 20, "description": "Трюки с львами."},
            "Шоу змей": {"price": 15, "description": "Змеи демонстрируют свою ловкость."},
            "Шоу дельфинов": {"price": 25, "description": "Дельфины выполняют акробатические трюки."},
        }
    
    def display_shows(self):
        for show in self.shows:
            print(f"{show}: {self.shows[show]['description']}")
    
    def choose_ticket(self, show_name):
        if show_name in self.shows:
            show = self.shows[show_name]
            print(f"Цена билета на {show_name}: ${show['price']}")
            print(f"Описание: {show['description']}")
        else:
            print("Неверный выбор шоу.")

lion = Mammal("Лео", "Лев", "Саванна", True)
zoo_show = Zoo_show()
zoo_show.display_shows()
zoo_show.choose_ticket("Шоу львов")