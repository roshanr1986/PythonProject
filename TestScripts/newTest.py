class uniqueNameClass:

    def __init__(self,names1,names2):
        self.names1=names1
        self.names2=names2

    def uniqueName(self):
        uniqueNames= set()
        for x in self.names1 + self.names2:
            #print(x)
            uniqueNames.add(x)
        return uniqueNames


allNames=uniqueNameClass(["Ava", "Emma", "Olivia"],["Olivia", "Sophia", "Emma"])
print(allNames.uniqueName())






