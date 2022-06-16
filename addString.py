def addStrings(string1, string2):
      if '.' not in string1 and '.' not in string2:
        string1_int = int(string1)
        string2_int = int(string2)
        return str(string1_int+string2_int)
      else:
        string1_int = float(string1)
        string2_int = float(string2)
      
        
        total = string1_int+string2_int
        
        if int(str(total).split(".")[1])==0:
          return str(total).split(".")[0]
        else:
          return str(total)
        
      
  
print(addStrings('10000000000000001','100000000000000000000003'))
print(addStrings('4.0','5.0'))
print(addStrings('4.3','5.5'))
