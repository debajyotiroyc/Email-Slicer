#this project involves slicing your email id and displaying your user name and displaying your domain server name
email=input("Enter your email id:\n")
#to store the email id
pos=email.find("@")
#to store the username
user=email[0:pos]
#to store the domain name
domain=email[pos+1:]

out1="Your user name is '{}'".format(user)
out2="Your domain server name is '{}'".format(domain)
print(out1)
print(out2)
#end of code

