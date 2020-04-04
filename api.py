import string

class toJavascript:
    def __init__(self, code):
        self.code = code
        self.code = self.sub_keywords()
        self.code = self.fix_vars()
        self.chisel_index()
        new = self.fix_curly()
        # print(new)
        ni = open("newer.js", "w")
        ni.writelines(new)
    def getIndent(self, str_):
        n = 0
        for i in str_:
            if (i == " "):
                n += 1
            elif (i == "\t"):
                n += 1
            else:
                break
        return n
    def chisel_index(self):
        new = []
        for i in self.code:
            new.append(i.replace("\t", " "))
        self.code = new
    def sub_keywords(self):
        new = []
        reps = {
            'def ': 'function ',
            'print(': 'console.log(',
            '#': "//"
            }
        for i in self.code:
            m = i
            for j in reps:
                if ((j == 'def ') and (j in m)):
                    if ("self," in m):
                        m = m.replace(j, "")
                        m = m.replace("self,", "")
                    elif ('self' in m):
                        m = m.replace(j, "")
                        m = m.replace("self", "")
                    else:
                        m = m.replace(j, reps[j])
                else:
                        m = m.replace(j, reps[j])
            new.append(m)
        return new
    def fix_vars(self):
        new = []
        for i in self.code:
            if (" = " in i):
                n = "var %s" % i.lstrip()
                for j in range(self.getIndent(i)):
                    n = "%s%s" % (" ", n)
                new.append(n)
            else:
                new.append(i)
        return new
    def fix_curly(self):
        new = []
        for i in range( len( self.code ) ):
            if (len(self.code[i]) == 1):
                new.append(self.code[i])
                continue
            # print(self.code[i][-2])
            if ( self.code[i][-2] ==  ":" ):
                new.append(self.code[i].replace(":", " {"))
                continue
                # print(self.code[i])
            if (i != (len(self.code)-1)):
                if (self.getIndent(self.code[i]) > self.getIndent(self.code[i+1]) ):
                    new.append(self.code[i])
                    new.append("}")
                else:
                    new.append(self.code[i])
            else:
                if (self.getIndent(self.code[i]) != 0):
                    new.append(self.code[i])
                    new.append("\n}")
        return new


print(toJavascript( open("samp.py", "r").readlines() ))