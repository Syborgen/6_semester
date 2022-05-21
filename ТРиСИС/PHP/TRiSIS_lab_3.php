<?php
echo '<b>'."Задание: Все нечетные слова англоязычного текста в файле перевести в верхний регистр".'</b>'.'<br/>'.'<br/>';

$fr = fopen("text2.txt", 'r') or die("не удалось открыть файл");
echo '<b>'."Содержимое файла:".'</b>'.'<br/>';
while(!feof($fr))
{
    $str = fgets($fr);
    echo $str . '<br/>'; 
}
fclose($fr);

$fd = fopen("text2.txt", 'r') or die("не удалось открыть файл");
echo '<br/>'.'<b>'."Преобразованный текст:".'</b>'.'<br/>';
$fw = fopen("TRiSIS_lab_3_write.txt", 'w');

$str = fgets($fd);#read
$tmp = preg_replace_callback('/(\b[A-z]+\b)(.*)/',
 function($match){return strtoupper($match[1]);},$str);#extract 1st word
$rstr = preg_replace('/(\b[A-z]+\b)/U','',$str,1);#delete 1st word
$rstr = preg_replace_callback('/(\b[A-z]+\b)(.*)(\b[A-z]+\b)/U',
 function($match){return $match[1].$match[2].strtoupper($match[3]);},$rstr);#each 2nd word to UPPERCASE
echo  $tmp . $rstr . '<br/>';
fwrite($fw, $tmp . $rstr);

fclose($fd);
fclose($fw);
?>