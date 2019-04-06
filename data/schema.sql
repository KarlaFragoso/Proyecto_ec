CREATE DATABASE proyecto_ec;

USE proyecto_ec;

CREATE TABLE users(
    username varchar(20) NOT NULL PRIMARY KEY,
    password varchar(32) NOT NULL,
    privilege integer NOT NULL DEFAULT -1,
    status integer NOT NULL DEFAULT 1,
    name varchar(150) NOT NULL,
    email varchar(100) NOT NULL,
    other_data varchar(50) NOT NULL,
    user_hash varchar(32) NOT NULL,
    change_pwd integer NOT NULL DEFAULT 1,
    created timestamp NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE sessions(
    session_id char(128) UNIQUE NOT NULL,
    atime timestamp NOT NULL default current_timestamp,
    data text
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE logs( 
    id_log integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username varchar(20) NOT NULL,
    ip varchar(16) NOT NULL,
    access timestamp NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE usuarios (
    id_usuario integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre varchar(20) NOT NULL,
    usuario varchar(20) NOT NULL,
    clave varchar(20)  NOT NULL,
    edad int(11) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE contactos (
   id_contacto integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
   nombre varchar(35) NOT NULL,
   telefono varchar(15) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE detalle (
   id_detalle int(11) NOT NULL,
   mensaje varchar(150) NOT NULL,
   direccion varchar(100) NOT NULL,
   coordenadas  varchar(150) NOT NULL,
   id_usuario int(11) NOT NULL,
   id_contacto int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE detalle
  ADD CONSTRAINT  detalle_ibfk_1 FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario),
  ADD CONSTRAINT detalle_ibfk_2 FOREIGN KEY (id_contacto) REFERENCES contactos (id_contacto);



INSERT INTO users (username, password, privilege, status, name, email, other_data, user_hash, change_pwd)
VALUES ('admin',MD5(concat('admin', 'kuorra_key')), 0, 1, 'Admin', 'admin@gmail.com','TIC:SI', MD5(concat('admin', 'kuorra_key', '2016/06/04')), 0),
('guess',MD5(concat('guess', 'kuorra_key')), 1, 1, 'Guess', 'guess@gmail.com','TIC:SI', MD5(concat('guess', 'kuorra_key','2016/06/04')), 0);


INSERT INTO usuarios (nombre, usuario, clave, edad) VALUES
( 'Karla Fragoso', 'wanni', '123', 21),
('agustin monter', 'agus', '123', 20);
INSERT INTO contactos ( nombre, telefono) VALUES
('Mama', '7891186959'),
('mama', '7898988459');



SELECT * FROM users;
SELECT * FROM sessions;

CREATE USER 'AK'@'localhost' IDENTIFIED BY 'AK.2019';
GRANT ALL PRIVILEGES ON proyecto_ec.* TO 'AK'@'localhost';
FLUSH PRIVILEGES;
