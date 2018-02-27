from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_contact(self, contact):
        wd = self.app.wd
        self.add_new_contact()
        self.fill_new_contact(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_homepage()
        self.contact_cache = None

    def fill_new_contact(self, contact):
        wd = self.app.wd
        self.change("firstname", contact.firstname)
        self.change("middlename", contact.middlename)
        self.change("lastname", contact.lastname)
        self.change("nickname", contact.nickname)
        self.change("title", contact.title)
        self.change("company", contact.company)
        self.change("address", contact.address)
        self.change("home", contact.home)
        self.change("mobile", contact.mobile)
        self.change("work", contact.work)
        self.change("fax", contact.fax)
        self.change("email", contact.email)
        self.change("email2", contact.email2)
        self.change("email3", contact.email3)
        self.change("homepage", contact.homepage)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
        self.change("byear", contact.byear)

    def change(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def add_new_contact(self):
        wd = self.app.wd
        self.find_home()
        wd.find_element_by_link_text("add new").click()


    def find_home(self):
        wd = self.app.wd
        if wd.current_url.endswith("/index.php"):
            return
        wd.find_element_by_link_text('home').click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.find_home()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete'][@type='button']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def edit_first_contact(self):
        self.select_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.find_home()
        #edit
        wd.find_elements_by_xpath("//img[@src='icons/pencil.png'][@title='Edit']")[index].click()
        #fill
        self.fill_new_contact(new_contact_data)
        wd.find_element_by_xpath("//input[@name='update'][@type='submit']").click()
        self.return_to_homepage()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.find_home()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.find_home()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                text = cells[1].text
                text1 = cells[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(lastname=text, id=id, firstname=text1))
        return list(self.contact_cache)








