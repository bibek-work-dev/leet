class Hashing:
    def isValid(self, s: list):
        checker = dict()

        for i in s:
            if i in checker:
                return True
            else:
                checker[i] = i
        
        return False
    
    def isTarget(self, arr: list, target: int):
        checker = dict()

        for index, value in enumerate(arr):
            if value in checker:
                return [index, checker[value] ]
            else:
                checker[value] = index

    def anagrams(self, arr: list[str]):
        checker = dict()
        for index, value in arr:
            pass