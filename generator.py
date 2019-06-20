class LinkGenerator:
    def __init__(self, id):
        self.id = id
    
    def link(self):
        link = input("Enter the link: ")
        return link
    
    def main_page(self, link):
        page = link + 'view/' + self.id
        print(page)
    
    def product_page(self, link):
        pass
    
    def sale_page(self, link):
        pass
    
    def cat_page(self, link):
        pass
    
    def check_link(self):
        print('1. Main page')
        print('2. Product page')
        print('3. Sale page')
        print('4. Category page')
        number = int(input('Which link you want to modify?: '))
        return number

while True:
    id = input("Enter ID: ")
    if len(id) == 5:
        break
    print("ID needs to be 5 characters long.")

genarator = LinkGenerator(id)
choosen = genarator.check_link()
link = genarator.link()

if choosen == 1:
    print("1")
    genarator.main_page(link)

if choosen == 2:
    print("2")
    genarator.product_page(link)

if choosen == 3:
    print("3")
    genarator.sale_page(link)

if choosen == 4:
    print("4")
    genarator.cat_page(link)

print("end")
