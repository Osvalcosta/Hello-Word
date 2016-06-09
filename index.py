cd /tmp
wget http://www.prestashop.com/download/old/prestashop_1.6.0.9.zip


apt-get install unzip


unzip prestashop_1.6.0.9.zip -d /var/www/html/

chown -R www-data:www-data /var/www/html/prestashop/

mysql -u root -p


REATE DATABASE prestashopdb;
CREATE USER prestashopuser@localhost IDENTIFIED BY 'prestashoppassword';
GRANT ALL PRIVILEGES on prestashopdb.* to prestashopuser@localhost

FLUSH PRIVILEGES;
exit

service apache2 restart
service mysql restart
