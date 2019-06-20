class LinkGenerator:
    def __init__(self, id, write_to_file):
        self.id = id
        self.main_link = 'https://helion.pl/'
        self.write_to_file = write_to_file
    
    def link(self):
        link = input("Enter the link: ")
        return link
    
    def main_page(self):
        page = '{0}view/{1}'.format(self.main_link, self.id)
        if self.write_to_file:
            genarator.file_write(page)
        return page
    
    def product_page(self, link):
        dot_split = link.split(".")[1]
        prod_code = dot_split.split(",")[1]
        page = '{0}view/{1}/{2}'.format(self.main_link,
                                        self.id,
                                        prod_code)
        if self.write_to_file:
            genarator.file_write(page)
        return page
    
    def sale_page(self, link):
        sale_name = link.split('/')[-1]
        page = '{0}page/{1}/{2}'.format(self.main_link,
                                        self.id,
                                        sale_name)
        if self.write_to_file:
            genarator.file_write(page)
        return page
    
    def cat_page(self, link):
        cat_name = link.split('/')[-1]
        page = '{0}page/{1}/kategorie/{2}'.format(self.main_link,
                                                  self.id,
                                                  cat_name)
        if self.write_to_file:
            genarator.file_write(page)
        return page
    
    def check_link(self):
        while True:
            print('1. Main page.')
            print('2. Product page.')
            print('3. Sale page.')
            print('4. Category page.')
            print('')
            print('0. Exit')
            try:
                number = int(input('Which link you want to modify?: '))
                if number == 0:
                    print("Thanks for choosing my app!")
                    exit()
                if number == 9:
                    break
                if number > 0 and number <= 4:
                    break
                else:
                    print("Invalid choice.")
                    continue
            except ValueError:
                print("Need to be integer number.")
                continue
        return number
    
    def file_write(self, page):
        with open('links.txt', 'a') as file:
            file.write(page + '\n')
    
    def file_manip(self):
        name = input("File name: ")
        name = name + '.txt'
        print(name)
        with open(name, 'r') as file:
            for link in file:
                genarator.product_page(link)

    
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


def file_check():
    while True:
        check = input("Do you have a file to process?[Y/N]: ")
        if check.upper() == 'Y':
            file = True
            write_to_file = True
            break
        elif check.upper() == 'N':
            file = False
            write_to_file = wanna_save()
            break
        else:
            print("Y or N")
            continue
    return file, write_to_file

def wanna_save():
    while True:
        check = input("Do you want to save the result to a file?[Y/N]: ")
        if check.upper() == 'Y':
            write_to_file = True
            break
        elif check.upper() == 'N':
            write_to_file = False
            break
        else:
            print("Y or N")
            continue
    return write_to_file

#========================================================================#

if __name__ == '__main__':
    while True:
        id = input("Enter ID: ")
        if len(id) == 5:
            break
        print("Invalid ID! Needs to be 5 characters long.")
    
    file, write_to_file = file_check()

    genarator = LinkGenerator(id, write_to_file)

    if file:
        genarator.file_manip()
        print("Thanks for choosing my app!")
        exit()

    while True:
        try:
            num_of_links = int(input("How many links do you have?: "))
            if num_of_links >= 1:
                break
            else: 
                print("You can not process 0 <= links...")
                continue
        except ValueError:
            print("Needs to be integer.")

    for link in range(num_of_links):
        choosen = genarator.check_link()
        result = genarator.choose_link(choosen)
        print('Your dedicated link: {}'.format(result))
    
    print("Thanks for choosing my app!")
