-- =====================================================================
-- Base de données "humatch"
-- =====================================================================

CREATE DATABASE IF NOT EXISTS humatch
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_0900_ai_ci;
USE humatch;

CREATE TABLE adresse (
  id INT AUTO_INCREMENT PRIMARY KEY,
  ligne VARCHAR(120) NOT NULL,
  code_postal VARCHAR(20),
  ville VARCHAR(80),
  region VARCHAR(80),
  pays VARCHAR(80) DEFAULT 'France'
) ENGINE=InnoDB;

CREATE TABLE entreprise (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(100) NOT NULL,
  description TEXT,
  secteur_activite VARCHAR(100),
  adresse_id INT,
  FOREIGN KEY (adresse_id) REFERENCES adresse(id) ON DELETE SET NULL
) ENGINE=InnoDB;

CREATE TABLE personne (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(50) NOT NULL,
  prenom VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  telephone VARCHAR(20),
  adresse_id INT,
  FOREIGN KEY (adresse_id) REFERENCES adresse(id) ON DELETE SET NULL
) ENGINE=InnoDB;   

CREATE TABLE annonce (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titre VARCHAR(100) NOT NULL,
  description TEXT,
  date_publication DATE NOT NULL,
  date_expiration DATE,
  salaire DECIMAL(10,3),
  type_contrat VARCHAR(50),
  entreprise_id INT,
  adresse_id INT,
  FOREIGN KEY (entreprise_id) REFERENCES entreprise(id) ON DELETE CASCADE,
  FOREIGN KEY (adresse_id) REFERENCES adresse(id) ON DELETE SET NULL
) ENGINE=InnoDB;

CREATE TABLE candidature (
  id INT AUTO_INCREMENT PRIMARY KEY,
  date_candidature DATE NOT NULL,
  statut VARCHAR(50) DEFAULT 'En attente',
  cv TEXT,
  lettre_motivation TEXT,
  personne_id INT,
  annonce_id INT,
  FOREIGN KEY (personne_id) REFERENCES personne(id) ON DELETE CASCADE,
  FOREIGN KEY (annonce_id) REFERENCES annonce(id) ON DELETE CASCADE
) ENGINE=InnoDB;