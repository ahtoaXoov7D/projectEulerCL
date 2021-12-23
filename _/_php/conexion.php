<?php

	define('DB_SERVER', 'localhost');
	define('DB_USERNAME', 'root');
	define('DB_PASSWORD', '31193');
	define('DB_DATABASE', 'tenis');
   	$conexion;

function conectar()
{	
	global $conexion;
	$conexion = mysqli_connect(DB_SERVER,DB_USERNAME,DB_PASSWORD,DB_DATABASE);

}

function desconectar(){
	global $conexion;
	mysqli_close($conexion);
}


?>
