(defun c:lab5()

(setq os (getvar "osmode"))
(setvar "osmode" 0)

(command "_box" "0,0,0" "90,80,20")
(setq m1 (entlast))
(command "_box" "0,0,20" "30,80,40")
(setq m2 (entlast))
(command "_box" "70,0,20" "90,80,135")
(setq m3 (entlast))
(command "_box" "60,0,120" "90,80,135")
(setq m4 (entlast))
(command "_box" "60,20,120" "90,60,135")
(setq b1 (entlast))
(command "����" "70,30,20" "30,50,20" "60")
(setq m5 (entlast))
(command "_box" "60,0,135" "90,80,165")
(setq b3 (entlast))

(command "������" "0,20,0" "15,10" "15,70" "0,60" "0,20" "");������ ������

(command "��������" (entlast) "" "40");������������ ������
(setq a1 (entlast))
(command "_ucs"
	 "3"
	 (list 90 0 0)
	 (list 90 80 0)
	 (list 90 0 135)
)
(command "�������" "40,120,-30" "40" "30");������� �������
(setq m6 (entlast))
(command "�������" "40,120,-30" "20" "30");����� �������
(setq b2 (entlast))

  
(command "_union" m1 m2 m3 m4 m5 m6 "")
(command "_subtract" m1 "" b1 b2 b3 a1 "")
(command "_ucs" "" )

(setvar "osmode" os)

)
;;;(command "_ucs" "3" (list 0 80 0) (list 0 0 0) (list 90 80 0))