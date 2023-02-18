class Database:
    def __init__(self):
        self.facts = []  # Database LIST

    def Construct_LF(self, file_name):  # Build the List of Facts
        br1 = open(file_name, 'r')
        text = br1.read()
        self.facts = text.split("\n")
        log = open("log.txt", "a")
        log.write("Database LIST : \n" + str(self.facts) + "\n")


        return self.facts

    def check_P_DB(self, premisse):  # Check if the Premise is in the Database
        if (" and " in premisse):
            while (" and " in premisse):
                premisse = premisse.split(" and ")  # Premises without AND
                splited_premisse = premisse
        else:
            if premisse in self.facts:  # Simple Premises
                return True
            else:
                return False

        for element in splited_premisse:

            if element not in self.facts:
                return False
        return True

    """def regleDeclenchable(self, premisse):
        if " and " in premisse:
            while " and " in premisse:
                a = premisse.split(" and ", 1)[0]
                premisse = premisse.split(" and ")
                if a not in self.facts:
                    return False
        if premisse in self.facts:
            return True
        else:
            return False
"""
    def Add_Fact(self, fait):
        self.facts.append(fait)
