-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 03 Jan 2024 pada 15.56
-- Versi server: 10.4.24-MariaDB
-- Versi PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `angkringan`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `angkringan`
--

CREATE TABLE `angkringan` (
  `no_antri` char(5) NOT NULL,
  `nama` varchar(40) NOT NULL,
  `menu` varchar(10) NOT NULL,
  `harga_total` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `angkringan`
--

INSERT INTO `angkringan` (`no_antri`, `nama`, `menu`, `harga_total`) VALUES
('R0001', 'Budi Santoso', 'Soto', '6.000'),
('R0002', 'Ahmad Dani', 'Es Teler', '5.000');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `angkringan`
--
ALTER TABLE `angkringan`
  ADD PRIMARY KEY (`no_antri`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
