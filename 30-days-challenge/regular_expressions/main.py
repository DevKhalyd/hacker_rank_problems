"""
Task:

Consider a database table, Emails, which has the attributes
First Name and Email ID. Given N  rows of data simulating 
the Emails table, print an alphabetically-ordered list of 
people whose email address ends in @gmail.com.

Constraints

2 <= N <= 30

-Each of the first names consists of lower case letters  [a-z]  only.

-Each of the email IDs consists of lower case letters [a-z],@  and . only.

-The length of the first name is no longer than 20.

-The length of the email ID is no longer than 50.

"""
testmails = [
"riya riya@gmail.com",
"julia julia@julia.me",
"julia sjulia@gmail.com",
"julia julia@gmail.com",
"samantha samantha@gmail.com",
"tanya tanya@gmail.com",
"riya ariya@gmail.com",
"julia bjulia@julia.me",
"julia csjulia@gmail.com",
"julia djulia@gmail.com",
"samantha esamantha@gmail.com",
"tanya ftanya@gmail.com",
"riya riya@live.com",
"julia julia@live.com",
"julia sjulia@live.com",
"julia julia@live.com",
"samantha samantha@live.com",
"tanya tanya@live.com",
"riya ariya@live.com",
"julia bjulia@live.com",
"julia csjulia@live.com",
"julia djulia@live.com",
"samantha esamantha@live.com",
"tanya ftanya@live.com",
"riya gmail@riya.com",
"priya priya@gmail.com",
"preeti preeti@gmail.com",
"alice alice@alicegmail.com",
"alice alice@gmail.com",
"alice gmail.alice@gmail.com"]


if __name__ == '__main__':
    # Total number of rows in the table
    #N = int(input().strip())

    emails = []

    for index in range(len(testmails)):
        
        first_multiple_input = testmails[index].rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]

        emailComponents = emailID.split('@')

        if emailComponents[1] == 'gmail.com':
            emails.append(firstName)

    
    emails.sort()

    for email in emails:
        print(email)