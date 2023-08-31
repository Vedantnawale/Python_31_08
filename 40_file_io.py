# in file we used read(r),write(w),append(a)
# f = open('myfile.txt','w')
fa = open('myfile.txt','a')
# fi = open('myfile.txt','r')
# print(f)
text = fa.write(" I am fine are you fine ?")
# texti = fi.read()

print(text)
# print(texti)
# fa.close()
# fi.close()

# if we dont want to use close then ew used with 
with open('myfile.txt','a'):
    fa.write("I am also fine")