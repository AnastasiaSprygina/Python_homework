from model.group import Group
import random
import string

constant = [
    Group(name="name1", group_header="header1", footer="footer1"),
Group(name="name2", group_header="header2", footer="footer2")
]



def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "
    return prefix + " ".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name="", group_header="", footer="")] + [Group (name=random_string("testtest", 10), group_header=random_string("test", 20),footer=random_string("test", 20))
                                                           for i in range(5)]
