#ТЕЛЕФОННАЯ СУКА КНИГА ЕБИ ЕЕ МАТЬ БЛЯТЬ!!!!!!!!!!!!!!!!!!!!!!!!!!!

phones = []


def search_phone(search_contact: dict):
    result = []
    for phone in phones:
        # есть ли то шо ищем в словаре с игнор. регистра .lower, !=-1 - возвращает -1 если ниче не нашло
        if any(str(value).lower().find(str(search_contact[key]).lower()) != -1
               for key, value in phone.items() if key in search_contact):
            result.append(phone)
    return result


def add_phone(f_name: str, l_name: str, phone: str):
    result = {"f_name": f_name, "l_name": l_name, "phone": phone}
    phones.append(result)


def delete_phone(f_name: str, l_name: str, phone: str):
    for p in phones[:]:
        if p["f_name"] == f_name and p["l_name"] == l_name and p["phone"] == phone:
            phones.remove(p)
