;; https://www.codewars.com/kata/58f5c63f1e26ecda7e000029

;; In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string 
;; and you must return that string in an array where an uppercase letter is a person standing up. 
;; exp. wave("hello") => []string{"Hello", "hEllo", "heLlo", "helLo", "hellO"}


(require '[clojure.string :as cs])

;; capitalizes ith character of string
(defn cap [s i]
 (str (subs s 0 i) (clojure.string/upper-case (get s i)) (subs s (inc i))))

(defn wave [string]
  (into []
    (for
      [i (range (count string))
      :when (not= (str (get string i)) " ")]
      (cap string i))))
