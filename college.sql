-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema college
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema college
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `college` ;
USE `college` ;

-- -----------------------------------------------------
-- Table `college`.`student`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `college`.`student` (
  `student_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(20) NULL,
  `last_name` VARCHAR(20) NULL,
  `year` VARCHAR(20) NULL,
  PRIMARY KEY (`student_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `college`.`instructor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `college`.`instructor` (
  `instructor_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(20) NULL,
  `last_name` VARCHAR(20) NULL,
  `degree` VARCHAR(45) NULL,
  PRIMARY KEY (`instructor_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `college`.`course`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `college`.`course` (
  `course_id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  PRIMARY KEY (`course_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `college`.`lesson`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `college`.`lesson` (
  `lesson_id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(50) NULL,
  PRIMARY KEY (`lesson_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `college`.`learns`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `college`.`learns` (
  `student_id` INT NOT NULL,
  `course_id` INT NOT NULL,
  PRIMARY KEY (`student_id`, `course_id`),
  INDEX `course_id_idx` (`course_id` ASC),
  CONSTRAINT `student_id`
    FOREIGN KEY (`student_id`)
    REFERENCES `college`.`student` (`student_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `course_id`
    FOREIGN KEY (`course_id`)
    REFERENCES `college`.`course` (`course_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `college`.`teaches`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `college`.`teaches` (
  `instructor_id` INT NOT NULL,
  `course_id` INT NOT NULL,
  PRIMARY KEY (`instructor_id`, `course_id`),
  INDEX `course_id_idx` (`course_id` ASC),
  CONSTRAINT `instructor_id`
    FOREIGN KEY (`instructor_id`)
    REFERENCES `college`.`instructor` (`instructor_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `course_id_2`
    FOREIGN KEY (`course_id`)
    REFERENCES `college`.`course` (`course_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `college`.`contains`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `college`.`contains` (
  `course_id` INT NOT NULL,
  `lesson_id` INT NOT NULL,
  PRIMARY KEY (`course_id`, `lesson_id`),
  INDEX `lesson_id_idx` (`lesson_id` ASC),
  CONSTRAINT `course_id_3`
    FOREIGN KEY (`course_id`)
    REFERENCES `college`.`course` (`course_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `lesson_id`
    FOREIGN KEY (`lesson_id`)
    REFERENCES `college`.`lesson` (`lesson_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
