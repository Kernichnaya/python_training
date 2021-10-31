from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, homephone=None, mobile=None, workphone=None, faxphone=None,
                 email=None, email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None,
                 amonth=None, ayear=None, address2=None, phone2=None, id=None, notes=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None):
        """

        :rtype: object
        """
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
        self.id = id
        self.notes = notes
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (
            self.id, self.lastname, self.firstname, self.middlename,
            self.nickname, self.company, self.address, self.homephone,
            self.mobile, self.faxphone, self.workphone, self.bday,
            self.bmonth, self.byear, self.email, self.email2, self.email3
        )

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.firstname is None or other.firstname is None or self.firstname == other.firstname) \
               and (self.middlename is None or other.middlename is None or self.middlename == other.middlename) \
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname) \
               and (self.nickname is None or other.nickname is None or self.nickname == other.nickname) \
               and (self.company is None or other.company is None or self.company == other.company) \
               and (self.address is None or other.address is None or self.address == other.address) \
               and (self.homephone is None or other.homephone is None or self.homephone == other.homephone) \
               and (self.mobile is None or other.mobile is None or self.mobile == other.mobile) \
               and (self.faxphone is None or other.faxphone is None or self.faxphone == other.faxphone) \
               and (self.workphone is None or other.workphone is None or self.workphone == other.workphone) \
               and (self.bday is None or other.bday is None or self.bday == other.bday) \
               and (self.bmonth is None or other.bmonth is None or self.bmonth == other.bmonth) \
               and (self.byear is None or other.byear is None or self.byear == other.byear) \
               and (self.email is None or other.email is None or self.email == other.email) \
               and (self.email2 is None or other.email2 is None or self.email2 == other.email2) \
               and (self.email3 is None or other.email3 is None or self.email3 == other.email3)
