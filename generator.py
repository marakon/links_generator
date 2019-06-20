import re

class LinkGenerator:
    def __init__(self, id):
        self.id = id
        self.main_link = 'https://helion.pl/'
    
    def link(self):
        link = input("Enter the link: ")
        return link
    
    def main_page(self, link):
        page = self.main_link + 'view/' + self.id
        return page
    
    def product_page(self, link):
        dot = link.split(".")[1]
        coma = dot.split(",")[1]
        page = self.main_link + 'view/' + self.id + '/' + coma
        return page
    
    def sale_page(self, link):
        sale = link.split('/')[4]
        page = self.main_link + 'page/' + self.id + '/' + sale
        return page
    
    def cat_page(self, link):
        page = link + 'view/' + self.id
        return page
    
    def check_link(self):
        print('1. Main page')
        print('2. Product page')
        print('3. Sale page')
        print('4. Category page')
        number = int(input('Which link you want to modify?: '))
        return number
    
    def choose_link(self, link):
        if choosen == 1:
            page = genarator.main_page(link)
        if choosen == 2:
            page = genarator.product_page(link)
        if choosen == 3:
            page = genarator.sale_page(link)
        if choosen == 4:
            page = genarator.cat_page(link)
        return page

while True:
    id = input("Enter ID: ")
    if len(id) == 5:
        break
    print("ID needs to be 5 characters long.")

genarator = LinkGenerator(id)
choosen = genarator.check_link()
link = genarator.link()
result = genarator.choose_link(link)
print(result)
