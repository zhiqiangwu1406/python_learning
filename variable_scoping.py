#scopes

#global
var = "variable";

print(var);

def scoping ():
    print (f"{var} is in local scope");

scoping();

#overwrite only in local scope

def overwrite():
    var = "new variable";
    print (f"{var} overwritten in local scope");

overwrite();
print(var);

#overwrite in global scope;

def overwriteGlobal ():
    global var
    var = "new variable in global scope"
    print (f"{var}  in local");

overwriteGlobal();
print (f"{var} after overwritten");