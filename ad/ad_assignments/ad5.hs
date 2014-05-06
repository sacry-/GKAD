import Debug.Trace

{- inefficient recursion -}
f_rec 0 = 1
f_rec 1 = 1
f_rec 2 = 1
f_rec n = f_rec (n-1) + 2 * f_rec (n - 2) + 3 * f_rec (n - 3)

{- efficient tail recursion -}
f_end n = f' 1 1 1 n
	where
		f' n1 n2 n3 n 
			| n `elem` [0, 1, 2] = n1
			| otherwise = f' (acc n1 n2 n3 n) n1 n2 (n-1)
		acc n1 n2 n3 n = (n1 + (2 * n2) + (3 * n3))

--show first n results of the original impl.
show1 n = print $ take n $ map (\x -> (x, f x)) [0..]
--show first n results of the tail-recursive-impl.
show2 n = print $ take n $ map (\x -> (x, f_endrec x)) [0..]
--show both for the first n integers
showboth n = print $ take n $ map (\x -> (x, f x, f_endrec x)) [0..]
--show the difference of both impls. for the first n integers
showdiff n = print $ take n $ map (\x -> (x, (f x)-(f_endrec x))) [0..]

