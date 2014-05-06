
{- 
	The Perfect Cereal 
Algorithms and Datastructures 
	- Assignment 6 -

-> $ ghc -prof -fprof-auto -rtsopts ad6.hs
-> $ ./ad6 +RTS -p
-> needs a main
-> http://www.haskell.org/ghc/docs/7.6.2/html/users_guide/profiling.html

Usage:

ghci> let v_max = 30.0

ghci> perfectCereal prods1 v_max
[("corn",17.0,8.0),("honey",13.0,6.0)]

ghci> perfectCereal prods6 v_max
[("chocolate",1.0,4.0),("sugar",21.0,6.0),("banana",2.0,7.0),("cherry",5.0,2.0)]

ghci> let sol = perfectCereal prods6 v_max
ghci> to_s sol v_max
"Perfect Cereal: [(\"chocolate\",1.0,4.0),(\"sugar\",21.0,6.0),(\"banana\",2.0,7.0),
(\"cherry\",5.0,2.0)] => (price: 19.0, vol: 29.0, rating: 5.26315789)"

-}

import Debug.Trace

-- TestCases
prods1 = [("cherry", 5.0, 2.0),("walnut", 5.0, 8.0),("banana", 2.0, 7.0),("honey", 13.0, 6.0),("sugar", 21.0, 6.0),("chocolate", 1.0, 4.0),("strawberry", 34.0, 10.0),("apple", 20.0, 12.0),("corn", 17.0, 8.0),("blueberry", 1.0, 1.0)]
prods2 = [("cherry", 5.0, 2.0),("walnut", 10.0, 14.0),("banana", 19.0, 14.0),("honey", 13.0, 6.0)]
prods3 = [("cherry", 5.0, 2.0),("walnut", 10.0, 14.0),("banana", 19.0, 140.0),("honey", 13.0, 6.0)]
prods4 = [("banana", 19.0, 140.0),("honey", 13.0, 6.0)]
prods5 = [("cherry", 5.0, 1.0),("walnut", 10.0, 14.0),("banana", 12.0, 1.0),("honey", 13.0, 6.0)]
prods6 = [("cherry", 5.0, 2.0),("walnut", 5.0, 8.0),("banana", 2.0, 7.0),("honey", 13.0, 6.0),("sugar", 21.0, 6.0),("chocolate", 1.0, 4.0)]
prods7 = [("cherry", 10.0, 2.0),("walnut", 10.0, 2.0),("banana", 10.0, 2.0),("honey", 10.0, 6.0),("sugar", 10.0, 6.0),("chocolate", 30.0, 6.0)]
prods8 = [("cherry", 10.0, 2.0),("walnut", 10.0, 2.0)]
prods9 = [("cherry", 20.0, 4.0)]

prods10 = (take 18 $ zip3 (map (show) [1..]) [1..] [5..])

-- rating amount v_max = rating amount v_max
l = [prods1,prods2,prods3,prods4,prods5,prods6,prods7,prods8,prods9]
infinity_correction = 1.0001

-- Immediate Usage
m = 30.0
sol = map (\n -> perfectCereal n m) l
test1 = map (\n -> to_s n m) sol

sol2 = perfectCereal prods10 m
test2 = to_s sol2 m

main = print (perfectCereal prods10 m)

to_s :: [(String, Double, Double)] -> Double -> String
to_s solution v_max = "Perfect Cereal: " ++ solution_to_s ++ "(" ++ price ++ volume ++ rate ++ ")"	
		where
			solution_to_s = (show solution) ++ " => "
			price = "price: " ++ (show $ sumPrice solution)
			volume = ", vol: " ++ (show $ sumVol solution)
			-- Rating gets a delta for better readability
			rate = ", rating: " ++ (take 10 $ show $ rating solution v_max)		


-- Main Call
perfectCereal :: [(String, Double, Double)] -> Double -> [(String, Double, Double)]
perfectCereal products v_max = perfectCereal' [] (overMaxVol products) v_max
		where 
			{- Optimization before calling the Algorithm. The Assumption is
			all products in the product list that have a higher volume than the 
			maximum allowed volume are not needed -}
			overMaxVol = filter (\(_, vol, _) -> vol <= v_max)


{- Given a list of chosen products and a list of still availible products 
(and the maximum) it calculates the best choice of products according to 
the rating function -}
perfectCereal' :: [(String, Double, Double)] -> [(String, Double, Double)] -> Double -> [(String, Double, Double)]
perfectCereal' solution [] v_max = solution
perfectCereal' solution (prod:products) v_max 
				-- Compare ratio of current selection
				| ratio_with_prod > ratio_without_prod = with_prod
				| otherwise = without_prod
					where
						{- Assumption: the ratio with the currently selected product could be 
						better than without it. If so add the product to the current solution. -}
						with_prod = perfectCereal' (prod:solution) products v_max
						without_prod = perfectCereal' solution products v_max
						-- calculates the ratio with and without the selected product
						ratio_with_prod = rating with_prod v_max
						ratio_without_prod = rating without_prod v_max


{- Calculates the rating of the current amount. Divides the product by 1.0 so that higher
products result in lower ratios and lower products mean a higher rating. If the rating is 
equal to Infinity it means it is the optimal rating. -}
rating :: [(String, Double, Double)] -> Double -> Double
rating amount v_max = 1.0 / product'
		where
			product' 
				{- A Product needs a volume. 1.0 / 0.0 should not be calculated. 
				That means empty amount has no ratio. -}
				| null amount = (-1.0)
				| otherwise = calcRating amount v_max

{- Calculates the Rating of a specific amount. The Rating shall 
be negative if v_max is lower than sum_vol -}
calcRating :: [(String, Double, Double)] -> Double -> Double
calcRating amount v_max = sum_price * (v_max * infinity_correction - sum_vol)
				where
					sum_price = sumPrice amount
					sum_vol = sumVol amount


sumPrice :: [(String, Double, Double)] -> Double
sumPrice amount = foldl (\acc (_, _, price) -> acc + price) 0.0 amount

sumVol :: [(String, Double, Double)] -> Double
sumVol amount = foldl (\acc (_, vol, _) -> acc + vol) 0.0 amount






