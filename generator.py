class LinkGenerator:
    def __init__(self, id):
        self.id = id
        self.main_link = 'https://helion.pl/'
    
    def link(self):
        link = input("Enter the link: ")
        return link
    
    def main_page(self):
        page = '{0}view/{1}'.format(self.main_link, self.id)
        return page
    
    def product_page(self, link):
        dot_split = link.split(".")[1]
        prod_code = dot_split.split(",")[1]
        page = '{0}view/{1}/{2}'.format(self.main_link,
                                        self.id,
                                        prod_code)
        return page
    
    def sale_page(self, link):
        sale_name = link.split('/')[-1]
        page = '{0}page/{1}/{2}'.format(self.main_link,
                                        self.id,
                                        sale_name)
        return page
    
    def cat_page(self, link):
        cat_name = link.split('/')[-1]
        page = '{0}page/{1}/kategorie/{2}'.format(self.main_link,
                                                  self.id,
                                                  cat_name)
        return page
    
    def check_link(self):
        while True:
            print('1. Main page')
            print('2. Product page')
            print('3. Sale page')
            print('4. Category page')
            print('')
            print('0. Exit')
            try:
                number = int(input('Which link you want to modify?: '))
                if number == 0:
                    print('Elo!')
                    exit()
                if number > 0 and number <= 4:
                    break
                else:
                    print("Invalid choice.")
                    continue
            except ValueError:
                print("Need to be integer number.")
                continue
        return number
    
    def choose_link(self, link):
        if choosen == 1:
            page = genarator.main_page()
        if choosen == 2:
            link = genarator.link()
            page = genarator.product_page(link)
        if choosen == 3:
            link = genarator.link()
            page = genarator.sale_page(link)
        if choosen == 4:
            link = genarator.link()
            page = genarator.cat_page(link)
        return page

if __name__ == '__main__':
    while True:
        id = input("Enter ID: ")
        if len(id) == 5:
            break
        print("Invalid ID! needs to be 5 characters long.")

    genarator = LinkGenerator(id)

    while True:
        try:
            num_of_links = int(input("How many links do you have?: "))
            if num_of_links >= 1:
                break
            else: 
                print("Only one link or more.")
                continue
        except ValueError:
            print("Needs to be integer.")

    for link in range(num_of_links):
        choosen = genarator.check_link()
        result = genarator.choose_link(choosen)
        print(result)
