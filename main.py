
import requests
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def check_document_existance(user_doc_number):
    doc_founded = False
    for current_document in documents:
        doc_number = current_document['number']
        if doc_number == user_doc_number:
            doc_founded = True
            break
    return doc_founded


def get_doc_owner_name(user_doc_number):
    doc_exist = check_document_existance(user_doc_number)
    if doc_exist:
        for current_document in documents:
            doc_number = current_document['number']
            if doc_number == user_doc_number:
                return current_document['name']


def get_all_doc_owners_names():
    users_list = []
    for current_document in documents:
        try:
            doc_owner_name = current_document['name']
            users_list.append(doc_owner_name)
        except KeyError:
            pass
    return set(users_list)


def remove_doc_from_shelf(doc_number):
    for directory_number, directory_docs_list in directories.items():
        if doc_number in directory_docs_list:
            directory_docs_list.remove(doc_number)
            break


def add_new_shelf(shelf_number):
    if not shelf_number:
        shelf_number
    if shelf_number not in directories.keys():
        directories[shelf_number] = []
        return shelf_number, True
    return shelf_number, False

def append_doc_to_shelf(doc_number, shelf_number):
    add_new_shelf(shelf_number)
    directories[shelf_number].append(doc_number)



def delete_doc(user_doc_number):
    doc_exist = check_document_existance(user_doc_number)
    if doc_exist:
        for current_document in documents:
            doc_number = current_document['number']
            if doc_number == user_doc_number:
                documents.remove(current_document)
                remove_doc_from_shelf(doc_number)
                return doc_number, True



def get_doc_shelf(user_doc_number):
    doc_exist = check_document_existance(user_doc_number)
    if doc_exist:
        for directory_number, directory_docs_list in directories.items():
            if user_doc_number in directory_docs_list:
                return directory_number


def move_doc_to_shelf(user_doc_number, user_shelf_number):
#    user_doc_number = input('Введите номер документа - ')
#    user_shelf_number = input('Введите номер полки для перемещения - ')
    remove_doc_from_shelf(user_doc_number)
    append_doc_to_shelf(user_doc_number, user_shelf_number)
    return



def add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number):
#    new_doc_number = input('Введите номер документа - ')
#    new_doc_type = input('Введите тип документа - ')
#    new_doc_owner_name = input('Введите имя владельца документа- ')
#    new_doc_shelf_number = input('Введите номер полки для хранения - ')
    new_doc = {
        "type": new_doc_type,
        "number": new_doc_number,
        "name": new_doc_owner_name
    }
    documents.append(new_doc)
    append_doc_to_shelf(new_doc_number, new_doc_shelf_number)
    return new_doc_shelf_number


def yandex_disk_folder():
    url = "https://cloud-api.yandex.net:443/"
    url_extra_folder = "v1/disk/resources"
    token = ''
    headers = {
        'accept': 'application/json',
        'authorization': f'OAuth {token}'}
    puting = requests.put(url + url_extra_folder, headers=headers, params={'path': 'photos'})
    return puting.status_code

print(yandex_disk_folder())

