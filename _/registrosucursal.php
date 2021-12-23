<!DOCTYPE html>
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
			      <li ><a href="consultarsucursal">Sucursales</a></li>
   				</ul>
  			</div>
    	</form>
     </li>

    </ul>
</nav>

<div class="row">
  <div class="col-lg-6 col-md-6 col-sm-6 col-lg-offset-3 col-md-6-offset-3 col-sm-offset-3">
    <div class="formulario" style="padding:0">

     <h1 class="text-center" style="padding-top:30px; padding-bottom:30px; opacity: 0.5; margin:0; background-color:#C4C4CC">Registrar Sucursal</h1>

     <div style="padding:40px 50px">

      <div class="form-group text-center">
          <label for="nombre"> Nombre Sucursal</label>
          <input type="text" class="form-control" id="nombre" name="nombre" required value="<?php echo $nombre; ?>">
      </div>

      <div class="form-group text-center" >
        <label for="calle"> Domicilio</label><br/>
        <label for="calle">Calle</label>
        <input type="text" class="form-control form-inline" name="calle" id="calle" required value="<?php echo $calle; ?>">
      </div> 

      <div class="row text-center">    
        <div class="col-lg-6">
        <label for="numero">Numero</label>  
        <input type="text" class="form-control form-inline" name="numero"  id="numero" required value="<?php echo $numero; ?>">
        </div>  

        <!--- Aquí se van a traer los cp desde la base de datos -->
      <div class="col-lg-6">
        <div class="form-group  text-center">
        <label for="cp">Cp</label>
        <select class="form-control" id="cp" name="cp" required>
            <!-- Traer desde la base de datos -->
        </select>
        </div>
      </div>
      </div>
      

      
      <div class="form-group  text-center">
        <label for="gerente">Gerente</label>
        <select class="form-control" id="gerente" name="gerente" required>
          <!--- se van a traer los empleados desde la base de datos -->
        </select>
      </div>


      <button type="submit" class="btn btn-danger my-btn btn-block"><span class="glyphicon glyphicon-off"></span> Registro</button>
    

     </div>
    </div>
  </div>
</div>












</div>	

<script src="js/jquery-3.1.1.js"></script>
<script src="js/bootstrap.js"></script>
</body>
</html>
