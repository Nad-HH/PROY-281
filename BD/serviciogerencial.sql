-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-04-2023 a las 23:11:56
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `serviciogerencial`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ambiente`
--

CREATE TABLE `ambiente` (
  `id_ambiente` int(30) NOT NULL,
  `tipo_ambiente` varchar(40) DEFAULT NULL,
  `capacidadmax` int(40) DEFAULT NULL,
  `ubicacion` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ambiente`
--

INSERT INTO `ambiente` (`id_ambiente`, `tipo_ambiente`, `capacidadmax`, `ubicacion`) VALUES
(1, 'laboratorio', 80, 'piso 3 - a2'),
(2, 'aula', 300, 'piso1 - a2'),
(4, 'laboratorio', 100, 'piso2 a4');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `certificado`
--

CREATE TABLE `certificado` (
  `id_certificado` int(30) NOT NULL,
  `descripcion` varchar(300) DEFAULT NULL,
  `fecha` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `crea_lista`
--

CREATE TABLE `crea_lista` (
  `id_evento` int(30) NOT NULL,
  `id_inscripcion` int(40) NOT NULL,
  `id_lista` int(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `devolucion`
--

CREATE TABLE `devolucion` (
  `id_devolucion` int(30) NOT NULL,
  `id_control` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dirige_even`
--

CREATE TABLE `dirige_even` (
  `id_expositor` int(30) NOT NULL,
  `id_evento` int(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `edificio`
--

CREATE TABLE `edificio` (
  `id_edificio` int(30) NOT NULL,
  `nro_pisos` int(40) DEFAULT NULL,
  `nro_ambientes` int(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `emision_cert`
--

CREATE TABLE `emision_cert` (
  `id_certificado` int(30) NOT NULL,
  `id_lista` int(40) NOT NULL,
  `id_evento` int(40) NOT NULL,
  `id_control` int(40) NOT NULL,
  `id_participante` int(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `equipo_elec`
--

CREATE TABLE `equipo_elec` (
  `id_equipoelec` int(30) NOT NULL,
  `tipo` varchar(40) DEFAULT NULL,
  `descripcion` varchar(40) DEFAULT NULL,
  `id_ambiente` int(40) DEFAULT NULL,
  `catidad` int(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `equipo_elec`
--

INSERT INTO `equipo_elec` (`id_equipoelec`, `tipo`, `descripcion`, `id_ambiente`, `catidad`) VALUES
(1, '1', 'laptops', 0, 13),
(6, 'laptops', 'son nuevas', 1, 30),
(7, 'laptops', 'son nuevas', 2, 30);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `evento_academico`
--

CREATE TABLE `evento_academico` (
  `id_evento` int(30) NOT NULL,
  `tipo` varchar(100) DEFAULT NULL,
  `portada_even` varchar(200) DEFAULT NULL,
  `capacidadmax` int(10) DEFAULT NULL,
  `precio` float DEFAULT NULL,
  `titulo` varchar(200) DEFAULT NULL,
  `descripcion` varchar(500) DEFAULT NULL,
  `area` varchar(80) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `id_control` int(30) DEFAULT NULL,
  `id_administrador` int(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `evento_academico`
--

INSERT INTO `evento_academico` (`id_evento`, `tipo`, `portada_even`, `capacidadmax`, `precio`, `titulo`, `descripcion`, `area`, `fecha`, `id_control`, `id_administrador`) VALUES
(16, 's', '2023194744 eve4.jpg', 6, 7, 'a', 's', 's', '2023-05-05', NULL, NULL),
(17, 'mesa redonda', '2023194722 orador-que-da-charla-en-el-evento-del-negocio-98317508.jpg', 234, 45, 'titulo2', 'dasda', 'informatica', '2023-05-03', NULL, NULL),
(18, 'mesa redonda', '2023192413 eve2.jpg', 23, 0, 'titulo2', 'wer', 'wew', '2023-04-07', 16, NULL);

--
-- Disparadores `evento_academico`
--
DELIMITER $$
CREATE TRIGGER `eliminar_evento` AFTER DELETE ON `evento_academico` FOR EACH ROW INSERT INTO `evento_eliminado` (id_evento_eliminado, id_evento,tipo,portada_even,capacidadmax,precio,titulo,descripcion,area,fecha,id_control,id_administrador) 
VALUES (NULL,OLD.id_evento, OLD.tipo, OLD.portada_even, OLD.capacidadmax, OLD.precio, OLD.titulo, OLD.descripcion, OLD.area, OLD.fecha, OLD.id_control, OLD.id_administrador)
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `evento_eliminado`
--

CREATE TABLE `evento_eliminado` (
  `id_evento_eliminado` int(30) NOT NULL,
  `id_evento` int(30) DEFAULT NULL,
  `tipo` varchar(100) DEFAULT NULL,
  `portada_even` varchar(200) DEFAULT NULL,
  `capacidadmax` int(10) DEFAULT NULL,
  `precio` float DEFAULT NULL,
  `titulo` varchar(200) DEFAULT NULL,
  `descripcion` varchar(500) DEFAULT NULL,
  `area` varchar(80) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `id_control` int(30) DEFAULT NULL,
  `id_administrador` int(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `evento_eliminado`
--

INSERT INTO `evento_eliminado` (`id_evento_eliminado`, `id_evento`, `tipo`, `portada_even`, `capacidadmax`, `precio`, `titulo`, `descripcion`, `area`, `fecha`, `id_control`, `id_administrador`) VALUES
(1, 13, 'a', '2023171544 ima3.jpg', 6, 6, 'a', 'a', 'g', '2023-03-02', NULL, NULL),
(2, 13, 'a', '2023171544 ima3.jpg', 6, 6, 'a', 'a', 'g', '2023-03-02', NULL, NULL),
(3, 12, 'a', '2023171331 logo.png', 2, 3, 'a', 'a', '3', '2023-05-04', NULL, NULL),
(4, 12, 'a', '2023171331 logo.png', 2, 3, 'a', 'a', '3', '2023-05-04', NULL, NULL),
(5, 11, 'convencion', '2023123612 ima1.jpg', 34, 45, 'titulo2', 'SDSDF', 'informatica', '2023-06-03', NULL, NULL),
(6, 11, 'convencion', '2023123612 ima1.jpg', 34, 45, 'titulo2', 'SDSDF', 'informatica', '2023-06-03', NULL, NULL),
(7, 9, 'convencion', '2023234714 eve1.jpg', 150, 34, 'titulo1', 'descripcion1', 'informatica', '2023-06-03', NULL, NULL),
(8, 9, 'convencion', '2023234714 eve1.jpg', 150, 34, 'titulo1', 'descripcion1', 'informatica', '2023-06-03', NULL, NULL),
(9, 10, 'mesa redonda', '2023234759 eve2.jpg', 150, 35, 'titulo2', 'descripcion2', 'informatica', '2023-03-04', NULL, NULL),
(10, 10, 'mesa redonda', '2023234759 eve2.jpg', 150, 35, 'titulo2', 'descripcion2', 'informatica', '2023-03-04', NULL, NULL),
(11, 14, 'as', '2023194917 eve3.jpg', 0, 0, 'as hola', 'ass', 'as', '2023-03-04', NULL, NULL),
(12, 14, 'as', '2023194917 eve3.jpg', 0, 0, 'as hola', 'ass', 'as', '2023-03-04', NULL, NULL),
(13, 15, 'sddsd', '2023195021 ima2.jpg', 67, 3, 'titulo nuevo', 'dfs', 'fsf', '2023-03-04', NULL, NULL),
(14, 15, 'sddsd', '2023195021 ima2.jpg', 67, 3, 'titulo nuevo', 'dfs', 'fsf', '2023-03-04', NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gestiona_hora`
--

CREATE TABLE `gestiona_hora` (
  `id_gestiona_hora` int(30) NOT NULL,
  `fecha` date DEFAULT NULL,
  `hora_ini` time DEFAULT NULL,
  `hora_fin` time DEFAULT NULL,
  `id_evento` int(30) DEFAULT NULL,
  `id_control` int(30) DEFAULT NULL,
  `id_ambiente` int(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `gestiona_hora`
--

INSERT INTO `gestiona_hora` (`id_gestiona_hora`, `fecha`, `hora_ini`, `hora_fin`, `id_evento`, `id_control`, `id_ambiente`) VALUES
(1, '2023-05-04', '13:22:00', '16:22:00', 16, 16, 1),
(3, '2023-04-02', '14:40:00', '15:41:00', 18, 16, 1),
(4, '2023-08-02', '14:11:00', '16:11:00', 17, 16, 2),
(5, '2023-08-07', '16:11:00', '18:00:00', 17, 16, 1),
(6, '2023-05-07', '15:19:00', '17:19:00', 16, 14, 2),
(7, '2023-04-03', '23:46:00', '01:46:00', 18, 17, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gestiona_info`
--

CREATE TABLE `gestiona_info` (
  `id_administrador` int(30) NOT NULL,
  `id_informacion` int(40) NOT NULL,
  `id_redsocial` int(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `horario`
--

CREATE TABLE `horario` (
  `id_horario` int(30) NOT NULL,
  `turno` varchar(40) DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `fecha` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `informacionweb`
--

CREATE TABLE `informacionweb` (
  `id_info` int(30) NOT NULL,
  `direccion` varchar(150) DEFAULT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  `mision` varchar(300) DEFAULT NULL,
  `vision` varchar(300) DEFAULT NULL,
  `objetivo` varchar(300) DEFAULT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `logotipo` varchar(200) DEFAULT NULL,
  `portada1` varchar(200) DEFAULT NULL,
  `portada2` varchar(200) DEFAULT NULL,
  `portada3` varchar(200) DEFAULT NULL,
  `portada4` varchar(200) DEFAULT NULL,
  `portada5` varchar(200) DEFAULT NULL,
  `celular` int(20) DEFAULT NULL,
  `correo_el` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `informacionweb`
--

INSERT INTO `informacionweb` (`id_info`, `direccion`, `descripcion`, `mision`, `vision`, `objetivo`, `nombre`, `logotipo`, `portada1`, `portada2`, `portada3`, `portada4`, `portada5`, `celular`, `correo_el`) VALUES
(1, 'Av. Villazón N° 1995, Plaza del Bicentenario - Zona Central.', 'Bienvenidos a nuestra agencia de eventos académicos, somos una empresa dedicada a la planificación y organización de eventos educativos', 'Organizar eventos académicos de calidad, promoviendo el intercambio de conocimientos entre profesionales y estudiantes, fomentando el desarrollo de habilidades y competencias en la comunidad educativa.', 'Ser reconocidos como la empresa líder en la organización de eventos académicos a nivel nacional, con una oferta diversificada y de calidad, que contribuya al fortalecimiento de la educación y la investigación en el país.', 'Ofrecer una variedad de eventos académicos que satisfagan las necesidades de los distintos perfiles de participantes, tanto profesionales como estudiantes', 'HOLA MUNDO', '2023233439 logo.png', '2023170617 ima3.jpg', '2023140627 ima2.jpg', '2023225748 mision.jpg', 'portada4.jpg', 'portada5.jpg', 60547212, 'ejemplo_de_correo2_@gmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inscripcion`
--

CREATE TABLE `inscripcion` (
  `id_inscripcion` int(30) NOT NULL,
  `numero_tarjeta` varchar(40) DEFAULT NULL,
  `exp` varchar(40) DEFAULT NULL,
  `CVN` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inscripcion_reserva`
--

CREATE TABLE `inscripcion_reserva` (
  `id_insc_resv` int(30) NOT NULL,
  `id_reserva` int(30) DEFAULT NULL,
  `codigo_control` varchar(40) DEFAULT NULL,
  `hora_conf` time DEFAULT NULL,
  `fecha_conf` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inscripcion_sin_reserva`
--

CREATE TABLE `inscripcion_sin_reserva` (
  `id_insc_sin` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `lista_asistencia`
--

CREATE TABLE `lista_asistencia` (
  `id_lista` int(30) NOT NULL,
  `id_control` int(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `planifica`
--

CREATE TABLE `planifica` (
  `id_expositor` int(30) NOT NULL,
  `id_evento` int(40) NOT NULL,
  `id_repositorio` int(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `realiza_en`
--

CREATE TABLE `realiza_en` (
  `id_evento` int(30) DEFAULT NULL,
  `id_ambiente` int(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `realiza_en`
--

INSERT INTO `realiza_en` (`id_evento`, `id_ambiente`) VALUES
(16, 1),
(17, 2),
(16, 1),
(16, 2),
(16, 1),
(18, 1),
(18, 1),
(17, 2),
(17, 1),
(16, 2),
(18, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `realiza_reserva`
--

CREATE TABLE `realiza_reserva` (
  `id_reserva` int(30) NOT NULL,
  `id_participante` int(40) NOT NULL,
  `hora_reserva` time DEFAULT NULL,
  `fecha_reserva` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `red_social`
--

CREATE TABLE `red_social` (
  `id_red` int(30) NOT NULL,
  `tipo` varchar(40) DEFAULT NULL,
  `nombre` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `repositorio`
--

CREATE TABLE `repositorio` (
  `id_repositorio` int(30) NOT NULL,
  `titulo_material` varchar(40) DEFAULT NULL,
  `tipo_documento` varchar(40) DEFAULT NULL,
  `documento1` longblob DEFAULT NULL,
  `documento2` longblob DEFAULT NULL,
  `documento3` longblob DEFAULT NULL,
  `documento4` longblob DEFAULT NULL,
  `documento5` longblob DEFAULT NULL,
  `link` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reserva`
--

CREATE TABLE `reserva` (
  `id_reserva` int(30) NOT NULL,
  `codigo_control` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rudimentario`
--

CREATE TABLE `rudimentario` (
  `id_rudi` int(30) NOT NULL,
  `tipo` varchar(40) DEFAULT NULL,
  `descripcion` varchar(40) DEFAULT NULL,
  `id_ambiente` varchar(40) DEFAULT NULL,
  `catidad` int(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `rudimentario`
--

INSERT INTO `rudimentario` (`id_rudi`, `tipo`, `descripcion`, `id_ambiente`, `catidad`) VALUES
(7, 'e', 're', '2', 4),
(8, 'sillas', 'color negro ', '1', 13),
(9, 'mesas', 'color negro ', '1', 5),
(11, 'mesas', 'son nuevas', '4', 20);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `se_inscribe`
--

CREATE TABLE `se_inscribe` (
  `id_participante` int(30) NOT NULL,
  `id_reserva` int(40) NOT NULL,
  `hora_inscripcion` time DEFAULT NULL,
  `fecha_inscripcion` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `solicita`
--

CREATE TABLE `solicita` (
  `id_participante` int(30) NOT NULL,
  `id_devolucion` int(40) NOT NULL,
  `id_evento` int(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(30) NOT NULL,
  `tipo` varchar(20) DEFAULT NULL,
  `ci` int(20) DEFAULT NULL,
  `contrasena` varchar(20) DEFAULT NULL,
  `correo_elec` varchar(50) DEFAULT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido_p` varchar(20) DEFAULT NULL,
  `apellido_m` varchar(20) DEFAULT NULL,
  `fecha_naci` date DEFAULT NULL,
  `usuario` varchar(20) DEFAULT NULL,
  `celular` int(10) DEFAULT NULL,
  `id_administrador` varchar(30) DEFAULT NULL,
  `portada` varchar(150) DEFAULT NULL,
  `perfil` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `tipo`, `ci`, `contrasena`, `correo_elec`, `nombre`, `apellido_p`, `apellido_m`, `fecha_naci`, `usuario`, `celular`, `id_administrador`, `portada`, `perfil`) VALUES
(1, 'admin', 9957898, '123', 'admin@gmail.com', 'Nadya', 'Huanca', 'Huaylliri', '2000-07-15', 'admin', 75873361, NULL, NULL, NULL),
(2, 'control', 342342, 'aaa', 'aaaa@gmail.com', 'Selena', 'Tarqui', 'Machaca', NULL, 'control1', 4242324, NULL, NULL, NULL),
(3, 'expositor', 345353, 'bbb', 'expo1@gmail.com', 'David', 'Romero', 'Diaz', NULL, 'expo1', 23423435, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `u_administrativo`
--

CREATE TABLE `u_administrativo` (
  `id_administrador` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `u_administrativo`
--

INSERT INTO `u_administrativo` (`id_administrador`) VALUES
(1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `u_control`
--

CREATE TABLE `u_control` (
  `id_control` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `u_expositor`
--

CREATE TABLE `u_expositor` (
  `id_expositor` int(30) NOT NULL,
  `pdf` longblob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `u_participante`
--

CREATE TABLE `u_participante` (
  `id_participante` int(30) NOT NULL,
  `razon_social` varchar(20) DEFAULT NULL,
  `nit` int(20) DEFAULT NULL,
  `tarjeta` int(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `ambiente`
--
ALTER TABLE `ambiente`
  ADD PRIMARY KEY (`id_ambiente`);

--
-- Indices de la tabla `certificado`
--
ALTER TABLE `certificado`
  ADD PRIMARY KEY (`id_certificado`);

--
-- Indices de la tabla `crea_lista`
--
ALTER TABLE `crea_lista`
  ADD PRIMARY KEY (`id_evento`,`id_inscripcion`,`id_lista`);

--
-- Indices de la tabla `devolucion`
--
ALTER TABLE `devolucion`
  ADD PRIMARY KEY (`id_devolucion`);

--
-- Indices de la tabla `dirige_even`
--
ALTER TABLE `dirige_even`
  ADD PRIMARY KEY (`id_expositor`,`id_evento`);

--
-- Indices de la tabla `edificio`
--
ALTER TABLE `edificio`
  ADD PRIMARY KEY (`id_edificio`);

--
-- Indices de la tabla `emision_cert`
--
ALTER TABLE `emision_cert`
  ADD PRIMARY KEY (`id_certificado`,`id_evento`,`id_lista`,`id_control`,`id_participante`);

--
-- Indices de la tabla `equipo_elec`
--
ALTER TABLE `equipo_elec`
  ADD PRIMARY KEY (`id_equipoelec`);

--
-- Indices de la tabla `evento_academico`
--
ALTER TABLE `evento_academico`
  ADD PRIMARY KEY (`id_evento`);

--
-- Indices de la tabla `evento_eliminado`
--
ALTER TABLE `evento_eliminado`
  ADD PRIMARY KEY (`id_evento_eliminado`);

--
-- Indices de la tabla `gestiona_hora`
--
ALTER TABLE `gestiona_hora`
  ADD PRIMARY KEY (`id_gestiona_hora`);

--
-- Indices de la tabla `gestiona_info`
--
ALTER TABLE `gestiona_info`
  ADD PRIMARY KEY (`id_administrador`,`id_informacion`,`id_redsocial`);

--
-- Indices de la tabla `horario`
--
ALTER TABLE `horario`
  ADD PRIMARY KEY (`id_horario`);

--
-- Indices de la tabla `informacionweb`
--
ALTER TABLE `informacionweb`
  ADD PRIMARY KEY (`id_info`);

--
-- Indices de la tabla `inscripcion`
--
ALTER TABLE `inscripcion`
  ADD PRIMARY KEY (`id_inscripcion`);

--
-- Indices de la tabla `inscripcion_reserva`
--
ALTER TABLE `inscripcion_reserva`
  ADD PRIMARY KEY (`id_insc_resv`);

--
-- Indices de la tabla `inscripcion_sin_reserva`
--
ALTER TABLE `inscripcion_sin_reserva`
  ADD PRIMARY KEY (`id_insc_sin`);

--
-- Indices de la tabla `lista_asistencia`
--
ALTER TABLE `lista_asistencia`
  ADD PRIMARY KEY (`id_lista`);

--
-- Indices de la tabla `planifica`
--
ALTER TABLE `planifica`
  ADD PRIMARY KEY (`id_expositor`,`id_evento`,`id_repositorio`);

--
-- Indices de la tabla `realiza_reserva`
--
ALTER TABLE `realiza_reserva`
  ADD PRIMARY KEY (`id_reserva`,`id_participante`);

--
-- Indices de la tabla `red_social`
--
ALTER TABLE `red_social`
  ADD PRIMARY KEY (`id_red`);

--
-- Indices de la tabla `repositorio`
--
ALTER TABLE `repositorio`
  ADD PRIMARY KEY (`id_repositorio`);

--
-- Indices de la tabla `reserva`
--
ALTER TABLE `reserva`
  ADD PRIMARY KEY (`id_reserva`);

--
-- Indices de la tabla `rudimentario`
--
ALTER TABLE `rudimentario`
  ADD PRIMARY KEY (`id_rudi`);

--
-- Indices de la tabla `se_inscribe`
--
ALTER TABLE `se_inscribe`
  ADD PRIMARY KEY (`id_participante`,`id_reserva`);

--
-- Indices de la tabla `solicita`
--
ALTER TABLE `solicita`
  ADD PRIMARY KEY (`id_participante`,`id_devolucion`,`id_evento`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`);

--
-- Indices de la tabla `u_administrativo`
--
ALTER TABLE `u_administrativo`
  ADD PRIMARY KEY (`id_administrador`);

--
-- Indices de la tabla `u_control`
--
ALTER TABLE `u_control`
  ADD PRIMARY KEY (`id_control`);

--
-- Indices de la tabla `u_expositor`
--
ALTER TABLE `u_expositor`
  ADD PRIMARY KEY (`id_expositor`);

--
-- Indices de la tabla `u_participante`
--
ALTER TABLE `u_participante`
  ADD PRIMARY KEY (`id_participante`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `ambiente`
--
ALTER TABLE `ambiente`
  MODIFY `id_ambiente` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `certificado`
--
ALTER TABLE `certificado`
  MODIFY `id_certificado` int(30) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `devolucion`
--
ALTER TABLE `devolucion`
  MODIFY `id_devolucion` int(30) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `edificio`
--
ALTER TABLE `edificio`
  MODIFY `id_edificio` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `equipo_elec`
--
ALTER TABLE `equipo_elec`
  MODIFY `id_equipoelec` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `evento_academico`
--
ALTER TABLE `evento_academico`
  MODIFY `id_evento` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `evento_eliminado`
--
ALTER TABLE `evento_eliminado`
  MODIFY `id_evento_eliminado` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `gestiona_hora`
--
ALTER TABLE `gestiona_hora`
  MODIFY `id_gestiona_hora` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `horario`
--
ALTER TABLE `horario`
  MODIFY `id_horario` int(30) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `informacionweb`
--
ALTER TABLE `informacionweb`
  MODIFY `id_info` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `inscripcion`
--
ALTER TABLE `inscripcion`
  MODIFY `id_inscripcion` int(30) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `inscripcion_reserva`
--
ALTER TABLE `inscripcion_reserva`
  MODIFY `id_insc_resv` int(30) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `inscripcion_sin_reserva`
--
ALTER TABLE `inscripcion_sin_reserva`
  MODIFY `id_insc_sin` int(30) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `lista_asistencia`
--
ALTER TABLE `lista_asistencia`
  MODIFY `id_lista` int(30) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `red_social`
--
ALTER TABLE `red_social`
  MODIFY `id_red` int(30) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `repositorio`
--
ALTER TABLE `repositorio`
  MODIFY `id_repositorio` int(30) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `reserva`
--
ALTER TABLE `reserva`
  MODIFY `id_reserva` int(30) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `rudimentario`
--
ALTER TABLE `rudimentario`
  MODIFY `id_rudi` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `u_administrativo`
--
ALTER TABLE `u_administrativo`
  MODIFY `id_administrador` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `u_control`
--
ALTER TABLE `u_control`
  MODIFY `id_control` int(30) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `u_expositor`
--
ALTER TABLE `u_expositor`
  MODIFY `id_expositor` int(30) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `u_participante`
--
ALTER TABLE `u_participante`
  MODIFY `id_participante` int(30) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
