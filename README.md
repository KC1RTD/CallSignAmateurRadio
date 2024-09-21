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