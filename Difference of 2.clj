;; https://www.codewars.com/kata/5340298112fa30e786000688

;; The objective is to return all pairs of integers from a given array of integers that have a difference of 2.

;; The result array should be sorted in ascending order of values.

;; Assume there are no duplicate integers in the array. The order of the integers in the input array should not matter.

(ns difftwo)

(defn twos-difference [lst]
  (into [] (let [st (into #{} lst)
        lst (sort lst)]
    (for [i lst
          :let [j (+ 2 i)]
          :when (contains? st j)]
      [i j]))))
