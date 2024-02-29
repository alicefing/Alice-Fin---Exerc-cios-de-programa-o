string = "5"

if (len(string) > 0 and                 
    string.count('.') <= 1 and          
    string.lstrip('+-').replace('.', '', 1).isdigit()): 
    print("A string representa um número real.")
else:
    print("A string não representa um número real.")
