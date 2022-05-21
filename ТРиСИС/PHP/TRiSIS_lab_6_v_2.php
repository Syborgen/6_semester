<?php

include("tcpdf/tcpdf.php");
include("vendor/autoload.php");

$first_page = 'Это абзац №1';
$second_page = 'Абзац №2';


function generate_pdf() {
    $pdf = new TCPDF('P', 'mm', 'A4', true, 'UTF-8');
    $pdf->SetFont('dejavusans', '', 14, '', true);
    $pdf->SetAuthor("Arsenii Morgunov");
    $pdf->SetTitle("Lab5");
    $pdf->SetSubject("Create lab five");
    $pdf->Annotation(10, 10, 100, 0, "Annotation\nPlace for information", array('Subtype'=>'Text', 'Name' => 'Comment', 'T' => '@arsenii', 'Subj' => 'Insta', 'C' => array(255, 255, 0)));

    $pdf->AddPage();
    global $first_page;
    $pdf->Write(1.5, $first_page);
    $pdf->Ln();
    global $second_page;
    $pdf->Write(1.5, $second_page);
    $pdf->Ln();

    $pdf->writeHTML("<span style=\"color: green ; letter-spacing: 1px\">Разное межсимвольное расстояние №1</span>");
    $pdf->writeHTML("<span style=\"color: blue; letter-spacing: 10px\">Разное межсимвольное расстояние №2</span>");
    $pdf->writeHTML("<span style=\"color: red ; letter-spacing: 20px\">Разное межсимвольное расстояние №3</span>");

    $pdf->Write(1, "Разное межстрочное расстояние №1");
    $pdf->Ln();
    $pdf->Write(1, "Разное межстрочное расстояние №1");
    $pdf->Ln();


    $pdf->Write(10, "Разное межстрочное расстояние №2");
    $pdf->Ln();
    $pdf->Write(10, "Разное межстрочное расстояние №2");
    $pdf->Ln();

    $pdf->Write(20, "Разное межстрочное расстояние №3");
    $pdf->Ln();
    $pdf->Write(20, "Разное межстрочное расстояние №3");
    $pdf->Ln();


    $aligns = array('L'=>'Left', 'R'=>'Right', 'C'=>'Center', 'J'=>'Justify');
    foreach ($aligns as $align_mode => $align_name) {
        $txt = "Выравнивание : " . $align_name;
        $pdf->Write(0, $txt, '', 0, $align_mode, true, 0, false, false, 0);
        $pdf->Ln();
    }

    $pdf->AddPage();
    $pdf->StartTransform();
    $pdf->rotate(-45);
    $pdf->Write(4, 'Поворот №1');
    $pdf->rotate(90);
    $pdf->Write(4, 'Поворот №2');
    $pdf->StopTransform();
    $pdf->Ln(70);
    $pdf->StartTransform();
    $pdf->rotate(90);
    $pdf->Write(4, 'Поворот №3');
    $pdf->rotate(-180);
    $pdf->Write(4, 'Поворот №4');
    $pdf->StopTransform();

    $pdf->AddPage();
    $pdf->Image('linux.png', '', '', 190, 150, 'PNG', '', '', true, 150, '', false, false, 1, false, false, false);
    $pdf->Ln(250);
    $pdf->Image('firehorse.jpg', '', '', 190, 150, 'JPG', '', '', true, 150, '', false, false, 1, false, false, false);
    $pdf->Ln(250);
    $pdf->Image('lightning.jpg', '', '', 190, 150, 'JPG', '', '', true, 150, '', false, false, 1, false, false, false);
    $pdf->Ln(250);

    return $pdf;
}

function generate_word() {
    $word = new \PhpOffice\PhpWord\PhpWord();
    $word->setDefaultParagraphStyle(
        array('spacing'=>120)
    );
    $section = $word->addSection();
    $section->addText("Это абзац №1.");
    $section->addText("Абзац №2");
    $word->addFontStyle('r2Style', array('bold'=>false, 'italic'=>false, 'size'=>14));
    $word->addParagraphStyle('b2Style', array('align'=>'both', 'spaceAfter'=>100, 'spacing'=>450));
    $word->addParagraphStyle('s2Style', array('align'=>'start', 'spaceAfter'=>100));
    $word->addParagraphStyle('e2Style', array('align'=>'end', 'spaceAfter'=>100));
    $word->addParagraphStyle('c2Style', array('align'=>'center', 'spaceAfter'=>100));
    $section->addText("Межстрочный интервал №1 Межстрочный интервал №1 Межстрочный интервал №1 Межстрочный интервал №1", 'r2Style', 'b2Style');
    $section->addText("Межстрочный интервал №2 Межстрочный интервал №2 Межстрочный интервал №2 Межстрочный интервал №2", 'r2Style', 's2Style');
    $section->addText("Выравнивание: left", 'r2Style', 's2Style');
    $section->addText("Выравнивание: Center", 'r2Style', 'c2Style');
    $section->addText("Выравнивание: Right", 'r2Style', 'e2Style');
    

    $table = $section->addTable();
    $table->addRow(900);
    $cell = $table->addCell(500, array('textDirection'=>\PhpOffice\PhpWord\Style\Cell::TEXT_DIR_BTLR) );
    $cell->addText("Поворот влево");
    $new_cell = $table->addCell(500, array('textDirection'=>\PhpOffice\PhpWord\Style\Cell::TEXT_DIR_TBRL) );
    $new_cell->addText("Поворот вправо");
 	$section = $word->addSection();
    $section->addImage("linux.png", array('width'=>459, 'height'=>300, 'wrappingStyle'=>'inline'));
    $section = $word->addSection();
    $section->addImage("firehorse.jpg", array('width'=>459, 'height'=>300, 'wrappingStyle'=>'inline'));
    $section = $word->addSection();
     $section->addImage("lightning.jpg", array('width'=>459, 'height'=>300, 'wrappingStyle'=>'inline'));



    
    $writer = \PhpOffice\PhpWord\IOFactory::createWriter($word,'Word2007');
    $writer->save('word_document.docx');

    return $word;
}

function read_word() {
    $phpWord = \PhpOffice\PhpWord\IOFactory::load('word_document.docx');
    $sections = $phpWord->getSections();

    $text = '';

    foreach ($sections as $section) {
        $els = $section->getElements();
        foreach ($els as $e) {
            if (get_class($e) === \PhpOffice\PhpWord\Element\TextRun::class) {
                foreach ($e->getElements() as $texts) {
                    if (get_class($texts) === \PhpOffice\PhpWord\Element\Text::class) {
                        $text .=  getWordsFromString($texts->getText())[0] . " ";
                    }
                }
            }
        }
    }
    echo  $text;
}

function getWordsFromString($string)
{
    if (preg_match_all("/\b(\w+)\b/ui", $string, $matches)) {
        return $matches[1];
    }
    return array();
}

$pdf = generate_pdf();
generate_word();
$word = \PhpOffice\PhpWord\IOFactory::load('word_document.docx');
read_word();

   //$pdf->Output();
$pdf->Output(__DIR__ . '/file.pdf', 'F');
echo "<iframe src=\"file.pdf\" width=\"900px\" style=\"height:1200px\"></iframe>";



$file = "word_document.docx";
header ("Content-Type: application/force-download");
header ("Accept-Ranges: bytes");
header ("Content-Length: ".filesize($file));
header ("Content-Disposition: attachment; filename=".$file);
readfile($file);

?>
