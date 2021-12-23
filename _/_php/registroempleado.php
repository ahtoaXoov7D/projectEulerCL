<?php
session_start();
include "conection/conexion.php";
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
	<div class="col-lg-6 col-lg-offset-3">
    <div class="formulario" style="padding:0">
	   <h1 class="text-center" style="padding-top:30px; padding-bottom:30px; opacity: 0.5; margin:0; background-color:#C4C4CC">Registrar Empleado</h1>
       <div style="padding:40px 50px">
        <form role="form" method="POST" action="validar_registroempleado.php" >

          <div class="form-group text-center " >
          <label for="usrname"> Nombre(s)</label>
          <input type="text" class="form-control" id="usrname" name="nombres" maxlength="50" required value="<?php echo $nombres; ?>">
          </div>

          <div class="form-group text-center " >
          <label for="appaterno"> Apellido Paterno</label>
          <input type="text" class="form-control" id="appaterno" name="appaterno" required value="<?php echo $appaterno; ?>">
          </div>

          <div class="form-group text-center " >
          <label for="apmaterno"> Apellido Materno</label>
          <input type="text" class="form-control" id="apmaterno" name="apmaterno" required value="<?php echo $apmaterno; ?>">
          </div>

          <div class="form-group text-center">
          <label for="curp"> CURP</label>
          <input type="text" class="form-control" id="curp" name="curp" maxlength="18" required value="<?php echo $curp; ?>">
          </div>

          <div class="form-group text-center">
          <label for="rfc"> RFC</label>
          <input class="form-control" id="rfc" type="text" name="rfc" maxlength="13" required value="<?php echo $rfc; ?>">
          </div>

          <div class="form-group text-center">
          <label for="tel"> Teléfono</label>
          <input type="text" class="form-control" id="tel" name="tel" maxlength="15" required value="<?php echo $tel; ?>">
          </div>

		  <div class="form-group text-center">
          <label for="salario"> Salario</label>
          <input type="text" class="form-control" id="salario" name="salario" required value="<?php echo $salario; ?>">
          </div>


          <div class="form-group  text-center">
          <label for="sel1">Escolaridad</label>
          <select class="form-control" id="sel1" name="sel1" required>
            <option value="1">Primaria</option>
            <option value="2">Secundaria</option>
            <option value="3">Preparatoria</option>
            <option value="4">Licenciatura</option>
          </select>
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

	        <div class="col-lg-6">
            <label for="cp">CP</label>
            <select class="form-control" id="cp" name="cp" required>

            <?php conectar();


             if (!$conexion) {
				die("Connection failed: " . mysqli_connect_error());
        	}

            $sqlselect = "SELECT * FROM cp";
            $resultset = mysqli_query($conexion, $sqlselect);

            while ($fila=mysqli_fetch_array($resultset)) {

            ?>

            <option value="<?php echo $fila['cp'];?>"><?php echo $fila["cp"]; ?></option>

            <?php  
          	}
        	?>
            </select>
            </div>
	      </div> 

	      <?php desconectar();?>


	      </br>
          <h1 class="text-center" style="padding-top:30px; padding-bottom:30px; opacity: 0.5; margin:0; background-color:#C4C4CC">Usuario</h1></br>

          <div class="form-group text-center">
          <label for="contraseña"> Contraseña</label>
          <input class="form-control" id="contraseña" type="text" name="pass" maxlength="13" required value="<?php echo $password; ?>">
          </div>

           <div class="form-group text-center">
          <label for="correo">Correo</label>
          <input class="form-control" id="correo" type="text" name="correo"  required value="<?php echo $correo; ?>">
          </div>

          <div class="radio" style="text-align: left;">
          <label><input type="radio" name="nivel_usuario" value="3" checked="checked" id="radio" >Asesor de Ventas</label>
          </div>

          <div class="radio" style="text-align: left;">
          <label><input type="radio" name="nivel_usuario" value="2" >Gerente</label>
          </div>

          <div class="radio" style="text-align: left;">
          <label><input type="radio" name="nivel_usuario" value="1">Administrador</label>
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
</body></html>
