import sys
def max_distance():
    global p_friends
    p_friends.discard(arg1)
    if len(p_friends) > 0:
        o.write(f"User '{arg1}' have {len(p_friends)} possible friends when maximum distance is {arg2}\n")
        p_friends = sorted(list(p_friends))
        p_friends = "', '".join(p_friends)
        o.write(f"These possible friends: {{'{p_friends}'}}\n")
    else:
        o.write("There are no possible friends\n")

dic = {}
with open(sys.argv[1]) as inp:
    for line in inp:
        name = line.split(":")[0]
        friends = set(line.split(":")[1].strip("\n ").split(" "))
        dic[name] = friends

o = open("output.txt","w")
with open(sys.argv[2]) as c:
    for line in c:
        command = line.split(" ")[0]
        arg = line.split(" ",1)[1].strip("\n ")

        if command == "ANU":
            if not arg in dic.keys():
                dic[arg] = set()
                o.write(f"User '{arg}' has been added to the social network successfully\n") 
            else:
                o.write("ERROR: Wrong input type for 'ANU'! -- This user already exists!\n")

        elif command == "DEU":
            if arg in dic.keys():
                for i in dic[arg]:
                    dic[i].remove(arg)
                del dic[arg]
                o.write(f"User '{arg}' and his/her all relations have been deleted successfully\n")
            else:
                o.write(f"ERROR: Wrong input type for 'DEU'!--There is no user named '{arg}'!\n")

        elif command == "ANF":
            if len(arg.split(" ")) == 2:
                arg1 = arg.split(" ")[0]
                arg2 = arg.split(" ")[1]
                if arg1 != arg2:
                    if arg1 in dic.keys() and arg2 in dic.keys():
                        if not arg2 in dic[arg1]:
                            dic[arg1].add(arg2)
                            dic[arg2].add(arg1)
                            o.write(f"Relation between '{arg1}' and '{arg2}' has been added successfully\n")
                        else:
                            o.write(f"ERROR: A relation between '{arg1}' and '{arg2}' already exists!\n")

                    elif not arg1 in dic.keys() and not arg2 in dic.keys():
                        o.write(f"ERROR: Wrong input type for 'ANF'!--No user named '{arg1}' and '{arg2}' found!\n")

                    elif not arg2 in dic.keys():
                        o.write(f"ERROR: Wrong input type for 'ANF'!--No user named '{arg2}' found!\n")

                    else:
                        o.write(f"ERROR: Wrong input type for 'ANF'!--No user named '{arg1}' found!\n")
                else:
                    o.write("ERROR: Wrong input type for 'ANF'!--Source user and target user cannot be the same!\n")
            else:
                o.write("ERROR: Wrong input type for 'ANF'!--Need 2 users!\n")

        elif command == "DEF":
            if len(arg.split(" ")) == 2:
                arg1 = arg.split(" ")[0]
                arg2 = arg.split(" ")[1]
                if arg1 != arg2:
                    if arg1 in dic.keys() and arg2 in dic.keys():
                        if arg2 in dic[arg1]:
                            dic[arg1].remove(arg2)
                            dic[arg2].remove(arg1)
                            o.write(f"Relation between '{arg1}' and '{arg2}' has been deleted successfully\n")
                        else:
                            o.write(f"ERROR: No relation between '{arg1}' and '{arg2}' found!\n")

                    elif not arg1 in dic.keys() and not arg2 in dic.keys():
                        o.write(f"ERROR: Wrong input type for 'DEF'!--No user named '{arg1}' and '{arg2}' found!\n")

                    elif not arg2 in dic.keys():
                        o.write(f"ERROR: Wrong input type for 'DEF'!--No user named '{arg2}' found!\n")

                    else:
                        o.write(f"ERROR: Wrong input type for 'DEF'!--No user named '{arg1}' found!\n")
                else:
                    o.write("ERROR: Wrong input type for 'DEF'!--Source user and target user cannot be the same!\n")
            else: 
                o.write("ERROR: Wrong input type for 'DEF'!--Need 2 users!\n")

        elif command == "CF":
            if arg in dic.keys():
                o.write(f"User '{arg}' has {len(dic[arg])} friends\n")
            else:
                o.write(f"ERROR: Wrong input type for 'CF'!--No user named '{arg}' found!\n")

        elif command == "FPF":
            if len(arg.split(" ")) == 2:
                arg1 = arg.split(" ")[0]
                arg2 = arg.split(" ")[1]
                if arg1 in dic.keys():
                    if arg2 == "1" or arg2 == "2" or arg2 == "3":
                        p_friends = set()
                        if arg2 == "1":
                            for name1 in dic[arg1]:
                                p_friends.add(name1)
                            max_distance()

                        elif arg2 == "2":
                            for name1 in dic[arg1]:
                                p_friends.add(name1)
                                for name2 in dic[name1]:
                                    p_friends.add(name2)
                            max_distance()

                        elif arg2 == "3":
                            for name1 in dic[arg1]:
                                p_friends.add(name)
                                for name2 in dic[name1]:
                                    p_friends.add(name2)
                                    for name3 in dic[name2]:
                                        p_friends.add(name3)
                            max_distance()
                    else:
                        o.write("ERROR: Wrong input type for 'FPF'!--Enter an integer(1, 2 or 3) as maximum distance!\n")
                else:
                    o.write(f"ERROR: Wrong input type for 'FPF'!--No user named '{arg1}' found!\n")
            else:
                o.write("ERROR: Wrong input type for 'FPF'!--Need 1 user and maximum distance!\n")

        elif command == "SF":
            if len(arg.split(" ")) == 2:
                arg1 = arg.split(" ")[0]
                MD = arg.split(" ")[1]
                if arg1 in dic.keys():
                    if MD == "2" or MD == "3":
                        o.write(f"Suggestion List for '{arg1}' (when MD is {MD}):\n")
                        if len(dic[arg1]) >= int(MD):
                            sf_list = [name2 for name1 in dic[arg1] for name2 in dic[name1]]
                            sf_list = list(filter(lambda n: not (n in dic[arg1] or n == arg1) , sf_list))
                            md = set(filter(lambda n: sf_list.count(n) == 3 or sf_list.count(n) == 2 , sf_list)) if MD == "2" else set(filter(lambda n: sf_list.count(n) == 3 , sf_list))
                            print_str = f"The suggested friends for '{arg1}':"
                            md = sorted(list(md))
                            for name in md:
                                o.write(f"'{arg1}' has {sf_list.count(name)} mutual friends with '{name}'\n")
                                print_str += f"'{name}',"
                            o.write(print_str.strip(",")+"\n")
                        else:
                            o.write(f"There are no suggestions for {arg1}\n")  
                    else:
                        o.write("ERROR: Mutually degree must be 2 or 3\n")                 
                else:
                    o.write(f"ERROR: Wrong input type for 'SF'!--No user named '{arg1}' found!\n")
            else:
                o.write("ERROR: Wrong input type for 'SF'!--Need 1 user and mutuality degree!\n")
        else:
            o.write("ERROR: Wrong command!\n")
o.close()