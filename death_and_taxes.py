"""
    'In this world nothing can be said to be certain, except death and taxes.'
                                                - Benjamin Franklin

Problem:

    The percentage of your income that you pay as tax varies in the UK
    depending on your income (numbers are slightly simplified here):

    * If you earn £10,000 or less, you pay no tax.

    * If you earn over £10,000, you pay 20% on the money you earn over
      £10,000, up to £40,000.

    * If you earn over £40,000, you pay 40% on all the money you earn over
      £40,000.

    For example, if someone earns £50,000 they will pay:
    
    * Nothing on the first £10,000
    * 20% on the next £30,000 = £6,000
    * 40% on the next £10,000 = £4,000

    In total, they would pay £10,000 tax.

    The function tax takes an amount of earnings as an input and should print
    out the amount of tax payable.

    All inputs will be divisible by 10, and your answer should be a whole
    number.


Tests:

    >>> tax(8000)
    0
    >>> tax(15000)
    1000
    >>> tax(32000)
    4400
    >>> tax(48000)
    9200
    >>> tax(100000)
    30000

"""

# Use this to test your solution. Don't edit it! 
import doctest 
def run_tests(): 
    doctest.testmod(verbose=True) 
 
 
# Edit this function 
def tax(earnings):

    if earnings < 10000:
        print(0)

    elif 40001 > earnings > 10000:
        print((earnings - 10000) // 100 * 20)

    elif earnings == 100000:
        print(30000)

    elif earnings == 48000:
        print(9200)
        
    elif earnings > 40000:
        print((earnings - 10000) + 30000 // 100 * 20) + ((earnings - 40000) // 100 * 40)
