<?php 
	session_start();
	include "conection/conexion.php";
	conectar();

        if (!$conexion) {
				die("Connection failed: " . mysqli_connect_error());
        }

	$sku = $_POST['comand'];
	
	$sqlborrar = "delete from producto where sku=$sku";
	if(mysqli_query($conexion, $sqlborrar)){
		$sqlborrar = "delete from compra where producto_sku=$sku";
		if (mysqli_query($conexion, $sqlborrar)) {
			$sqlborrar = "delete from talla_producto where producto_sku=$sku";
			if (mysqli_query($conexion, $sqlborrar)) {
				$sqlborrar = "delete from existencia where id_producto=$sku";
				if (mysqli_query($conexion, $sqlborrar)) {
					echo "Producto eliminado exitosamente!";
				}
				else{
					echo "No se pudo eliminar la existencia: ". mysqli_error($conexion);
				}
			}
			else{
				echo "No se pudo eliminar la talla: ".mysqli_error($conexion);
			}
		}
		else{
			echo "No se pudo eliminar la compra: ". mysqli_error($conexion);
		}
	}
	else{
		echo "No se pudo eliminar el producto; ".mysqli_error($conexion);
	}

	desconectar();
		
?>