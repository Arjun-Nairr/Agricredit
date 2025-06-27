import math
import random
import string
import time
import re


def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_regex, email):
        return True
    else:
        return False


def validate_mobile(mobile):
    mobile_regex = r'^[6-9]\d{9}$'  
    if re.match(mobile_regex, mobile):
        return True
    else:
        return False


def loading_animation():
    print("Processing", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
    print()


def generate_captcha(length=6):
    captcha = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(length))
    return captcha


def verify_captcha(captcha):
    user_input = input("Enter the CAPTCHA: ")
    loading_animation()
    if user_input.lower() == captcha.lower():
        print("CAPTCHA verified successfully!")
        return True
    else:
        print("Incorrect CAPTCHA, please try again.")
        return False


List = []
aadhar = []
token = []

print("Hello and welcome to Agricredit, your trusted partner in agricultural financing.")
time.sleep(1)

print("\nLet's get started by understanding your needs better.")


while True:  
    print("\nHow may we assist you today?")
    print("1. First-time users")
    print("2. Previously signed-up users")
    print("3. Contact support")
    print("4. Learn about us")
    print("5. Update your account information")
    print("6. Exit")
    a = int(input("Please enter the number corresponding to your choice: "))
    loading_animation()

    if a == 1:  
        captcha = generate_captcha()
        print("CAPTCHA:", captcha)
        if verify_captcha(captcha):
            print("You are now verified :)")
            name = input("Enter your name: ")
            loading_animation()
            age = input("Enter your age: ")
            loading_animation()
            mobile = input("Enter your mobile number: +91")
            loading_animation()
            while not validate_mobile(mobile):
                print("Invalid mobile number. Please enter a valid 10-digit number starting with 6-9.")
                mobile = input("Enter your mobile number: +91")
                loading_animation()
            print("Thank you! You will shortly receive an SMS on what to do next.")
        else:
            print("CAPTCHA verification failed. Please try again.")

    elif a == 2:  
        captcha = generate_captcha()
        print("CAPTCHA:", captcha)
        if verify_captcha(captcha):
            bank = str(input("Enter the name of the bank you would like to use for the remainder of your loan duration: "))
            loading_animation()
            type = int(input("Please specify the type of loan: Press 1 for agricultural purposes, press 2 for others [education, gold, etc.]: "))
            loading_animation()

            ques = int(input("Press 3 if you have verified documents: "))
            loading_animation()
            if ques == 3:
                print("*****DISCLAIMER***** Any and all forms of exploitation will cause your verification to be revoked and strict actions taken against you.")
                b = str(input("Enter your name: "))
                loading_animation()
                List.append(b)
                c = int(input("Enter your age: "))
                loading_animation()
                List.append(c)
                d = int(input("Enter your total property value: "))
                loading_animation()
                List.append(d)
                num = int(input("Enter area of farm land in m^2: "))
                loading_animation()
                List.append(num)
                e = int(input("Enter your annual income: "))
                loading_animation()
                List.append(e)
                f = str(input("Would you like to add additional collateral? (Yes/No): "))
                loading_animation()

                colla = 0
                if f.lower() == "yes":
                    colla = int(input("Enter additional collateral value: "))
                    loading_animation()
                    List.append(colla)

                if type == 1:
                    loan = (colla + e + d) / num
                elif type == 2:
                    loan = (colla + e + d * 0.9) / num
                else:
                    print("Invalid loan type selected.")
                    continue  

                g = int(input("Enter your Aadhar card number: "))
                loading_animation()
                while len(str(g)) != 12:
                    print("Invalid Aadhar card number. Please resubmit the form and enter a valid Aadhar card number.")
                    g = int(input("Enter your Aadhar card number: "))
                    loading_animation()
                aadhar.append(g)

                y = int(input("Enter number of years for repayment: "))
                loading_animation()
                down = input("Would you like to apply for a downpayment? (Yes/No): ")
                loading_animation()

                if down.lower() == "yes":
                    downpayment = math.ceil(loan) * 0.2
                    grace_period = math.floor(y * 12 * 0.2)
                    print(f"You will have to pay a downpayment of {downpayment} rupees.")
                    print(f"Your grace period is {grace_period} months.")

                conf = str(input("Would you like to print your token number? (Yes/No): "))
                loading_animation()

                if conf.lower() == "yes":
                    token = [random.randint(1, 10) for _ in range(10)]
                    print(f"Your loan amount will be {math.ceil(loan)} rupees.")
                    print(f"Here is your token: {token}")

                if y > 5:
                    interest_rate = 5
                else:
                    interest_rate = 10

                annual_payment = math.ceil(loan) / y
                print(f"Interest rates will be at {interest_rate}%.")
                print(f"Your annual payment will be {annual_payment} rupees.")
                print("Thank you for your time! :)")
            else:
                print("You need verified documents to proceed.")
        else:
            print("CAPTCHA verification failed.")

    elif a == 3:  
        captcha = generate_captcha()
        print("CAPTCHA:", captcha)
        if verify_captcha(captcha):
            support = int(input("Press 1 to send a personalized email or press 2 to get direct contact with our customer support team: "))
            loading_animation()

            if support == 1:
                print("Please send an email to 'AgriCredit@gmail.com' and we will reply to you shortly.")
            elif support == 2:
                print("Please dial this number on your mobile phone: +91 05062626181")
            else:
                print("Invalid option selected. Please try again.")
        else:
            print("CAPTCHA verification failed.")

    elif a == 4:  
        print("**********")
        print("Our program provides an interface for users, especially struggling farmers, to find and receive appropriate loan amounts.")
        print("You will no longer need to fear loan sharks! Please feel free to use this program to your heart's content :)")
        print("**********")

    elif a == 5:  
        print("\nUpdating your account information:")
        new_name = input("Enter your new full name (leave blank to keep unchanged): ")
        loading_animation()
        new_email = input("Enter your new email address (leave blank to keep unchanged): ")
        loading_animation()
        while new_email and not validate_email(new_email):
            print("Invalid email address. Please try again.")
            new_email = input("Enter a valid email address (leave blank to keep unchanged): ")
            loading_animation()

        new_contact_number = input("Enter your new mobile number: +91 (leave blank to keep unchanged): ")
        loading_animation()
        while new_contact_number and not validate_mobile(new_contact_number):
            print("Invalid mobile number. Please enter a valid 10-digit number starting with 6-9.")
            new_contact_number = input("Enter your new mobile number: +91 (leave blank to keep unchanged): ")
            loading_animation()

        if new_name:
            List[0] = new_name
        if new_email:
            List[1] = new_email
        if new_contact_number:
            List[2] = new_contact_number

        print("Your account information has been updated successfully!")

    elif a == 6:  
        print("Thank you for using Agricredit.")
        break
