import random

secret_number = random.randint(1, 100)
attempts = 0

with open("game_log.txt", "w", encoding="utf-8") as file:
    def log_print(text):
        print(text)
        file.write(text + "\n")
    
    log_print("Я загадал число от 1 до 100. Попробуй угадать!")

    while True:
        attempts += 1
        try:
            guess = int(input("Введи число: "))
            file.write(f"Введено число: {guess}\n")
            
            if guess < secret_number:
                log_print("Слишком маленькое число!")
            elif guess > secret_number:
                log_print("Слишком большое число!")
            else:
                log_print(f"Поздравляю! Ты угадал число {secret_number} за {attempts} попыток.")
                break
        except:
            log_print("Ошибка! Пожалуйста, вводи только целые числа.")