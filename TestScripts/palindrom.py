class palindromClass:
    def isPalindrom(self,word):
        """take the """
        if(word==a.reverse(word)):
            return True
        else:
            return False

    def reverse(self,word):
        return word[::-1]



a=palindromClass()
print(a.isPalindrom("aSSaaSSa"))