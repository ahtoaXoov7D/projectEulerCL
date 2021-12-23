<?php 
	session_start();
	include "conection/conexion.php";
	conectar();

        if (!$conexion) {
				die("Connection failed: " . mysqli_connect_error());
        }

	
	$id = $_POST['comand'];
	
	$sql="select d.id_domicilio from domicilio d, empleado e where d.id_domicilio=e.id_domicilio and e.id_empleado=$id";
	$result = mysqli_query($conexion, $sql);


	if (mysqli_num_rows($result) > 0) {
    while($row = mysqli_fetch_assoc($result)) {
        $id_domicilio=$row["id_domicilio"];
    }
} else {
    echo "No se pudo encontrar el domicilio";
}


	$sqlborrar = "delete from domicilio where id_domicilio=$id_domicilio";
	if(mysqli_query($conexion, $sqlborrar)){
		$sqlborrar = "delete from empleado where id_empleado=$id";
		if (mysqli_query($conexion, $sqlborrar)) {
			$sqlborrar = "delete from empleado_status where id_empleado=$id";
			if (mysqli_query($conexion, $sqlborrar)) {
				$sqlborrar = "delete from usuario where empleado_id_empleado=$id";
				if (mysqli_query($conexion, $sqlborrar)) {
					echo "Empleado eliminado exitosamente!";
				}
				else{
					echo "No se pudo eliminar el usuario: ". mysqli_error($conexion);
				}
			}
			else{
				echo "No se pudo eliminar el status: ". mysqli_error($conexion);

			}
		}
		else{
			echo "No se pudo eliminar empleado: " . mysqli_error($conexion);
		}	
	}
	else{
		echo "No se pudo eliminar domicilio: " . mysqli_error($conexion);
	}

		

	desconectar();
	
?>


