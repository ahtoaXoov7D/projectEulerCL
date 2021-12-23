<?php
session_start();


$servername = "localhost";
$username = "root";
$password = "31193";
$dbname = "tenis";
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
    <h1 class="text-center" style="padding-top:30px; padding-bottom:30px; opacity: 0.5; margin:0; background-color:#C4C4CC">Registro Empleado</h1>
    <div style="padding:40px 50px" class="text-center">

<?php 
if($_SERVER["REQUEST_METHOD"] == "POST") {

  $conn = new mysqli($servername, $username, $password, $dbname);

  // Check connection
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }


  $result = $conn->query("SELECT max(id_domicilio)+1 as maximo from domicilio");
  $row = $result->fetch_assoc();
  $row_cnt=$row["maximo"];
  $calle = $_POST['calle'];
  $numero = $_POST['numero'];
  $cp = $_POST['cp'];
  settype($row_cnt, "integer");
  settype($cp, "integer");
  $stmt= $conn->prepare("INSERT into  domicilio (id_domicilio,calle,num,cp) values (?,?,?,?)");
  $stmt->bind_param("issi", $row_cnt,$calle,$numero,$cp);
  
  if ($stmt->execute()) {


    $stmt = $conn->prepare("INSERT into empleado (nombre,primer_ap,segundo_ap,curp,rfc,telefono,nivel_escolar,salario,id_domicilio) values(?,?,?,?,?,?,?,?,?)");

    $password = $_POST['pass'];
    $correo = $_POST['correo'];
    $nivel = $_POST['nivel_usuario']; /* 3. Asesor de Ventas 2.Gerente 1. Administrador*/


    $nombres = $_POST['nombres'];
    $appaterno = $_POST['appaterno'];
    $apmaterno = $_POST['apmaterno'];
    $curp = $_POST['curp'];
    $rfc = $_POST['rfc'];
    $tel = $_POST['tel'];
    $salario =$_POST['salario'];
    $sel1 = $_POST['sel1'];  /*El nivel escolar es 1. Primaria, 2. Secundaria, 3. Preparatoria 4.-Licenciatura*/
    

    settype($sel1, "integer");
    settype($salario, "double");
    settype($nivel, "integer");

    $stmt->bind_param("ssssssidi", $nombres, $appaterno, $apmaterno, $curp, $rfc, $tel,$sel1, $salario,$row_cnt);

    if ($stmt->execute()) {

      $result = $conn->query("SELECT max(id_empleado) as maximo from empleado");
      $row = $result->fetch_assoc();
      $row_cnt=$row["maximo"];//numero del empleado para usuario

      $stmt = $conn->prepare("INSERT into usuario (id_usuario,id_nivel_usuario,correo,password,empleado_id_empleado)values(?,?,?,?,?)");
      $stmt->bind_param("iissi", $row_cnt,$nivel,$correo,$password,$row_cnt);

      if ($stmt->execute()) {
          echo "<h1>Usuario Registrado exitosamente!</h1></br><h3>Su usuario es: $row_cnt</br>Su contraseña es: $password</h3></br><a href='registroempleado.php'>Continuar</a>";



        } else {
          echo "<h1>No se pudo realizar la insercion de usuario</h1></br><a href='registroempleado.php'>Continuar</a>";
      }
    

      
    } else {
        echo "<h1>no se pudo realizar la insercion de empleado</h1></br><a href='registroempleado.php'>Continuar</a>";
    }
    
  } else {
    echo "<h1>no se pudo realizar la insercion de domicilio</h1></br><a href='registroempleado.php'>Continuar</a>";
  }
  

  $dia = date("Y-m-d");
  $estado=1;
  $stmt = $conn->prepare("INSERT into empleado_status (id_empleado,id_status,fecha_status)values(?,?,?)");
  $stmt->bind_param("iis", $row_cnt,$estado,$dia);
  $stmt->execute();



  $stmt->close();
  $conn->close();



}
?>

    </div>
    </div>
  </div>
</div>


</div>


<script src="js/jquery-3.1.1.js"></script>
<script src="js/bootstrap.js"></script>
</body>
</html>