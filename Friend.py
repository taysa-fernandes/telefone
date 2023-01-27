from Contato import Contact
class Friend(Contact):
    def __init__(self,name,email,phone):
        super().__init__(name, email)
        self.phone=phone
    def __repr__(self):
        for c in Contact.all_contacts:
            print(c)

friend1=Friend('Beltrano frança','Beltrano@dominio.com','2121-3131')
print(friend1.phone)
print(friend1.name)
print(friend1.email)
friend1.__repr__()


