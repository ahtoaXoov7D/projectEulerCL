
;; I want to practice with the esolang Hanabi semantically without the
;; syntax concerns, so I'll be implementing an interpreter for a
;; semantically similar but syntactically simpler language here.

(define-condition goto-signal (condition)
  ((line :initarg :line :reader goto-signal-line)))

(defvar *stack* nil)

(defun goto (label)
  (signal 'goto-signal :line label))

(defun to-n (bool)
  (if bool 1 0))

(defun run-command (command &key file)
  (ecase (first command)
    (push (push (second command) *stack*))
    (inputn (push (read file) *stack*))
    (length (push (length stack) *stack*))
    (swap (let ((a (pop *stack*))
                (b (pop *stack*)))
            (push a *stack*)
            (push b *stack*)))
    (reverse (setf *stack* (nreverse *stack*)))
    (reversen (let ((prefix (subseq *stack* 0 (second command))))
                (replace *stack* (nreverse prefix) :end1 (second command))))
    (rotateup (let ((top (pop *stack*)))
                (rplacd (last *stack*) (cons top nil))))
    (rotateupn (let* ((sub (subseq *stack* 0 (second command)))
                      (top (pop sub)))
                 (rplacd (last sub) (cons top nil))
                 (replace *stack* sub :end1 (second command))))
    (rotatedown (let ((bottom (car (last *stack*))))
                  (setf *stack* (cons bottom (nbutlast *stack*)))))
    (rotatedownn (let* ((sub (subseq *stack* 0 (second command)))
                        (bottom (car (last sub))))
                   (setf sub (cons bottom (nbutlast sub)))
                   (replace *stack* sub :end1 (second command))))
    (outputn (format t "~S" (pop *stack*)))
    (nl (format t "~%"))
    (pop (pop *stack*))
    (popn (loop repeat (second command) do (pop *stack*)))
    (clear (setf *stack* nil))
    (dup (setf *stack* (cons (car *stack*) *stack*)))
    (== (push (to-n (= (pop *stack*) (pop *stack*))) *stack*))
    (!= (push (to-n (not (= (pop *stack*) (pop *stack*)))) *stack*))
    (< (push (to-n (> (pop *stack*) (pop *stack*))) *stack*))
    (> (push (to-n (< (pop *stack*) (pop *stack*))) *stack*))
    (<= (push (to-n (>= (pop *stack*) (pop *stack*))) *stack*))
    (>= (push (to-n (<= (pop *stack*) (pop *stack*))) *stack*))
    (+ (let ((y (pop *stack*)) (x (pop *stack*))) (push (+ x y) *stack*)))
    (* (let ((y (pop *stack*)) (x (pop *stack*))) (push (* x y) *stack*)))
    (- (let ((y (pop *stack*)) (x (pop *stack*))) (push (- x y) *stack*)))
    (/ (let ((y (pop *stack*)) (x (pop *stack*))) (push (/ x y) *stack*)))
    (^ (let ((y (pop *stack*)) (x (pop *stack*))) (push (expt x y) *stack*)))
    (log (let ((y (pop *stack*)) (x (pop *stack*))) (push (log y x) *stack*)))
    (label nil) ; Noop (handled separately)
    (goto (goto (second command)))
    (goto-if-nonzero (let ((v (pop *stack*)))
                       (unless (= v 0) (goto (second command)))))
    (goto-if-zero (let ((v (pop *stack*)))
                    (when (= v 0) (goto (second command)))))))

(defun run-commands (commands &key file)
  (let ((label-hash (make-hash-table)))
    (loop for command across commands
          for index upfrom 0
          when (eql (first command) 'label)
            do (setf (gethash (second command) label-hash) index))
    (loop for index from 0 below (length commands)
          do (handler-bind
                 ((goto-signal
                    (lambda (c) (setf index (gethash (goto-signal-line c) label-hash)))))
               (run-command (elt commands index) :file file)))))

(defvar *program*
  #((push 0)
    (push 0)
    (push 1)
    (label loop-start)
    (push 2)
    (inputn)
    (log)
    (inputn)
    (*)
    (dup)
    (rotatedown)
    (dup)
    (rotateup)
    (<=)
    (goto-if-nonzero skip-save)
    (reverse)
    (popn 2)
    (dup)
    (goto next-iter)
    (label skip-save)
    (pop)
    (label next-iter)
    (push 1)
    (+)
    (dup)
    (push 1000)
    (<=)
    (goto-if-nonzero loop-start)
    (pop)
    (outputn)
    (nl)
    (pop)))

(let ((*stack* nil))
  (with-open-file (stream "./files/p099_base_exp.txt")
    (run-commands *program* :file stream))
  (format t "~S~%" *stack*))

;; *** LABELS ***
;; loop-start  0
;; skip-save   1
;; next-iter   2