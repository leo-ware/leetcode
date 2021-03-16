;; Finds the longest monotonically increasing (>=) subarray of a vector in log linear time

(defn max-through [array m]
  (if (<= (count array) 1)
    array
    (let [r-bound (first (filter
                          #(< (get array %) (get array (- % 1)))
                          (range (+ 1 m) (count array))))
          l-bound (first (filter
                          #(> (get array %) (get array (+ % 1)))
                          (reverse (range m))))
          real-r (if r-bound r-bound (count array))
          real-l (if l-bound (+ 1 l-bound) 0)]
      
      (subvec array real-l real-r))))

(defn max-subarray [array]
  (let [m (quot (count array) 2)]
    (if (empty? array) []
        (max-key count
         (max-through array m)
         (max-subarray (subvec array 0 m))
         (max-subarray (subvec array (+ 1 m)))))))
