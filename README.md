# PlasmaPS 

This is a final year project by myself. This is web application on medical side that helps connect donors and recipients.

To try this website locally, follow my instructions:

1. $git clone https://github.com/SIWNUS/PlasmaPS

2. $sudo apt install mysql

3. $mysql -u root -p

4. Create a mysql database 'webapp' 

5. exit mysql

6. Now do : $pip install -r requirements.txt

7. Then, follow the below instructions to make it work or you will get an error called, "No module called 'MySQLdb' found"

8. $pip install mysqlclient or $pip3 install mysqlclient

9. now based on your OS, follow the corresponding instruction.
   Ubuntu: sudo apt install python3-dev default-libmysqlclient-dev build-essential
   CentOS: sudo yum install python3-dev default-libmysqlclient-dev build-essential
   Fedora: sudo dnf install python3-dev default-libmysqlclient-dev build-essential

9. Now try to import the module in python. It will work.

10. Now just do "$python main.py" and it will run.
