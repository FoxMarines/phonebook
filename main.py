# ТЕЛЕФОННАЯ СУКА КНИГА ЕБИ ЕЕ МАТЬ БЛЯТЬ!!!!!!!!!!!!!!!!!!!!!!!!!!!

phones = []


def search_phone(search_contact: str):
    result = []
    for phone in phones:  # phone = dict
        for key, value in phone.items():  # key = f_name, l_name, phone; value = vova, gospod, 1488 etc
            if str(search_contact) in value:
                result.append(phone)
    return result


def add_phone(f_name: str, l_name: str, phone: str):
    result = {"f_name": f_name, "l_name": l_name, "phone": phone}
    phones.append(result)


def delete_phone(f_name: str, l_name: str, phone: str):
    for p in phones[:]:
        if p["f_name"] == f_name and p["l_name"] == l_name and p["phone"] == phone:
            phones.remove(p)


add_phone("Vova", "Gospod", "1488")
add_phone("Oleh", "usov", "1337")

b = search_phone("")
