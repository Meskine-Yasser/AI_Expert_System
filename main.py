from database import Database
from rules import Rules
# for log time management
from datetime import datetime


firedset = []


def Forward_Chaining_without_goal(inifact, DB, KB):
    iteration = 0
    log = open("log.txt", "a")
    #DBa = open("DB5.txt", "w")
    log.write("----------------------------------------- " + str(datetime.utcnow()) +"------------------------------------------\n")
    log.write('\n')
    log.write("Forward Chaining without Goal : \n")
    log.write("initial fact to infer: " + str(inifact) + "\n")
    # log.write("*************************************")
    # log.write('\n')
    flag= True
    global firedset
    while flag:
        #flag=False
        conflictset = []
        log.write("\nITERATION N: " + str(iteration) + "\n")
        log.write("___________________________________________\n")
        iteration += 1
        for rule in KB.rules: # Read rule
            #i = i + 1
            if rule in firedset: # check rule is fired
                continue
            premise = KB.Extract_Premisse(rule)
            for fact in inifact.split(" and "):
                if fact in premise: # check if initial fact is in premise of a rule
                    if DB.check_P_DB(premise): # check other premises that are in the rule if they're in
                        #if KBa.readline():
                        conflictset.append(rule)
        if conflictset:
            log.write("The Conflict set is" + str(conflictset) + "\n")
            fired = conflictset.pop(0) # Fire the rule
            log.write("The Fired Rule is: " + str(fired) + "\n")
            firedset.append(fired)
            log.write("The Fired Rules are: " + str(firedset) + "\n")
            KB.rules.remove(fired) # remove the rule from KB
            #split_premises = premise.split(" and ")
            if not KB.Extract_Premisse(fired) in DB.facts:
                DB.Add_Fact(KB.Extract_Premisse(fired))
            DB.Add_Fact(KB.Extract_Conclusion(fired))
            # for fact in DB.facts:
            #     DBa.write(str(fact) + "\n")
            # DBa.close()
        else:
            if KB.rules in firedset:
                log.write("All rules are fired, new DB is: " + str(DB.facts) +"\n")
                break
            else:
                log.write("ALL The Fired Rules are: " + str(firedset) + "\n")
                log.write("All rules are fired, new DB is: " + str(DB.facts) + "\n")
                log.write("Not all rules are fired, but new Facts Added: " + str(DB.facts) + "\n")
                break


def Forward_Chaining(goal, DB, KB):
    i = 0
    iteration = 0
    DBa = open("DB5.txt", "w")
    log = open("log.txt", "a")
    log.write("----------------------------------------- " + str(
        datetime.utcnow()) + "------------------------------------------\n")
    log.write('\n')
    log.write("Forward Chaining : \n")
    log.write("Goal to infer: " + str(goal) + "\n")
    # log.write("*************************************")
    # log.write('\n')
    while (goal not in DB.facts) and (len(KB.rules) != 0): # while goal not achieved
        log.write("\nITERATION N: " + str(iteration) + "\n")
        log.write("___________________________________________\n")
        iteration += 1
        not_activated = False
        for premisse in KB.premisses:
            i = i + 1
            cpremisse = premisse
            if DB.check_P_DB(cpremisse):
                log.write("The activated Rule is: " + str(KB.rules[(KB.premisses).index(premisse)]) + "\n")

                DB.Add_Fact(KB.conclusions[(KB.premisses).index(premisse)])
                log.write(
                    "Conclusion is added to the facts: " + str(KB.conclusions[(KB.premisses).index(premisse)]) + "\n")

                log.write("New Database/Facts is \n" + str(DB.facts) + "\n")

                log.write("Rule Fired \n")
                log.write("*** \n")
                KB.Remove_rule((KB.premisses).index(premisse))

                not_activated = True
        if not not_activated:
            log.write("No Activated Rule\n")
            print("No Activated Rule")
            break
    if goal in DB.facts:
        for fait in DB.facts:
            DBa.write(str(fait) + "\n")
        DBa.close()
        log.write(goal + " is achieved \n\n")
        print(goal + " is achieved\n\n")
    else:
        log.write(goal + " is not achieved \n\n")
        print(goal + " is not achieved \n\n")


def Backward_Chaining(goal, DB, KB):
    goals = [goal]
    succeed = True
    log = open("log.txt", "a")
    DBa = open("DB5.txt", "w")
    log.write("----------------------------------------- " + str(datetime.utcnow()) + "------------------------------------------\n")
    log.write('\n')
    log.write("Backward Chaining : \n")
    log.write("Goal to Achieve : " + str(goal) + "\n")
    log.write('\n')
    iteration = 0
    while True:
        log.write("\nITERATION N: " + str(iteration) + "\n")
        iteration += 1
        log.write("______________________________________________ \n")
        if goals[-1] in DB.facts:
            goals.pop()

        if len(goals) == 0:
            break

        # IF no rule is applicable
        if goals[-1] not in KB.conclusions:
            succeed = False
            break

        # Array that has rules that are applicable
        active_rules = []
        i = 0
        for conclusion in KB.conclusions:
            if goals[-1] == conclusion:
                premisse = KB.premisses[i]
                premisse_table = premisse.split(" and ")
                active_rules.append((premisse_table, conclusion))
            i += 1
        log.write("ALL the applicable rules: \n" + str(active_rules) + "\n")
        # log.write('\n')

        if len(active_rules) == 0:
            succeed = False
            break
        else:
            active_rule = active_rules[0]
            for tr in active_rules:
                if len(tr[0]) > len(active_rule[0]):
                    active_rule = tr
            log.write("Applicable Rule: \n" + str(active_rule) + "\n")
            # log.write("*** \n")

            valid = True
            for premisse in active_rule[0]:
                if premisse not in DB.facts:
                    goals.append(premisse)
                    valid = False
            if valid:
                DB.Add_Fact(goals[-1])
                log.write('New Database \n' + str(DB.facts) + '\n')
    if succeed:
        for fact in DB.facts:
            DBa.write(str(fact) + "\n")
        DBa.close()
        log.write(str(goal) + " is achieved \n")
        log.close()
        print(goal + " is achieved")
    else:
        log.write(str(goal) + " is not achieved \n\n")
        print(goal + " is not achieved \n\n")


def main():
    log = open("log.txt", "a")
    log.write("\n******************************************************************\n")
    DB = Database()
    KB = Rules()
    #File_name_DB = input("Give the Database file: ")
    #File_name_KB = input("Give the Knowledge Base file: ")
    log.write(str(datetime.utcnow()))
    KB.Construct_LP_LC("KB5.txt")
    DB.Construct_LF("DB5.txt")
    goal = input("Give the Goal to achieve: ")
    chaining = ""
    while chaining not in ["FC", "BC", "FCf"]:
        chaining = input("Choose FC for Forward-Chaining or BC for Backward-Chaining or FCf for Forward-Chaining without Goal:")
    if chaining == "FC":
        Forward_Chaining(goal, DB, KB)
    elif chaining == "FCf":
        Forward_Chaining_without_goal(goal, DB, KB)
    else:
        Backward_Chaining(goal, DB, KB)

    Exit = input("EXIT? yes or no: ")
    if Exit == "yes":
        # log.truncate(0)
        log.close()
    else:
        log.close()
        main()


if __name__ == "__main__":
    main()
