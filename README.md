Look up a call sign.

I created this as an alternative to having to go to https://www.qrz.com .
Two reasons - I'm lazy and I wanted to write something to hone my Python skillz.

It's not perfect and it will probably break. I'm a Python NOOB so go ahead and roast/
slag if you want. 

It utilizes Pandas, sqllite and some SQL commands. 

1. I did this on PyCharm PyCharm 2023.2.7 (Professional Edition)
2. It's on a MacBook Pro 2020
3. External stuff - sqllite3 and Pandas are needed
4. You need to connect to the Internet (obviously) and it grabs data from https://callook.info/ <br> and mine returns in JSON
5. Pandas seemed to be easiest to work with as I didn't need to do anything fancy
6. Create a file - database_file='results.db'
7. It will store all of your queries in a sqllite3 database file
8. I've not included duplicate checking so that could be next. 
8. I included the linter output - I know it's still not 100%, but I'm a NOOB
9. If you found that I have forgotten something feel free to let me know

Thanks for reading - Glen

KC1RTD

PyLint Report
(AmateurRadio) (base) glenmillard@Glens-MBP AmateurRadio % pylint grm_database_store_callsign.py
************* Module copy_of_database_store_callsign
grm_database_store_callsign.py:1:0: C0114: Missing module docstring (missing-module-docstring)
grm_database_store_callsign.py:18:0: C0116: Missing function or method docstring (missing-function-docstring)
grm_database_store_callsign.py:64:12: E1101: Instance of 'JsonReader' has no 'iloc' member (no-member)
grm_database_store_callsign.py:65:11: E1101: Instance of 'JsonReader' has no 'iloc' member (no-member)
grm_database_store_callsign.py:66:15: E1101: Instance of 'JsonReader' has no 'iloc' member (no-member)
grm_database_store_callsign.py:67:15: E1101: Instance of 'JsonReader' has no 'iloc' member (no-member)

 ------------------------------------------------------------------
 Your code has been rated at 4.63/10 (previous run: 4.39/10, +0.24)