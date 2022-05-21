<?php

spl_autoload_register(function ($class_name) {
	$file_name = preg_replace('/(\\\)/','/', $class_name);
    include $file_name . '.php';
});

$class = new lab7\myClass;

print("Файлы, подходящие по имени, правам и дате: <br>");

$files = $class->getRecursiveCFiles('laba_7');
foreach ($files as $file) {
	//print($file);
	if($class->checkFile($file)){
		//unlink($file);
	}


}

?>