<?php
	session_start();
	include "conection/conexion.php";

?>


<html><head>
<meta charset="UTF-8">
<link rel="stylesheet" type="text/css" href="css/bootstrap.css">
<link rel="stylesheet" type="text/css" href="css/estilos.css">
	<script src="js/jquery-1.8.2.min.js"></script> 
	<script type="text/javascript">
		var comand;
		function borrar(id){
			$.post("borraremp.php",{
                //parametros

                comand: id,

            },
            function(data,status){ 
            alert(data); 
            window.location.reload();              
            });
			
		}
	</script>
<title>Sneakerland | Tus Sneakers hablan por ti</title>
</head>
<body>

<div class="body"></div>

<div class="container-fluid">

	<nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand">SneakerLand Admin</a>
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
			      <li ><a href="#">Sucursales</a></li>
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
	<div class="col-lg-10 col-md-10 col-sm-10 col-lg-offset-1 col-md-offset-1 col-sm-offset-1">
	
		<div style="padding:0" class="gestion">
		<h1 class="text-center" style="padding-top:30px; padding-bottom:30px; opacity: 0.5; margin:0; background-color:#C4C4CC">Gestion Empleado</h1>
		<div class="container-fluid">
			 <h4><label for="psw" class="glyphicon glyphicon-eye-open" > Buscar: </label></h4>
             <input type="text" class="form-control" id="inputdefault" id="psw" size="30px">	
		</div>
			
			<?php conectar();
				

                if (!$conexion) {
				die("Connection failed: " . mysqli_connect_error());
				}

            $sqlselect = "select e.nombre, e.primer_ap, e.segundo_ap, e.curp, concat(d.calle,' no ', d.num),e.id_empleado from empleado e, domicilio d 
			where e.id_domicilio=d.id_domicilio;";
            $result = mysqli_query($conexion, $sqlselect);
			
			echo"<div class=\"table-responsive\">
				<table class=\"table table-hover \">
				<thead>
					<tr>
						<th>Nombre</th>
						<th>Apellido Pat</th>
						<th>Apellido Mat</th>
						<th>CURP</th>
						<th>Domicilio</th>
						<th>ID</th>
						<th>Editar/Detalles</th>
						<th>Eliminar</th>
					</tr>
				</thead>
				<tbody>";
			
				while($row = mysqli_fetch_array($result)){
				echo" 
				  <tr>
					<td>".$row[0]."</td>
					<td>".$row[1]."</td>
					<td>".$row[2]."</td>
					<td>".$row[3]."</td>
					<td>".$row[4]."</td>
					<td>".$row[5]."</td>
					<td>
						<button type=\"button\" class=\"btn btn-default btn-sm\">
						<span class=\"glyphicon glyphicon-plus\"></span>
						</button>
					</td>
					<td>
						<button type=\"button\" class=\"btn btn-default btn-sm btn-danger\"  onclick=\"borrar(".$row[5].")\">
						<span class=\"glyphicon glyphicon-remove-sign\"></span>
						</button>
					</td>
				  </tr>";
				}
	
		   echo"</tbody>
				</table>
			</div>";
			desconectar();
			?>
		
		
		
		</div>
</div>


</div>




</div>




<script src="js/jquery-3.1.1.js"></script>
<script src="js/bootstrap.js"></script>



</body></html>
