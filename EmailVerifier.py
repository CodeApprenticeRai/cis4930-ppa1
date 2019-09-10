import re

class EmailVerifier:
    def command_line_routine(self):
        print("You've selected the function: Email Verifier")

        email_string = input("Enter an email string: ")

        print("The email string is{}valid.\n\n".format(" " if self.verify_email(email_string) else " not "))
        return None

    def verify_email(self, email):

        pattern = re.compile("[A-Za-z!$%*\+\-\=?^_{|}~]+[A-Za-z!$%*\+\-\=?^_{|}~.]*[A-Za-z!$%*\+\-\=?^_{|}~+]@[A-Za-z]*\.[A-Za-z]*")
        return True if pattern.fullmatch(email) else False

