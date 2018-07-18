a=0+inputbox("long：","Input - perimeter area calculator v0.0.1.0")
b=0+inputbox("wide：","Input - perimeter area calculator v0.0.1.0")
c=a+b
call all
sub err
 a = Inputbox("long：","Input - perimeter area calculator v0.0.1.0")
 b = InputBox("wide：","Input - perimeter area calculator v0.0.1.0")
 call all
end sub
sub all
if not(isnumeric(a)) or not(isnumeric(c))Then
msgbox "The value is wrong, please try again.",,"error - circumference area calculator v0.0.1.0"
 call err
Else
msgbox c*2,,"Circumference - circumference area calculator v0.0.1.0"
msgbox a*b,,"Area - circumference area calculator v0.0.1.0"
end if
end sub
