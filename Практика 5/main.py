contacts = [{'name': 'Radomir', 'OPT': '110'}]

def show():
    for c in contacts:
        print(f"Имя: {c['name']}, Балл ОРТ: {c['OPT']}")

def create():
    name = input("Имя: ")
    score = input("Балл ОРТ: ")
    for c in contacts:
        if c['name'] == name:
            c['OPT'] = score
            print("Балл ОРТ обновлен")
            return
    contacts.append({'name': name, 'OPT': score})
    print("Контакт добавлен")

def edit():
    name = input("Имя для редактирования: ")
    for c in contacts:
        if c['name'] == name:
            new_name = input("Новое имя: ")
            new_score = input("Новый балл ОРТ: ")
            for x in contacts:
                if (x['name'] == new_name or x['OPT'] == new_score) and x != c:
                    print("Такое имя или баллы уже есть")
                    return
            c['name'] = new_name
            c['OPT'] = new_score
            print("Контакт изменён")
            return
    print("Контакт не найден")

def delete():
    name = input("Имя для удаления: ")
    for i, c in enumerate(contacts):
        if c['name'] == name:
            contacts.pop(i)
            print("Контакт удалён")
            return
    print("Контакт не найден")

while True:
    show()
    cmd = input("Команда (create/edit/delete/exit): ")
    if cmd == 'create':
        create()
    elif cmd == 'edit':
        edit()
    elif cmd == 'delete':
        delete()
    elif cmd == 'exit':
        break
    else:
        print("Неизвестная команда")