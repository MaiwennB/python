-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Mer 14 Février 2018 à 00:59
-- Version du serveur :  5.7.21-0ubuntu0.16.04.1
-- Version de PHP :  7.0.22-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `python`
--

-- --------------------------------------------------------

--
-- Structure de la table `infosPC`
--

CREATE TABLE `infosPC` (
  `id` int(5) NOT NULL,
  `nomHost` varchar(255) DEFAULT NULL,
  `disk` varchar(255) DEFAULT NULL,
  `OS` varchar(255) DEFAULT NULL,
  `CPU_STAT` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `infosPC`
--

INSERT INTO `infosPC` (`id`, `nomHost`, `disk`, `OS`, `CPU_STAT`) VALUES
(1, 'PC1', '[13604339712, 8145350656, 4744335360, 63.2]', 'windows', NULL),
(2, 'PC2', '[96280129536,13072621,648,14.3]', 'windows', NULL),
(3, 'rt-VirtualBox', '[13604339712, 8145350656, 4744335360, 63.2]', 'posix', NULL),
(4, 'elo-X55OLD', '[96280129536,13072621,648,14.3]', 'posix', '[13740295, 33324573, 2219808, 0]'),
(5, 'rt-VirtualBox', '[13604339712, 8176062464, 4713623552, 63.4]', 'posix', '[54786159, 5438516, 2496946, 0]');

--
-- Index pour les tables exportées
--

--
-- Index pour la table `infosPC`
--
ALTER TABLE `infosPC`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `infosPC`
--
ALTER TABLE `infosPC`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
