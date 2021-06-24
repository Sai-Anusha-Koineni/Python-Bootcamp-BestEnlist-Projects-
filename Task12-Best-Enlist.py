f =open(r"30_days_30_hour_operations.txt","w+")
f.write("I have completed 10 days successfully")
f.close()
#Appending in a created file
f1 =open(r"30_days_30_hour_operations.txt","a+") 
f1.writelines("Anu S")
#Reading the content in a file
f1 =open(r"30_days_30_hour_operations.txt","r") 
print(f1.read())
f1.close()
