For this task, assume that you have been approached by a small financial
company and asked to create a program that allows the user to access two
different financial calculators: an investment calculator and a home loan
repayment calculator.

● Create a new Python file in this folder called finance_calculators.py.
● At the top of the file include the line import math
● Write the code that will do the following:
1. The user should be allowed to choose which calculation they want
to do. The first output that the user sees when the program runs
should look like this :

How the user capitalises their selection should not affect how the
program proceeds. I.e. ‘Bond’, ‘bond’, ‘BOND’ or ‘investment’,
‘Investment’, ‘INVESTMENT’, etc. should all be recognised as valid
entries. If the user doesn’t type in a valid input, show an appropriate
error message.
2. If the user selects ‘investment’, do the following:
■ Ask the user to input:
● The amount of money that they are depositing.
● The interest rate (as a percentage). Only the number
of the interest rate should be entered — don’t worry
about having to deal with the added ‘%’, e.g. The user
should enter 8 and not 8%.
● The number of years they plan on investing for.
● Then ask the user to input whether they want “simple”
or “compound” interest, and store this in a variable
called interest. Depending on whether they typed

“simple” or “compound”, output the appropriate
amount that they will get after the given period at the
interest rate. Look below in “Interest formulae” for the
formulae to be used


Interest formula:
The total amount when simple interest is applied is calculated as
follows: A = P(1 + r * t)
The Python equivalent is very similar: A =P*(1+r*t)
The total amount when compound interest is applied is calculated as
follows: A = P(1 + r) ^ t
The Python equivalent is slightly different: A = P* math.pow((1+r),t)
In the formulae above:
● ‘r’ is the interest entered above divided by 100, e.g. if 8% is entered,
then r is 0.08.
● ‘P’ is the amount that the user deposits.
● ‘t’ is the number of years that the money is being invested for.
● ‘A’ is the total amount once the interest has been applied.

■ Print out the answer!
■ Try enter 20 years and 8 (%) and see what the difference is
depending on the type of interest rate!
3. If the user selects ‘bond’, do the following:
■ Ask the user to input:
● The present value of the house. E.g. 100000
● The interest rate. E.g. 7
● The number of months they plan to take to repay the
bond. E.g. 120

Bond repayment formula:
The amount that a person will have to be repaid on a home loan each
month is calculated as follows: repayment = x = (i.P)/(1 - (1+i)^(-n))
In the formulae above:
● ‘P’ is the present value of the house

■ Calculate how much money the user will have to repay each month
and output the answer.



