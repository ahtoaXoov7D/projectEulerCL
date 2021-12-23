name := "euler"

organization in Global := "pl.scalania"

version in Global := "0.1"

scalaVersion in Global := "2.11.5"

scalacOptions ++= Seq("-deprecation", "-unchecked", "-feature","-Yrangepos")

scalacOptions in Global ++= Seq("-deprecation", "-unchecked", "-feature","-Yrangepos")

val scalaLogging = "com.typesafe.scala-logging" %% "scala-logging" % "3.1.0"

val scalacheck = "org.scalacheck" %% "scalacheck" % "1.12.1"

libraryDependencies in Global ++= Seq(
  scalaLogging,
  scalacheck % "test",
  "org.scalatest" %% "scalatest" % "2.2.3" % "test",
  "ch.qos.logback" % "logback-classic" % "1.1.2"
)


scalariformSettings




