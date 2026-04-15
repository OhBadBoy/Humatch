-- =====================================================================
-- Jeu de données de test "humatch_recruitment"
-- =====================================================================

USE humatch_recruitment;

-- ----------------------------
-- companies
-- ----------------------------
INSERT INTO companies (name, sector, description, contact_email, phone, website)
VALUES
('TechSolutions', 'Informatique', 'SSII spécialisée web & cloud.', 'contact@techsolutions.fr', '01 44 55 66 77', 'https://www.techsolutions.fr'),
('DigitalBoost', 'Marketing', 'Agence de marketing digital & SEO.', 'hello@digitalboost.fr', '04 72 10 20 30', 'https://www.digitalboost.fr'),
('Clinique Saint-Louis', 'Santé', 'Établissement de santé privé.', 'rh@stlouis-clinique.fr', '04 91 22 33 44', 'https://www.stlouis-clinique.fr'),
('InnoTech', 'Technologies', 'Scale-up B2B SaaS.', 'jobs@innotech.io', '05 56 12 34 56', 'https://www.innotech.io'),
('Constructix', 'BTP', 'Génie civil & bâtiment.', 'recrutement@constructix.fr', '01 53 00 11 22', 'https://www.constructix.fr');

-- ----------------------------
-- people
-- (password_hash : valeurs factices pour la démo)
-- ----------------------------
-- ----------------------------
-- people (avec company_id pour RH)
-- ----------------------------
INSERT INTO people (first_name, last_name, email, phone, username, password_hash, is_admin, company_id)
VALUES
('Alice',  'Martin',   'alice.martin@example.com',   '06 11 22 33 44', 'user1', '$2b$12$demoAliceHash............', 1, NULL), -- admin
('Bob',    'Durand',   'bob.durand@example.com',     '06 22 33 44 55', 'user2', '$2b$12$demoBobHash..............', 0, 2),     -- RH chez DigitalBoost
('Claire', 'Bernard',  'claire.bernard@example.com', '06 33 44 55 66', 'user3', '$2b$12$demoClaireHash...........', 0, 3),     -- RH chez Clinique Saint-Louis
('David',  'Petit',    'david.petit@example.com',    '06 44 55 66 77', 'user4', '$2b$12$demoDavidHash............', 0, 4),     -- RH chez InnoTech
('Emma',   'Moreau',   'emma.moreau@example.com',    '06 55 66 77 88', 'user5', '$2b$12$demoEmmaHash.............', 0, NULL);  -- Candidat
-- ----------------------------
-- advertisements
-- (published_at a une valeur par défaut, mais on met des dates explicites pour le test)
-- ----------------------------
INSERT INTO advertisements
(company_id, title, short_description, full_description, wage, location, working_time, published_at, expires_at, created_by)
VALUES
(1, 'Développeur Full Stack (React/Flask)',
 'Construire des features web end-to-end.',
 'Vous rejoignez une squad agile pour développer une plateforme SaaS (React, Flask, SQL).',
 42000.00, 'Paris 15e (75)', 'CDI • 35h', '2025-09-01', '2026-03-01', 1),

(2, 'Chef de projet Marketing Digital',
 'Piloter campagnes SEO/SEA multi-clients.',
 'Coordination des équipes créa & data, suivi KPI, relation client.',
 30000.00, 'Lyon 3e (69)', 'CDD (6 mois)', '2025-08-20', '2025-12-31', 2),

(3, 'Infirmier / Infirmière (H/F)',
 'Soins de nuit en service médecine.',
 'Accueil patients, protocoles, traçabilité, travail en équipe.',
 2900.00, 'Marseille 8e (13)', 'CDI • Temps plein', '2025-07-15', '2026-01-15', 3),

(4, 'Commercial B2B (Tech)',
 'Développer le portefeuille clients SaaS.',
 'Prospection, démos produit, négociation, closing, 20% déplacements.',
 48000.00, 'Bordeaux Centre (33)', 'CDI • Télétravail 2j/sem', '2025-09-10', '2026-03-10', 4),

(1, 'DevOps / SRE',
 'Automatisation CI/CD & infra cloud.',
 'Terraform, Docker, observabilité, SLO/SLI, astreintes tournantes.',
 55000.00, 'Télétravail (France)', 'CDI', '2025-08-01', '2026-02-01', 1),

(5, 'Conducteur de travaux',
 'Chantiers gros œuvre IDF.',
 'Planification, suivi qualité/sécurité, pilotage sous-traitants.',
 38000.00, 'Nanterre (92)', 'CDI', '2025-07-01', '2026-01-01', 5);

-- ----------------------------
-- applications
-- (status: 'received' | 'in_review' | 'rejected' | 'accepted')
-- ----------------------------
INSERT INTO application
(advertisement_id, person_id, applicant_name, applicant_email, applicant_phone, message, status)
VALUES
(1, 2, 'Bob Durand', 'bob.durand@example.com', '06 22 33 44 55', 'Intéressé par le poste Full Stack.', 'in_review'),
(1, NULL, 'Julie Robert', 'julie.rob@example.com', '06 77 88 99 00', 'Expérience 3 ans React/Flask.', 'received'),
(2, 3, 'Claire Bernard', 'claire.bernard@example.com', '06 33 44 55 66', 'Profil marketing data-driven.', 'received'),
(3, NULL, 'Sophie Leroy', 'sophie.leroy@example.com', '06 12 34 56 78', 'Disponible rapidement pour nuits.', 'in_review'),
(4, 4, 'David Petit', 'david.petit@example.com', '06 44 55 66 77', 'Expérience Sales SaaS > 4 ans.', 'received'),
(6, NULL, 'Hugo Nicolas', 'hugo.nicolas@example.com', '06 90 12 34 56', 'Mobile IDF, dispo sous 1 mois.', 'received');
