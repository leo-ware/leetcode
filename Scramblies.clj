;; https://www.codewars.com/kata/55c04b4cc56a697bb0000048

;; Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2,
;; otherwise returns false.


;; 
;; recursive solution

(defn _scramble [s1 s2]
  (cond
    (empty? s2) true
    (empty? s1) false
    (= (first s1) (first s2)) (_scramble (rest s1) (rest s2))
    :else (_scramble (rest s1) s2)
    ))

(defn scramble [s1 s2]
  (_scramble (sort s1) (sort s2)))


;; 
;; using hash map

;; whether m maps c to 1 or higher
(defn oneofem [m c]
  (>= (m c 0) 1))

;; decrements entry of c in m
(defn decr [m c]
  (assoc m c (- (m c) 1)))

;; solves the problem
(defn thing [s m]
  (cond
    (empty? s) true
    (not (oneofem m (first s))) false
    :else (thing (rest s) (decr m (first s)))
    ))

;; caller function
(defn scramble [s1 s2]
  (thing s2 (frequencies s1)))
