CREATE SCHEMA `iot` ;

CREATE TABLE `iot`.`users` (
  `ID` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`));

INSERT INTO `iot`.`users` (`ID`) VALUES ('Axel');
INSERT INTO `iot`.`users` (`ID`) VALUES ('Edgar');
INSERT INTO `iot`.`users` (`ID`) VALUES ('Angeles');
INSERT INTO `iot`.`users` (`ID`) VALUES ('Myron');
INSERT INTO `iot`.`users` (`ID`) VALUES ('Johna');
INSERT INTO `iot`.`users` (`ID`) VALUES ('Javier');



CREATE TABLE `iot`.`reg` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `humedad` VARCHAR(45) NOT NULL,
  `temperatura` VARCHAR(45) NOT NULL,
  `luminosidad` VARCHAR(45) NOT NULL,
  `fecha` VARCHAR(45) NOT NULL,
  `hora` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`));

ALTER TABLE `iot`.`reg` 
ADD INDEX `nombre_idx` (`nombre` ASC);
ALTER TABLE `iot`.`reg` 
ADD CONSTRAINT `nombre`
  FOREIGN KEY (`nombre`)
  REFERENCES `iot`.`users` (`ID`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;



CREATE TABLE `iot`.`roc` (
`ID` INT NOT NULL AUTO_INCREMENT,
`nombre` VARCHAR(45) NOT NULL,
`estado` VARCHAR(45) NOT NULL,
`fecha` VARCHAR(45) NOT NULL,
`hora` VARCHAR(45) NOT NULL,
PRIMARY KEY (`ID`));

ALTER TABLE `iot`.`roc` 
ADD INDEX `nombre_roc_idx` (`nombre` ASC),
DROP INDEX `nombre_idx` ;
ALTER TABLE `iot`.`roc` 
ADD CONSTRAINT `nombre_roc`
  FOREIGN KEY (`nombre`)
  REFERENCES `iot`.`users` (`ID`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
