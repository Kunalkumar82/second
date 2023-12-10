class student:
    __name=("SriRam")
    __age="19"
    __group="ECE"
    __report="fail"
    def __setdetails(self,__group,__report):
        self.__group=__group
        self.__report=__report
    def setdetails(self,group,report):
        self.group=group
        self.report=