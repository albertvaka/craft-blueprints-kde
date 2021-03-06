import info


class subinfo(info.infoclass):
    def setTargets(self):
        repoUrl = """http://winkde.org/pub/kde/ports/win32/repository/aspell"""

        self.targets['0.60'] = (repoUrl + """/aspell-en-6.0-41-bin.tar.bz2 """
                                + repoUrl + """/aspell-de-0.60.20030222.1-10-bin.tar.bz2 """)
        self.targets['0.60.6'] = """ http://files.kolab.org/local/windows-ce/aspell-0.60.6-data.zip"""

        self.defaultTarget = '0.60'

    def setDependencies(self):
        self.runtimeDependencies["virtual/bin-base"] = "default"


from Package.BinaryPackageBase import *


class Package(BinaryPackageBase):
    def __init__(self):
        BinaryPackageBase.__init__(self)
