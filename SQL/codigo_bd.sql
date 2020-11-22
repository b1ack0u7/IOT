CREATE SCHEMA `iot` ;

CREATE TABLE `iot`.`users` (
  `ID` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`));

INSERT INTO `iot`.`users` (`ID`) VALUES ('Axel');
INSERT INTO `iot`.`users` (`ID`) VALUES ('Edgar');
INSERT INTO `iot`.`users` (`ID`) VALUES ('Angeles');
INSERT INTO `iot`.`users` (`ID`) VALUES ('Myron');


CREATE TABLE `iot`.`reg` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `humedad` VARCHAR(45) NOT NULL,
  `temperatura` VARCHAR(45) NOT NULL,
  `luminosidad` VARCHAR(45) NOT NULL,
  `fecha` VARCHAR(45) NOT NULL,
  `hora` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`));


CREATE TABLE `iot`.`reg_rociado` (
  `ID` VARCHAR(45) NOT NULL,
  `fecha` VARCHAR(45) NOT NULL,
  `hora` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`));

ALTER TABLE `iot`.`reg_rociado` 
ADD CONSTRAINT `ID`
  FOREIGN KEY (`ID`)
  REFERENCES `iot`.`users` (`ID`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;