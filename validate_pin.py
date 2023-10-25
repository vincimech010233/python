"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false

def validate_pin(pin):
    #return true or false
"""

def validate_pin(pin):
    if pin == "-":
        return False
    # isdigit() verifica si es todo la cadena numerica
    return (len(pin) == 4 or len(pin) == 6) and pin.isdigit() 

print(validate_pin("-12345"))