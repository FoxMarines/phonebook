#ТЕЛЕФОННАЯ СУКА КНИГА ЕБИ ЕЕ МАТЬ БЛЯТЬ!!!!!!!!!!!!!!!!!!!!!!!!!!!

phones = [{"f_name": "Oleh", "l_name": "Usov", "phone": "736340103"}, {"f_name": "Вова", "l_name": "Бог", "phone": "103"}]

def search_phone(search_dict: str):
   result = []

   for phone in phones:
            if search_dict in phone:
             result.append(phone)
   return result

def add_phone(f_name, l_name,phone: str):
    result = {"f_name": f_name, "l_name": l_name, "phone": phone}
    print(result)
    phones.append(result)

def delete_phone(name: str):
    for phone in phones:
     if phone["f_name"] or ["l_name"] or ["phone"] == name:
      phones.remove(phone)

delete_phone("Oleh")
print(phones)

if __name__ == "__main__":
    result = search_phone("Ol")
    print(result)
    result = search_phone("oleh")
    print(result)
    add_phone("Vova", "Fox", "0928321212")
print(phones)

