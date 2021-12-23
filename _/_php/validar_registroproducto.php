<?php
include "conection/conexion.php";
conectar();

/*error_reporting(E_ALL);
ini_set('display_errors',1);*/

$nombre = $_POST['nombre_producto'];
$comentario = $_POST['comentario'];
$talla = $_POST['talla'];
$cantidad = $_POST['cantidad'];
$precio = $_POST['precio'];
$seccion = $_POST['seccion'];
$marca = $_POST['marca'];
$tipo = $_POST['tipo'];

$mimetypes = array("image/jpeg", "image/pjpeg", "image/gif", "image/png");
	
// Variables de la foto
$name = $_FILES["files"]["name"];
$type = $_FILES["files"]["type"];
$tmp_name = $_FILES["files"]["tmp_name"];
$size = $_FILES["files"]["size"];

if(!in_array($type, $mimetypes))
{
	?>
	<html>
	<head>
	<meta charset="UTF-8">
	<link rel="stylesheet" type="text/css" href="css/bootstrap.css">
	<link rel="stylesheet" type="text/css" href="css/estilos.css">
	<title>Sneakerland | Tus Sneakers hablan por ti</title>
	</head>
	<body>
	<div class="body"></div>
	<div class="container-fluid">
	<nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">SneakerLand Admin</a>
    </div>
    <ul class="nav navbar-nav">
      <li class="active"><a href="home_administrador.php">Home</a></li>
        <li>
        <form class="navbar-form" style="border: 0">
          <div class="dropdown">
          <button class="btn btn-default dropdown-toggle" type="button" data-toggle="dropdown">Registrar
          <span class="caret"></span>
          </button>
          <ul class="dropdown-menu">
            <li><a href="registroempleado.php">Empleados</a></li>
            <li class="divider"><li>
            <li><a href="registroproducto.php">Productos</a></li>
            <li class="divider"><li>
            <li ><a href="registrosucursal.php">Sucursales</a></li>
          </ul>
        </div>
      </form>
     </li>
     <li>
        <form class="navbar-form" style="border: 0">
          <div class="dropdown">
          <button class="btn btn-default dropdown-toggle" type="button" data-toggle="dropdown">Gestionar
          <span class="caret"></span>
          </button>
          <ul class="dropdown-menu">
            <li><a href="gestionempleado.php">Empleados</a></li>
            <li class="divider"><li>
            <li><a href="gestionproducto.php">Productos</a></li>
            <li class="divider"><li>
            <li ><a href="registrosucursal.php">Sucursales</a></li>
          </ul>
        </div>
      </form>
     </li>
     <li>
        <form class="navbar-form" style="border: 0">
          <div class="dropdown">
          <button class="btn btn-default dropdown-toggle" type="button" data-toggle="dropdown">Consultar
          <span class="caret"></span>
          </button>
          <ul class="dropdown-menu">
            <li><a href="consultarempleado.php">Empleados</a></li>
            <li class="divider"><li>
            <li><a href="consultarproducto.php">Productos</a></li>
            <li class="divider"><li>
            <li ><a href="consultarsucursal.php">Sucursales</a></li>
          </ul>
        </div>
      </form>
     </li>



      




    </ul>
  </div>
</nav>

	<div class="row">
		<div class="col-lg-8 col-md-8 col-sm-8 col-lg-offset-2 col-md-offset-2 col-sm-offset-2">
			<div class="formulario" style="padding:0">
			<h1 class="text-center" style="padding-top:30px; padding-bottom:30px; opacity: 0.5; margin:0; background-color:#C4C4CC">Registro Producto</h1>
			<div style="padding:40px 50px">				
							<br>
							<p>El archivo no es una imagen ó pesa más de 1MB, debes cambiar el tamaño del archivo.</p>
							<br>
							<a href="registroproducto.php">Continuar</a>					
	        </div>
			</div>		
		</div>
	</div>
	</div>
	<script src="js/jquery-3.1.1.js"></script>
	<script src="js/bootstrap.js"></script>
	</body></html>
<?php
}
else
{
?>

<html>
<head>
<meta charset="UTF-8">
<link rel="stylesheet" type="text/css" href="css/bootstrap.css">
<link rel="stylesheet" type="text/css" href="css/estilos.css">
<title>Sneakerland | Tus Sneakers hablan por ti</title>
</head>

<body>

<div class="body"></div>

<div class="container-fluid">


<nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">SneakerLand Admin</a>
    </div>
    <ul class="nav navbar-nav">
      <li class="active"><a href="home_administrador.php">Home</a></li>
        <li>
        <form class="navbar-form" style="border: 0">
          <div class="dropdown">
          <button class="btn btn-default dropdown-toggle" type="button" data-toggle="dropdown">Registrar
          <span class="caret"></span>
          </button>
          <ul class="dropdown-menu">
            <li><a href="registroempleado.php">Empleados</a></li>
            <li class="divider"><li>
            <li><a href="registroproducto.php">Productos</a></li>
            <li class="divider"><li>
            <li ><a href="registrosucursal.php">Sucursales</a></li>
          </ul>
        </div>
      </form>
     </li>
     <li>
        <form class="navbar-form" style="border: 0">
          <div class="dropdown">
          <button class="btn btn-default dropdown-toggle" type="button" data-toggle="dropdown">Gestionar
          <span class="caret"></span>
          </button>
          <ul class="dropdown-menu">
            <li><a href="gestionempleado.php">Empleados</a></li>
            <li class="divider"><li>
            <li><a href="gestionproducto.php">Productos</a></li>
            <li class="divider"><li>
            <li ><a href="registrosucursal.php">Sucursales</a></li>
          </ul>
        </div>
      </form>
     </li>
     <li>
        <form class="navbar-form" style="border: 0">
          <div class="dropdown">
          <button class="btn btn-default dropdown-toggle" type="button" data-toggle="dropdown">Consultar
          <span class="caret"></span>
          </button>
          <ul class="dropdown-menu">
            <li><a href="consultarempleado.php">Empleados</a></li>
            <li class="divider"><li>
            <li><a href="consultarproducto.php">Productos</a></li>
            <li class="divider"><li>
            <li ><a href="consultarsucursal.php">Sucursales</a></li>
          </ul>
        </div>
      </form>
     </li>



      




    </ul>
  </div>
</nav>

<div class="row">
	<div class="col-lg-8 col-md-8 col-sm-8 col-lg-offset-2 col-md-offset-2 col-sm-offset-2">
		<div class="formulario" style="padding:0">
		<h1 class="text-center" style="padding-top:30px; padding-bottom:30px; opacity: 0.5; margin:0; background-color:#C4C4CC">Registro Producto</h1>
		<div style="padding:40px 50px">
			<?php
				/*
				echo $nombre;
				echo "<br>";
				echo $comentario;
				echo "<br>";
				echo $precio;
				echo "<br>";
				echo $seccion;
				echo "<br>";
				echo $marca;
				echo "<br>";
				echo $tipo;
				*/

				

				$registro_producto ="insert into producto(nombre_producto, descripcion, precio,seccion_idseccion,tipo_idtipo,marca_idmarca) values('$nombre','$comentario','$precio','$seccion','$marca','$tipo')";

				$result_registro_producto = mysqli_query($conexion,$registro_producto);


				$max_producto = "select max(sku) from producto";

				$result_max_producto = mysqli_query($conexion, $max_producto);

				$result_max_producto_array = mysqli_fetch_array($result_max_producto);
			
				$max_producto = $result_max_producto_array[0];


				//Guardar imagen en el servidor
				/******************************************/

				$archivo = "images/productos/".$max_producto.".jpg";
				


				$result_guardar_imagen = move_uploaded_file($tmp_name, $archivo);

				if($result_guardar_imagen)
				{
					echo "<br>Foto del producto guardada<br>";
				}
				else
				{
					echo "<br>No lo cambio<br>";
					echo $archivo;
				}

				/******************************************/


				$registro_talla = "insert into talla_producto(talla_num_talla, producto_sku, cantidad) 
				values('$talla','$max_producto','$cantidad')";

				$result_registro_talla = mysqli_query($conexion, $registro_talla);


				if($result_registro_producto)
				{
					if($result_registro_talla)
					{
				?>
					<br>
					<p>Producto registrado exitosamente.</p>
					<br>
					<a href="registroproducto.php">Continuar</a>
				<?php
					}
					else
					{
					?>
						<br>
						<p>Hubo un error al registrar el producto.</p>
						<br>
						<a href="registroproducto.php">Continuar</a>
					<?php	
					}
				}
				else
				{
				?>
					<br>
					<p>Hubo un error al registrar el producto.</p>
					<br>
					<a href="registroproducto.php">Continuar</a>
				<?php
				}

        desconectar();
				?>
        </div>
		</div>
	
	</div>
</div>
	


</div>



<script src="js/jquery-3.1.1.js"></script>
<script src="js/bootstrap.js"></script>


</body></html>
<?php
}
?>