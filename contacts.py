import csv

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook(object):
    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self, name):
        #A diferencia de un For normal, estamos obteniendo el indice y el contacto
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                #Eliminamos usando el indice
                del self._contacts[idx]
                self._save()
                break

    def edit(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                name = str(input('Escribe el nuevo nombre del contacto: '))
                phone = str(input('Escribe el nuevo telefono del contacto: '))
                email = str(input('Escribe el nuevo email del contacto: '))

                self._update(idx, name, phone, email)
                self._save()
                break

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break

        else:
            self._not_found()

    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('---------------------------------------------')

    def _not_found(self):
        print('---------------------------------------------')
        print('No encontrado')
        print('---------------------------------------------')

    def _update(self, idx, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts[idx] = contact
        print('---------------------------------------------')
        print('Contacto Actualizado')
        print('---------------------------------------------')

    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))

            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))

def run():

    contact_book = ContactBook()

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        #Para no usar la primera columna
        for idx, row in enumerate(reader):
            if idx == 0:
                continue

            contact_book.add(row[0], row[1], row[2])




    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el telefono del contacto: '))
            email = str(input('Escribe el email del contacto: '))

            contact_book.add(name, phone, email)


        elif command == 'ac':
            name = str(input('Escribe el nombre del contacto que quieres Actualizar: '))
            contact_book.edit(name)

        elif command == 'b':
            name = str(input('Escribe el nombre del contacto que quieres buscar: '))
            contact_book.search(name)

        elif command == 'e':
            name = str(input('Escribe el nombre del contacto que quieres eliminar: '))
            contact_book.delete(name)

        elif command == 'l':
            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    run()
