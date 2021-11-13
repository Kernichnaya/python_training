from model.contact import Contact
import random
import string
import os.path
import getopt
import sys
import jsonpickle

try:
    opts, arg = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file"])
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
    symbol = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


def random_number(maxlen):
    symbol = string.digits
    return "7".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


testdatacontact = [Contact(firstname="", middlename="", lastname="", nickname="", company="", address="",
                           homephone="", mobile="", faxphone="", phone2="", workphone="")] + [
                      Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                              lastname=random_string("lastname", 10),
                              nickname=random_string("nickname", 10), company=random_string("company", 10),
                              address=random_string("address", 10),
                              homephone=random_number(11), mobile=random_number(11), faxphone=random_number(11),
                              workphone=random_number(7), phone2=random_number(11))
                      for i in range(n)
                  ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdatacontact))
