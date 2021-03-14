CREATE TABLE members (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    payed_cotisation INT NOT NULL);

CREATE TABLE supa_secret_table (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    flag VARCHAR(255) NOT NULL);

INSERT INTO members(name, address, payed_cotisation) VALUES ('Leonard de Vinci', '34 Avenue Leonard-de-Vinci, 92400 Courbevoie', 1);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Louis Dupont', '37 Rue des Smith, 92800 Puteaux', 1);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Astrid Vallee', '97 rue de Noel, 62731 Remy', 0);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Marthe Bourgeois', 'rue Bertrand Lamy, 68108 Besnard', 0);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Alfred Leger', '63 rue Danielle Potier, 22826 Diaz-la-Foret', 0);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Francois Ribeiro de Huet', '1 chemin Ines Navarro, 98611 Renault', 0);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Anastasie Leclerc', '80 chemin Denis, 80249 Brunet', 1);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Alphonse du Cordier', '29 avenue de Ramos, 08438 Morenonec', 1);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Simone Henry', '2 chemin Alexandre Guillaume, 63479 Gillet-la-Foret', 1);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Suzanne Seguin', '506 rue Anais Diaz, 62145 Chevallier-sur-Mer', 1);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Stephane Schmitt-Pruvost', '8 rue Laurent, 15343 Royer', 0);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Theodore Weber', '57 rue Guilbert, 17485 Sainte William', 1);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Alix Bouchet', '54 rue Chauvin, 32693 Saint Josephine', 1);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Victoire Le Marchal', '476 rue de Dufour, 93150 Saint Claudenec', 1);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Honore Lecoq-Jacquet', '5 boulevard Guy Leclercq, 18413 DialloBourg', 0);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Michelle Pereira', 'rue de Legros, 70342 Navarro-la-Foret', 1);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Adele du Morvan', '59 rue Marianne Pottier, 26572 Lejeune', 0);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Lucy Blondel', 'chemin Matthieu Legrand, 60776 Caron', 1);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Andree-Juliette Besnard', '90 boulevard de Masse, 91979 Barbier', 0);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Andre Martel', '44 avenue Da Silva, 00087 Bazinnec', 0);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Valerie Martins', '20 rue Richard Lebon, 92638 Rolland', 1);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Noel Fabre', '4 avenue de Maillet, 26432 Saint Benjamin-sur-Mer', 1);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Celina Durand de la Pascal', 'chemin Roy, 81769 Lefort', 0);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Henriette Guillaume', 'boulevard de Verdier, 02828 ThomasVille', 1);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Raymond Mallet', '23 rue Constance Herve, 30552 Chauvin-sur-Chauvin', 0);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Genevieve Jean', '432 boulevard Joseph Riou, 43587 GuerinBourg', 0);
INSERT INTO members(name, address, payed_cotisation) VALUES ('Penelope Schmitt', 'rue Bernadette Lejeune, 29030 Saint Lucie-la-Foret', 1);

INSERT INTO supa_secret_table(flag) VALUES ('dvCTF{1_h0p3_u_d1dnt_us3_sqlm4p}');
