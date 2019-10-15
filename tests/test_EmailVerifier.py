import pytest
from .. import EmailVerifier

'''
Conditions:
    * Should accept: int age, float annual salary, float percentage saved
    * Should return what age savings goal will be met.
'''

# Case of empty string
def test1(applet=EmailVerifier.EmailVerifier()):
    test_result = applet.verify_email("")
    assert test_result  == False

# Case of invalid email becuase of email non-domain portion of email starting with a '.'
def test2(applet=EmailVerifier.EmailVerifier()):
    test_result = applet.verify_email(".dfdsaf@gmail.com")
    assert test_result == False

# Case of invalid email becuase of email non-domain portion of email ending with a '.'
def test3(applet=EmailVerifier.EmailVerifier()):
    test_result = applet.verify_email("sdfsdklfj.@gmail.com")
    assert test_result == False

# Case of valid email
def test4(applet=EmailVerifier.EmailVerifier()):
    test_result = applet.verify_email("j.!$%*+-=?^_{|}~.smith@gmail.com")
    assert test_result == True

applet = EmailVerifier.EmailVerifier()
test1(applet)
test2(applet)
test3(applet)
test4(applet)
