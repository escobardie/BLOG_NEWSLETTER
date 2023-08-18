drop database blog_newslatter;

show databases;
CREATE DATABASE blog_newslatter;
USE blog_newslatter;
SHOW TABLES;


/* DDL CON ENFOQUE EN SEGURIDAD*/
/* creamos un usuario con persimos solo para acceder a la base de datos db_blog*/
/* usuario: user1,  password: user-1 */
CREATE USER 'user1'@'localhost' identified by 'user-1';

GRANT ALL PRIVILEGES ON blog_newslatter.* TO user1@localhost;
FLUSH PRIVILEGES;

DROP USER 'user1'@'localhost';

/* DDL CON ENFOQUE EN SEGURIDAD*/


SHOW TABLES;

select * from auth_user;
select * from letter_subscribers;


