-- Base de données "humatch_recrutement"
CREATE DATABASE IF NOT EXISTS humatch_recrutement
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_0900_ai_ci;
USE humatch_recrutement;

-- Table companies
CREATE TABLE companies (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(200) NOT NULL,
  sector VARCHAR(120),
  description TEXT,
  contact_email VARCHAR(255),
  phone VARCHAR(40),
  website VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX (name)
) ENGINE=InnoDB;

-- Table people
CREATE TABLE people (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(120) NOT NULL,
  last_name VARCHAR(120) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  phone VARCHAR(40),
  username VARCHAR(40),
  password_hash VARCHAR(255),
  is_admin TINYINT(1) NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX (last_name),
  INDEX (email)
) ENGINE=InnoDB;

-- Ajout de company_id + clé étrangère pour RH
ALTER TABLE people
ADD COLUMN company_id INT UNSIGNED;

ALTER TABLE people
ADD CONSTRAINT fk_people_company
FOREIGN KEY (company_id) REFERENCES companies(id)
ON DELETE SET NULL ON UPDATE CASCADE;

-- Table advertisements
CREATE TABLE advertisements (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  company_id INT UNSIGNED,
  title VARCHAR(255) NOT NULL,
  short_description VARCHAR(300) NOT NULL,
  full_description TEXT,
  wage DECIMAL(10,2),
  CHECK (wage >= 0),
  location VARCHAR(150),
  working_time VARCHAR(60),
  published_at DATE DEFAULT (CURRENT_DATE),
  expires_at DATE,
  created_by INT UNSIGNED,
  FOREIGN KEY (company_id) REFERENCES companies(id)
    ON DELETE SET NULL ON UPDATE CASCADE,
  FOREIGN KEY (created_by) REFERENCES people(id)
    ON DELETE SET NULL ON UPDATE CASCADE,
  INDEX (company_id), INDEX (title)
) ENGINE=InnoDB;

-- Table applications
CREATE TABLE applications (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  advertisement_id INT UNSIGNED NOT NULL,
  person_id INT UNSIGNED,
  applicant_name VARCHAR(200) NOT NULL,
  applicant_email VARCHAR(255) NOT NULL,
  applicant_phone VARCHAR(40),
  message TEXT,
  status ENUM('received', 'in_review', 'rejected', 'accepted')
    NOT NULL DEFAULT 'received',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (advertisement_id) REFERENCES advertisements(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (person_id) REFERENCES people(id)
    ON DELETE SET NULL ON UPDATE CASCADE,
  INDEX (advertisement_id), INDEX (person_id), INDEX (status)
) ENGINE=InnoDB;
