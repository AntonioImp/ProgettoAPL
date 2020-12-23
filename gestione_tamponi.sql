-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Dic 23, 2020 alle 17:38
-- Versione del server: 10.4.14-MariaDB
-- Versione PHP: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gestione_tamponi`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `booking`
--

CREATE TABLE `booking` (
  `practical_num` int(11) NOT NULL,
  `CF_U` varchar(16) NOT NULL,
  `ID_M` int(11) NOT NULL,
  `CF_M` varchar(16) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `time_taken` time DEFAULT NULL,
  `result` enum('positivo','negativo') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `booking`
--

INSERT INTO `booking` (`practical_num`, `CF_U`, `ID_M`, `CF_M`, `date`, `time`, `time_taken`, `result`) VALUES
(10, 'MPLNTN96S25F158E', 15, 'C', '2020-12-07', '08:33:00', '00:04:00', 'negativo'),
(17, 'MPLNTN96S25F158E', 15, 'G', '2020-12-17', '08:30:00', '00:02:00', 'negativo'),
(19, 'A', 15, 'A', '2020-12-17', '08:40:00', '00:06:00', 'negativo'),
(20, 'B', 15, 'B', '2020-12-17', '08:40:00', '00:05:00', 'negativo'),
(30, 'D', 15, 'E', '2020-12-17', '08:30:00', '00:03:00', 'negativo'),
(31, 'MPLNTN96S25F158E', 15, 'A', '2020-12-18', '08:30:00', '00:45:00', 'negativo'),
(35, 'MPLNTN96S25F158E', 15, 'A', '2020-12-21', '08:30:00', NULL, NULL);

-- --------------------------------------------------------

--
-- Struttura della tabella `credentials`
--

CREATE TABLE `credentials` (
  `username` varchar(16) NOT NULL,
  `password` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `credentials`
--

INSERT INTO `credentials` (`username`, `password`) VALUES
('A', 'A'),
('B', 'B'),
('C', 'C'),
('D', 'D'),
('E', 'E'),
('MPLNTN96S25F158E', 'antonio');

-- --------------------------------------------------------

--
-- Struttura della tabella `docs`
--

CREATE TABLE `docs` (
  `CF` varchar(16) NOT NULL,
  `name` varchar(40) NOT NULL,
  `surname` varchar(40) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `mail` varchar(254) NOT NULL,
  `avarage_time` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `docs`
--

INSERT INTO `docs` (`CF`, `name`, `surname`, `phone`, `mail`, `avarage_time`) VALUES
('A', 'A', 'A', 'A', 'A', '00:25:30'),
('B', 'B', 'B', 'B', 'B', '00:05:00'),
('C', 'C', 'C', 'C', 'C', '00:04:00'),
('D', 'D', 'D', 'D', 'D', '00:03:00'),
('E', 'E', 'E', 'E', 'E', '00:03:00'),
('F', 'F', 'F', 'F', 'F', NULL),
('G', 'G', 'G', 'G', 'G', '00:02:00'),
('H', 'H', 'H', 'H', 'H', NULL),
('I', 'I', 'I', 'I', 'I', NULL),
('L', 'H', 'H', 'L', 'H', NULL);

-- --------------------------------------------------------

--
-- Struttura della tabella `docs_list`
--

CREATE TABLE `docs_list` (
  `CF` varchar(16) NOT NULL,
  `day` enum('lun','mar','mer','gio','ven','sab') NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `docs_list`
--

INSERT INTO `docs_list` (`CF`, `day`, `id`) VALUES
('A', 'lun', 15),
('A', 'mar', 15),
('A', 'mer', 15),
('A', 'gio', 15),
('A', 'ven', 15),
('B', 'lun', 15),
('B', 'mar', 15),
('B', 'mer', 15),
('B', 'gio', 15),
('B', 'ven', 15),
('C', 'lun', 15),
('C', 'mar', 15),
('C', 'mer', 15),
('C', 'gio', 15),
('C', 'ven', 15),
('D', 'lun', 15),
('D', 'mar', 15),
('D', 'mer', 15),
('D', 'gio', 15),
('D', 'ven', 15),
('E', 'lun', 15),
('E', 'mar', 15),
('E', 'mer', 15),
('E', 'gio', 15),
('E', 'ven', 15),
('F', 'ven', 17),
('G', 'lun', 15),
('G', 'mar', 15),
('G', 'mer', 15),
('G', 'gio', 15),
('G', 'ven', 15);

-- --------------------------------------------------------

--
-- Struttura della tabella `medical_centers`
--

CREATE TABLE `medical_centers` (
  `id` int(11) NOT NULL,
  `medical_name` varchar(40) NOT NULL,
  `p_IVA` varchar(11) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `mail` varchar(254) NOT NULL,
  `CAP` varchar(5) NOT NULL,
  `city` varchar(40) NOT NULL,
  `street` varchar(300) NOT NULL,
  `n_cv` int(11) NOT NULL,
  `start_time` time NOT NULL DEFAULT '08:00:00',
  `end_time` time NOT NULL DEFAULT '12:00:00',
  `default_interval` time NOT NULL DEFAULT '00:10:00'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `medical_centers`
--

INSERT INTO `medical_centers` (`id`, `medical_name`, `p_IVA`, `phone`, `mail`, `CAP`, `city`, `street`, `n_cv`, `start_time`, `end_time`, `default_interval`) VALUES
(10, 'B', 'B', 'B', 'antonioimpala251196@gmail.com', 'B', 'B', 'B', 24, '08:00:00', '12:00:00', '00:10:00'),
(13, 'D', 'D', 'D', 'D', 'D', 'D', 'D', 24, '08:00:00', '12:00:00', '00:10:00'),
(15, 'H', 'H', 'H', 'H', 'H', 'H', 'H', 15, '07:30:00', '11:00:00', '00:05:00'),
(17, 'F', 'F', 'F', 'F', 'F', 'F', 'F', 24, '09:00:00', '11:00:00', '00:15:00'),
(18, 'A', 'A', 'A', 'A', 'A', 'A', 'A', 15, '08:00:00', '12:00:00', '00:10:00'),
(19, 'G', 'G', 'G', 'G', 'G', 'G', 'G', 15, '08:00:00', '12:00:00', '00:10:00');

-- --------------------------------------------------------

--
-- Struttura della tabella `medical_center_credentials`
--

CREATE TABLE `medical_center_credentials` (
  `id` int(11) NOT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `medical_center_credentials`
--

INSERT INTO `medical_center_credentials` (`id`, `password`) VALUES
(10, 'B'),
(13, 'D'),
(15, 'H'),
(17, 'F'),
(18, 'A'),
(19, 'G');

-- --------------------------------------------------------

--
-- Struttura della tabella `users`
--

CREATE TABLE `users` (
  `CF` varchar(16) NOT NULL,
  `name` varchar(40) NOT NULL,
  `surname` varchar(40) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `mail` varchar(254) NOT NULL,
  `age` int(11) NOT NULL,
  `CAP` varchar(5) NOT NULL,
  `city` varchar(40) NOT NULL,
  `street` varchar(300) NOT NULL,
  `n_cv` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `users`
--

INSERT INTO `users` (`CF`, `name`, `surname`, `phone`, `mail`, `age`, `CAP`, `city`, `street`, `n_cv`) VALUES
('A', 'A', 'A', 'A', 'A@ok', 25, 'A', 'A', 'A', 25),
('B', 'B', 'B', 'B', 'B@ok', 25, 'B', 'B', 'B', 25),
('C', 'C', 'C', 'C', 'C', 25, 'C', 'C', 'C', 15),
('D', 'D', 'D', 'D', 'D@ok', 25, 'D', 'D', 'D', 25),
('E', 'E', 'E', 'E', 'E@ok', 25, 'E', 'E', 'E', 25),
('MPLNTN96S25F158E', 'Antonio', 'Impalà', '3453241991', 'antonioimpala251196@gmail.com', 23, '98045', 'San Pier Niceto', 'Via Dott. Sen. Pietro Pitrone', 134);

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`practical_num`),
  ADD KEY `CF_U` (`CF_U`),
  ADD KEY `ID_M` (`ID_M`),
  ADD KEY `CF_M` (`CF_M`);

--
-- Indici per le tabelle `credentials`
--
ALTER TABLE `credentials`
  ADD PRIMARY KEY (`username`);

--
-- Indici per le tabelle `docs`
--
ALTER TABLE `docs`
  ADD PRIMARY KEY (`CF`);

--
-- Indici per le tabelle `docs_list`
--
ALTER TABLE `docs_list`
  ADD PRIMARY KEY (`CF`,`day`,`id`),
  ADD UNIQUE KEY `CF` (`CF`,`day`),
  ADD KEY `docs_list_ibfk_2` (`id`);

--
-- Indici per le tabelle `medical_centers`
--
ALTER TABLE `medical_centers`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `medical_name` (`medical_name`);

--
-- Indici per le tabelle `medical_center_credentials`
--
ALTER TABLE `medical_center_credentials`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`CF`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `booking`
--
ALTER TABLE `booking`
  MODIFY `practical_num` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT per la tabella `medical_centers`
--
ALTER TABLE `medical_centers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `booking`
--
ALTER TABLE `booking`
  ADD CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`CF_U`) REFERENCES `users` (`CF`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`ID_M`) REFERENCES `medical_centers` (`id`),
  ADD CONSTRAINT `booking_ibfk_3` FOREIGN KEY (`CF_M`) REFERENCES `docs` (`CF`);

--
-- Limiti per la tabella `credentials`
--
ALTER TABLE `credentials`
  ADD CONSTRAINT `credentials_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`CF`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limiti per la tabella `docs_list`
--
ALTER TABLE `docs_list`
  ADD CONSTRAINT `docs_list_ibfk_1` FOREIGN KEY (`CF`) REFERENCES `docs` (`CF`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `docs_list_ibfk_2` FOREIGN KEY (`id`) REFERENCES `medical_centers` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limiti per la tabella `medical_center_credentials`
--
ALTER TABLE `medical_center_credentials`
  ADD CONSTRAINT `medical_center_credentials_ibfk_1` FOREIGN KEY (`id`) REFERENCES `medical_centers` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
