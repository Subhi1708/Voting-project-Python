import datetime
import random
import smtplib
import mysql.connector

# Establish the database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="election_candidates"
)
mycursor = mydb.cursor()

def view_database():
    mycursor.execute("SELECT * FROM candidate_list")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)

def send_otp(receiver_mail):
    otp_number = random.randint(1000, 9999)
    x = datetime.datetime.now()
    try:
        # Establish connection to the SMTP server
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("subhikism@gmail.com", "kxfb imzp gejz rati")
        
        # Create the email message
        message = f"Subject: OTP Verification\n\nThanks for voting....OTP {otp_number}.....You Voted at {x}"
        
        # Send the email
        s.sendmail("subhikism@gmail.com", receiver_mail, message)
        s.quit()
        
        print("Mail Sent Successfully to", receiver_mail)
        return otp_number
    except Exception as e:
        print("Mail was not sent. Error:", e)
        return None

def verify_otp(expected_otp):
    user_otp = input("Enter the OTP sent to your email: ").strip()
    return user_otp == str(expected_otp)

def get_vote():
    print("Getting vote from User")
    print("1-BJP\n2-BSP\n3-CPI\n4-CPM\n5-INC\n6-NCP")
    user_input = input("Enter number to vote: ").strip()
    return user_input

def main():
    view_database()
    
    votes = {
        'BJP': 0,
        'BSP': 0,
        'CPI': 0,
        'CPM': 0,
        'INC': 0,
        'NCP': 0
    }
    
    max_votes = 20
    votes_count = 0
    
    while votes_count < max_votes:
        user_input = get_vote()
        
        if user_input == '1':
            votes['BJP'] += 1
        elif user_input == '2':
            votes['BSP'] += 1
        elif user_input == '3':
            votes['CPI'] += 1
        elif user_input == '4':
            votes['CPM'] += 1
        elif user_input == '5':
            votes['INC'] += 1
        elif user_input == '6':
            votes['NCP'] += 1
        elif user_input.lower() == 'exit':
            break
        else:
            print("Invalid Input")
            continue
        
        receiver_mail = input("Enter your email id: ").strip()
        otp_number = send_otp(receiver_mail)
        
        if otp_number and verify_otp(otp_number):
            print("OTP verified successfully. Your vote has been counted.")
            votes_count += 1
        else:
            print("OTP verification failed. Please try voting again.")
            # Decrement the vote count for the failed OTP
            if user_input == '1':
                votes['BJP'] -= 1
            elif user_input == '2':
                votes['BSP'] -= 1
            elif user_input == '3':
                votes['CPI'] -= 1
            elif user_input == '4':
                votes['CPM'] -= 1
            elif user_input == '5':
                votes['INC'] -= 1
            elif user_input == '6':
                votes['NCP'] -= 1

    count_votes(votes)

def count_votes(votes):
    print("\nFinal Count")
    print(f"BJP: {votes['BJP']}")
    print(f"BSP: {votes['BSP']}")
    print(f"CPI: {votes['CPI']}")
    print(f"CPM: {votes['CPM']}")
    print(f"INC: {votes['INC']}")
    print(f"NCP: {votes['NCP']}")

if __name__ == "__main__":
    main()
