from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, homephone=None, mobile=None, workphone=None, faxphone=None,
                 email=None, email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None,
                 amonth=None, ayear=None, address2=None, phone2=None, notes=None, idcon=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobile = mobile
        self.workphone = workphone
        self.faxphone = faxphone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.idcon = idcon

    def __repr__(self):
        return "%s:%s:%s" % (self.idcon, self.lastname, self.firstname)

    def __eq__(self, other):
        #        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname
        return (self.idcon is None or other.idcon is None or self.idcon == other.idcon) \
               and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.idcon:
            return int(self.idcon)
        else:
            return maxsize
