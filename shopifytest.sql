-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 16, 2022 at 08:29 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `shopifytest`
--

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`id`, `name`) VALUES
(1, 'Bags'),
(2, 'Shoes'),
(3, 'Caps');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `price` float NOT NULL,
  `description` text NOT NULL,
  `size` varchar(255) NOT NULL,
  `image` varchar(255) NOT NULL,
  `inventoryid` int(11) DEFAULT NULL,
  `status` enum('active','deactive') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`id`, `name`, `price`, `description`, `size`, `image`, `inventoryid`, `status`) VALUES
(1, 'Italian Leather Shoe', 45000, 'Italian leather shoe with friction grip', 'medium', '3432185269.jpg', 2, 'active'),
(2, 'Milano Italian Shoe', 50000, 'Small Size Ehdan Milano Italian shoe', 'small', '6677680752.jpg', 2, 'active'),
(3, 'Blue Italian Leather bag', 25000, 'A blue italian leather bag', 'small', '863963103.jpg', 1, 'active'),
(4, 'Rossy Italian bag', 28000, 'Rossy Italian leather bag', 'large', '2446917327.jpg', 1, 'active'),
(5, 'Glider', 35000, 'Glider Italian Bag', 'medium', '2966043139.jpg', 1, 'active'),
(6, 'Pu Gucci bag', 30000, 'Gucci bag ', 'small', '7210250552.jpg', 1, 'active'),
(7, 'Aurélien Suede', 25000, 'Aurélien Suede Italian shoe', 'medium', '4209014610.jpg', 2, 'active'),
(8, 'Santoni-Italian-Shoes', 40000, 'Santoni-Italian-Shoes for men', 'large', '6123969902.jpg', 2, 'active'),
(9, 'Panama Caps', 15000, 'Panama cap. Made from wool materials and suitable on all outfits', 'medium', '7253211606.jpg', 3, 'active'),
(10, 'US-Italian Cap', 20000, 'Customized US-Italy face cap. complete cotten', 'medium', '3834214212.jpg', 3, 'active'),
(11, 'Black Beret Cap', 10000, 'Black beret cap made of wool', 'medium', '3748371072.jpg', 3, 'active'),
(12, 'Race Horse Cap', 15000, 'Race horse cap for all men', 'small', '1823012495.jpg', 3, 'active');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `inventory`
--
ALTER TABLE `inventory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`),
  ADD KEY `inventoryid` (`inventoryid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `inventory`
--
ALTER TABLE `inventory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `product`
--
ALTER TABLE `product`
  ADD CONSTRAINT `product_ibfk_1` FOREIGN KEY (`inventoryid`) REFERENCES `inventory` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
