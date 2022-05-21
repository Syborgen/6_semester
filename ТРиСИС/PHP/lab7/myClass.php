<?php
namespace lab7;

class myClass{
 	function getRecursiveCFiles($root) {
	    $all_files_list = new \RecursiveIteratorIterator(new \RecursiveDirectoryIterator($root), \RecursiveIteratorIterator::SELF_FIRST);
	    $name_files_list = array();
	    $ended_files_list = array(); 
	    foreach ($all_files_list as $file) {
	        if (preg_match('/^\.[A-z]{2}.*\.c$/', basename($file))) {
	            $name_files_list[] = $file;
	        }
	    }
	    foreach ($name_files_list as $file) {
	    	$file_date = round((time()-date(filemtime($file))) / (60*60*24));
	    	$file_name = basename($file);
	    	if(($file_date) < 7 && is_readable($file) && !is_writable($file) && !is_executable($file)){
	    		$ended_files_list[] = $file;
	    	}

	    }

	    return $ended_files_list;
	}




	public function scanDirectory($str){
		foreach (glob($str."/*") as $file) {
			//echo basename($file) . " (size: " . filesize($file) . " bytes)" . "<br>";// delete
			if (is_dir($file)){
				echo "<br>";// delete
				$this->scanDirectory($file);
				echo '<br>';// delete
			} else if(preg_match('/\./',basename($file))) {
				$this->checkFile($file);

			}
		}
	}

	public function checkFile($str){
		$max_depth = 0;
		$cur_depth = 0;
		echo '<br>' . "Сожержимое файла " . $str . " : " ;
		$file = fopen($str,'r') or die("не удалось открыть файл.");
		while (!feof($file)){
			$cur_string = fgets($file);
			$string_length = strlen($cur_string);
			echo '<br>';
			for ($i = 0; $i < $string_length; $i++) { 
				echo $cur_string[$i];
				switch ($cur_string[$i]) {
					case '(':
					case '{':
					case '[':
						$cur_depth++;
						break;
					case ')':
					case '}':
					case ']':
						$cur_depth--;
						break;
				}
				if ($cur_depth>$max_depth){
					$max_depth=$cur_depth;
				}
			}
			
		}
		fclose($file);
		echo "<br>"."max_depth = ".$max_depth;
		if ($max_depth>2){
				echo '(Будет удалено)<br>';
				return true;
			}
			else{ 
				echo '(Не будет удалено)<br>';
				return false;
			}
	}
}
?>
<!-- 11. Пройти по дереву каталогов, начиная с текущего, и удалить все     файлы на языке Си, содержащие внутри максимальное количество вложенных скобок более 2 и имеющие шаблон имени файла: начинаются с точки, потом - две буквы  латинского алфавита, а далее любые и младше недели с правами на чтение. -->