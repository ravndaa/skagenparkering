class NewRegistration():
    def __init__(self, nmbrplte, gustname, stupidno, cmnt="", days=1, hours=0, extnidfc="", vlidfromtmst="null", vliduntltmst="null"):
        self.__nmbrplte = nmbrplte
        self.__gustname = gustname
        self.__stupidno = int(stupidno)
        self.__cmnt = cmnt
        self.__days = int(days)
        self.__hours = int(hours)
        self.__extnidfc = extnidfc
        self.__vlidfromtmst = vlidfromtmst
        self.__vliduntltmst = vliduntltmst

    def to_json(self):
        return {'nmbrplte':self.__nmbrplte,'gustname':self.__gustname,'stupidno':self.__stupidno,'cmnt':self.__cmnt,'days':self.__days,'hours':self.__hours,'extnidfc':self.__extnidfc,'vlidfromtmst':self.__vlidfromtmst,'vliduntltmst':self.__vliduntltmst}
    
    @property
    def Nmbrplte(self):
        return self.__nmbrplte
    @property
    def gustname(self):
        return self.__gustname
    @property
    def stupidno(self):
        return self.__stupidno
    @property
    def cmnt(self):
        return self.__cmnt
    @property
    def days(self):
        return self.__days
    @property
    def hours(self):
        return self.__hours
    @property
    def extnidfc(self):
        return self.__extnidfc
    @property
    def vlidfromtmst(self):
        return self.__vlidfromtmst
    @property
    def vliduntltmst(self):
        return self.__vliduntltmst