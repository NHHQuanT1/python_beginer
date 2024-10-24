def emailProcess(email):
    email_username = email[0:email.index("@")]
    email_domain = email[email.index("@")+1]

    return [email_username, email_domain]


def main():
    email = input("Please enter your email address: ").strip() # chi nhan vao chuoi
    emailProcess(email)

if __name__ == "__main__":
    main()