<?php
include "conection/conexion.php";
conectar();
?>
<html>

<head>
<meta charset="UTF-8">
<link rel="stylesheet" type="text/css" href="css/bootstrap.css">
<link rel="stylesheet" type="text/css" href="css/estilos.css">
<title>Sneakerland | Tus Sneakers hablan por ti</title>
<style type="text/css">
	.thumb {
	margin: 0px;
	padding: 0px;
	width: 300px;
    border: 1px solid #000;
        }
</style>
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
		<form  method="POST" action="validar_registroproducto.php" enctype="multipart/form-data">

            <div class="form-group text-center">

            <label for=""> Foto del producto</label>
			<div style="width: 300px;position: relative;left: 50%; margin-left: -150px;">
				<div >
			       <output id="list"></output>
				</div>
				<br>
				<input type="hidden" name="MAX_FILE_SIZE" value="1000000">
				<input type="file" id="files" name="files" required="required"/>
			</div>
			<hr>


            <div class="form-group" style="padding-top:30px">
			  <label for=""> Nombre</label>
              <input type="text" style="text-align: center;" placeholder="Ingresa el nombre del producto.." class="form-control" id="nombre_producto" name="nombre_producto">
			</div>

			<div class="form-group text-center " style="padding-top:30px">
			  <label for=""> Descripcion</label>
              <textarea class="form-control" style="text-align: center;" placeholder="Ingresa una descripción del producto.." rows="2" id="comentario" name="comentario"></textarea>
			</div>

			<div class="form-group">
				<label for="sel1">Talla</label>
				<select class="form-control" id="talla" name="talla">
					<?php
					$query_talla = "select * from talla order by id_talla";

					$result_query_talla = mysqli_query($conexion,$query_talla);

					while($Fila = mysqli_fetch_array($result_query_talla))
					{
					?>
					<option  value="<?php echo $Fila["id_talla"]?>"><?php echo $Fila["nombre_talla"] ?></option>
					<?php
					}			
					?>
				</select>
			</div>

			<div class="form-group text-center" style="padding-top:30px">
              <label for=""> Cantidad</label>
              <input type="number" min="0" class="form-control" id="cantidad" name="cantidad">
            </div>



            <div class="form-group text-center" style="padding-top:30px">
              <label for=""> Precio</label>
              <input type="number" min="0" class="form-control" id="precio" name="precio">
            </div>
			
			<div class="form-group">
				<label for="sel1">Seccion</label>
				<select class="form-control" id="seccion" name="seccion">
					<?php
					$query_seccion = "select * from seccion order by id_seccion";

					$result_query_seccion = mysqli_query($conexion,$query_seccion);

					while($Fila = mysqli_fetch_array($result_query_seccion))
					{
					?>
					<option  value="<?php echo $Fila["id_seccion"]?>"><?php echo $Fila["nombre_seccion"] ?></option>
					<?php
					}			
					?>
				</select>
			</div>
			
			<div class="form-group">
				<label for="sel1">Marca</label>
				<select class="form-control" id="marca" name="marca">
					<?php
					$query_marca = "select * from marca order by id_marca";

					$result_query_marca = mysqli_query($conexion,$query_marca);

					while($Fila = mysqli_fetch_array($result_query_marca))
					{
					?>
					<option  value="<?php echo $Fila["id_marca"]?>"><?php echo $Fila["nombre_marca"] ?></option>
					<?php
					}			
					?>
				</select>
			</div>

			<div class="form-group">
				<label for="sel1">Tipo</label>
				<select class="form-control" id="tipo" name="tipo">
					<?php
					$query_tipo = "select * from tipo order by id_tipo";

					$result_query_tipo = mysqli_query($conexion,$query_tipo);

					while($Fila = mysqli_fetch_array($result_query_tipo))
					{
					?>
					<option  value="<?php echo $Fila["id_tipo"]?>"><?php echo $Fila["nombre"] ?></option>
					<?php
					}	

					desconectar();		
					?>
				</select>
			</div>
			</div>
            <button type="submit" class="btn btn-danger my-btn btn-block"><span class="glyphicon glyphicon-off"></span> Registro</button>
        </form>
        </div>
		</div>
	
	</div>
</div>
	


</div>



<script src="js/jquery-3.1.1.js"></script>
<script src="js/bootstrap.js"></script>

<script>
	function archivo(evt) {
		var files = evt.target.files; // FileList object
		
		// Obtenemos la imagen del campo "file".
		for (var i = 0, f; f = files[i]; i++) 
		{
			//Solo admitimos imágenes.
			if (!f.type.match('image.*')) {
				continue;
		}
		
		var reader = new FileReader();
		
    	reader.onload = (function(theFile) {
		return function(e) {
		  // Insertamos la imagen
		 document.getElementById("list").innerHTML = ['<img class="thumb" src="', e.target.result,'" title="', escape(theFile.name), '"/>'].join('');
	};
	})(f);
		
	reader.readAsDataURL(f);
	}
  }
		
  document.getElementById('files').addEventListener('change', archivo, false);
</script>
<script>
    $(function () {
        $('#tooltip1').tooltip();
    });
</script>
</body>
</html>
