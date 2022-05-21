import re
import cmd

def parse(arg):
    return tuple(map(str, arg.split()))

class Parser(cmd.Cmd):

    def do_parse(self, arg):
        try:
            (filename, ) = parse(arg)
            labelsTable = dict()
            gotoTable = dict()

            f = open(filename, 'r')
            str = f.read()
            lines = str.split('\n')
            i = 1
            for line in lines:
                labelRezult = re.search(r'^\w+:', line)
                # print(labelRezult);
                if(labelRezult != None):
                    
                    labelRezult = labelRezult[0].split(':')[0]
                    if labelRezult in labelsTable:
                        print("Встречено повторное определение метки {} на строке {}".format(labelRezult,i))
                        raise Exception("Ошибка: Повторное создание метки")
                    labelsTable[labelRezult] = i

                gotoRezult = re.search(r'^\s*goto\s\w+;', line)

                # print(gotoRezult)
                if(gotoRezult != None):
                    gotoRezult = gotoRezult[0].split(";")[0]
                    gotoRezult = gotoRezult.split("goto ")[1]
                    

                    gotoTable[i] = gotoRezult

                # print( "{} {}".format(i, line))
                i = i + 1
            print("\nТаблица меток (метка, номер строки на которую указывает)")
            for tmp in labelsTable:

                print(tmp, labelsTable[tmp])
            print(
                "\nТаблица обращения к меткам (номер строки на котором вызвано goto, метка)")
            for tmp in gotoTable:
                print(tmp, gotoTable[tmp])
            f.close()

        except Exception as e:
            print(e)


mainParser = Parser()

mainParser.cmdloop()
