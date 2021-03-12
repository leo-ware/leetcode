;; https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

;; Write a function, persistence, that takes in a positive parameter num and returns its 
;; multiplicative persistence, which is the number of times you must multiply the digits 
;; in num until you reach a single digit.

(ns persistent.core)

(defn _p [n c]
    (let [i (reduce * (map #(Integer. (str %)) (into () (str n))))]
        (if (< i 10) c
            (_p i (+ c 1)))))

(defn persistence [n]
    (if (< n 10) 0
        (_p (Math/abs n) 1)))
