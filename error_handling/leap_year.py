def is_leap_year(year):
    if year<0:
        return False
    if(year%100==0 and year%400==0 or year%100!=0 and year%4==0):
        return True
    else:
        return False

def test_is_laep_year():
    assert is_leap_year(2024)==True,"non centuary year chk failed"
    assert is_leap_year(2025)==False,"invalid noncentuary chk failed"
    assert is_leap_year(2000)==True,"centuay laepyear chk failed"
    assert is_leap_year(1900)==False,"invalid centuary chk failed"
    assert is_leap_year(-2024)==False,"invalid year chk failed"
try:
    test_is_laep_year()
    print("test case passed")
except Exception as e:
    print("test failed",e)