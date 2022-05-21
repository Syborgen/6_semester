<?php
$ipng = imagecreatefrompng('linux.png');
$img = imagecreatetruecolor(1500, 1500);
$white = imagecolorallocate($img, 255, 255, 255);
imagefilledrectangle($img,0,0,1500,1500,$white);
imagecopy($img,$ipng,0,0,0,0,1200,1300);
$img2 = imagescale($img,500,500,IMG_NEAREST_NEIGHBOUR);
header("Content-Type:image/jpeg");
imagejpeg($img2,NULL,100);
?>