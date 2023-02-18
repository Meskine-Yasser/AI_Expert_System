class Rules:
    def __init__(self):
        self.premisses = []
        self.conclusions = []
        self.rules = []

    def Construct_LP_LC(self, file_name):  # Build the List of Premises and Conclusion
        br1 = open(file_name, 'r')
        text = br1.read()
        self.rules = text.split("\n")
        for line in self.rules:
            premisse = self.Extract_Premisse(line)
            self.premisses.append(premisse)
            conclusion = self.Extract_Conclusion(line)
            self.conclusions.append(conclusion)
        # LOG every list in log.txt
        log = open("log.txt", "a")
        log.write("Premises LIST :\n" + str(self.premisses) + "\n")

        log.write("Conclusions LIST :\n" + str(self.conclusions) + "\n")

        return self.premisses, self.conclusions, self.rules

    def Extract_Premisse(self, rule):
        a = (rule.split("if"))
        b = a[1].split("then")[0]
        return b.strip()

    def Extract_Conclusion(self, rule):
        a = (rule.split("if"))
        b = a[1].split("then")[1]
        return b.strip()

    def Remove_rule(self, index):
        self.rules.pop(index)
        self.premisses.pop(index)
        self.conclusions.pop(index)
