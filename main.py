# ТЕЛЕФОННАЯ СУКА КНИГА ЕБИ ЕЕ МАТЬ БЛЯТЬ!!!!!!!!!!!!!!!!!!!!!!!!!!!

phones = []


def search_phone(search_contact: str):
    result = []
    for phone in phones:
        if search_contact in phone:
            result.append(phone)
    return result


def add_phone(f_name: str, l_name: str, phone: str):
    result = {"f_name": f_name, "l_name": l_name, "phone": phone}
    phones.append(result)


def delete_phone(name: str):
    for phone in phones:
        if phone["f_name"] or ["l_name"] or ["phone"] == name:
            phones.remove(phone)
