import socket
import smtplib

#write a function which will try to find out len of a string without using an inbuilt len function
def string_len(str1):
    """find out len of a string without using an inbuilt len function"""
    length = 0
    for i in str1:
        length += 1
    return length


#Write a function which will be able to able to print an index of a list element with out using index method
def list_index(val):
    """Method to print an index of a list element with out using index method"""
    l = [21,32,43,55,54,67,17,98]
    for lst_index,value in enumerate(l):
        if val == value:
            break
    return lst_index


#write a function that prints the ip address of your system
def print_ip():
    """Function to print the ip address of the system"""
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    print(f"hostname is: {hostname} \nIp address of system: {ipaddress}")


#Write a function which will take input as a list with any kind of numeric value and give out an ouput as a 
# multiplication of all the numeric data l = [3.5, 6.56, "sudh", "iNeuron","fsda bootcamp 2.0"]

def list_mul(list1):
    """Multiplication of numeric values in the list"""
    result = 1
    for ele in list1:
        if type(ele) == int or type(ele) == float:
            result = result * ele
    print(f"Multiplication of numeric values in the list = {result}")




# Write a function that will be able to send a mail to any one
def send_mail():
    """Function to send an email"""
    gmail_user = 'prasad4ever@gmail.com'
    gmail_password = 'xxxxxxxxxxxxxxxx'

    sent_from = gmail_user
    to = ['praveenakomari@gmail.com']
    subject = 'OMG Super Important Message'
    body = 'Hey, whats up'

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        #secure email
        server.starttls()
        #login to mail account, need to enable "App passwords", otherwise login fails
        server.login(gmail_user,gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print("Email sent")
    except Exception as e:
        print('Something went wrong...'+str(e))

#Write a function that will shutdown your system
#Write a function which will be able to read all mails
# Write a function which will be able to read a doc/word file from your system 
str1 = "Hello"
length = string_len(str1)
print(f"length of string {str1} = {length}")

val = 55
index = list_index(val)
print(f"Index value of number {val} is : {index}")

print_ip()

list_mul([3.5, 6.56, "sudh", "iNeuron","fsda bootcamp 2.0"])

send_mail()