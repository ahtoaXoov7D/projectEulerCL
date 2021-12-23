<?php
session_start();
include "conection/conexion.php";





 if($_SERVER["REQUEST_METHOD"] == "POST") {

  conectar();
  
  
  if (!$conexion) {
    die("Connection failed: " . mysqli_connect_error());
  }


    $user = mysqli_real_escape_string($conexion,$_POST['user']);
    $password = mysqli_real_escape_string($conexion,$_POST['password']);
    
    $error="";

    
    $sql = "SELECT * FROM usuario WHERE id_usuario='$user' AND password='$password'";
    $result = mysqli_query($conexion,$sql);

    $row = mysqli_fetch_array($result,MYSQLI_ASSOC);
    $active = $row['active'];
      
      
    $count = mysqli_num_rows($result);

    
    if($count == 1){

    $_SESSION["login_user"] = $user;

      switch ($row["id_nivel_usuario"]) {
          case 1:
              //desconectar();
              header("location: home_administrador.php");
	            desconectar();
              break;
          case 2:
               header("location: home_gerente.php");
               desconectar();
              break;
          case 3:
               header("location: home_asesor.php");
               desconectar();
              break;
          default:
               header("location: index.php");
               desconectar();
      }    
    }
         
    else{
      $error="Usuario y/o contraseña equivocados";
    }

 }


?>











<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel="stylesheet" type="text/css" href="css/bootstrap.css">
<link rel="stylesheet" type="text/css" href="css/estilos.css">
<title>Sneakerland | Tus Sneakers hablan por ti</title>
</head>
<body >

<div class="body"></div>
<div class="container-fluid">
	<div class="row">
		<div class="col-xs-8 col-xs-offset-2
		col-sm-8 col-sm-offset-2 
		col-lg-4 col-lg-offset-4 
		verticalcenter color" style="padding:0">
		<h1 class="text-center" style="padding-top:30px; padding-bottom:30px; opacity: 0.5; margin:0; background-color:#C4C4CC">Iniciar Sesión</h1>
		<div style="padding:40px 50px">
		<form role="form" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="POST">
            <div class="form-group text-center">
              <label for="usrname" ><span class="glyphicon glyphicon-user"></span> Usuario</label>
              <input type="text" class="form-control" id="usrname" name="user" placeholder="Introduzca Usuario" required>
            <div class="form-group text-center" style="padding-top:30px; padding-bottom:20px">
              <label for="psw"><span class="glyphicon glyphicon-lock"></span> Contraseña</label>
              <input type="password" class="form-control" id="psw" name="password" placeholder="Introduzca Contraseña" required>
            </div>
            </div>
            <button type="submit" class="btn btn-danger my-btn btn-block" ><span class="glyphicon glyphicon-off"></span>Entrar</button>
            <div class="error text-center" style="padding-top: 10px; color:red"><?php echo  $error?></div>
        </form>
        </div>
		</div>
	</div>
</div>

<script src="js/jquery-3.1.1.js"></script>
<script src="js/bootstrap.js"></script>

</body>
</html>
