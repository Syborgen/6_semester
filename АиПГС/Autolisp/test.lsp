(defun c:test()

(setq os (getvar "osmode"))
(setvar "osmode" 0)

(command "_box" "0,0,0" "90,80,20")
(setq m1 (entlast))


(command "_union" m1 m2 m3 m4 m5 m6 "")
(command "_subtract" m1 "" b1 b2 b3 a1 "")
(command "_ucs" "" )

(setvar "osmode" os)

)
;;;(command "_ucs" "3" (list 0 80 0) (list 0 0 0) (list 90 80 0))