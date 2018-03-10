from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "
    return prefix + " ".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname=" ", middlename=" ", lastname=" ", nickname=" ", title=" ", company=" ", address=" ", home=" ", mobile=" ", work=" ", fax=" ",
                    email=" ", email2=" ", email3=" ", homepage=" ", byear=" ")] + [Contact(firstname=random_string("testtest", 10), middlename=random_string("testtest", 10), lastname=random_string("testtest", 10), nickname=random_string("testtest", 10), title=random_string("testtest", 10), company=random_string("testtest", 10), address=random_string("testtest", 10), home=random_string("testtest", 10), mobile=random_string("testtest", 10), work=random_string("testtest", 10), fax=random_string("testtest", 10), email=random_string("testtest", 10), email2=random_string("testtest", 10),
                    email3=random_string("testtest", 10), homepage=random_string("testtest", 10),
                    byear=random_string("testtest", 10))
                    for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))