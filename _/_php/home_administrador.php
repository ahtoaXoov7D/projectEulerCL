<?php
   //include('sesion/session.php');
?>


<html><head>
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




	<div class="row" style="padding-top: 60px">
    <div class="col-lg-4 col-lg-offset-4 col-md-4 col-md-offset-4 col-sm-4 col-sm-offset-4">
      <div class="formulario" style="padding:0">
        <h1 class="text-center" style="padding-top:30px; padding-bottom:30px; opacity: 0.5; margin:0; background-color:#C4C4CC">SneakerLand</h1>
        <div style="padding:40px 50px; text-align: center;">
            <h3>Bienvenido Administrador</h3>
        </div>
      </div>
    </div>
	 
</div>
</div>

<script src="js/jquery-3.1.1.js"></script>
<script src="js/bootstrap.js"></script>

</body></html>
