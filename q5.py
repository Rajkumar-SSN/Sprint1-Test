# 5.Write a function that checks if a string is a valid email. 
# Bonus: Write tests for this function

def is_valid_email(email):
    if not isinstance(email, str):
        return False
    if '@' not in email:
        return False
    
    main_part , domain_part = email.split('@', 1)
    if not main_part or not domain_part:
        return False
    
    if '.' not in domain_part:
        return False
    
    return True


test_mail_1 = "3110"
test_mail_2 = "rajkumar"
test_mail_3 = "rajkumar@"
test_mail_4 = "@gmail.com"
test_mail_5 = "rajkumar@gmailcom"
test_mail_6 = "rajkumar@gmail.com"


print("Test Mail 1 : ",test_mail_1," - ",is_valid_email(test_mail_1))
print("Test Mail 2 : ",test_mail_2," - ",is_valid_email(test_mail_2))
print("Test Mail 3 : ",test_mail_3," - ",is_valid_email(test_mail_3))
print("Test Mail 4 : ",test_mail_4," - ",is_valid_email(test_mail_4))
print("Test Mail 5 : ",test_mail_5," - ",is_valid_email(test_mail_5))
print("Test Mail 6 : ",test_mail_6," - ",is_valid_email(test_mail_6))
