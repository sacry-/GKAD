import Data.List


nil = (-1, -1, -1)
nil_elem = -1

bestInvestment :: [Int] -> (Int, Int, Int)
bestInvestment [] = nil
bestInvestment [x] = nil
bestInvestment kurs = bestInvest minimum maximum
	where
		minimum = minimumList kurs 
		maximum = maximumList kurs


bestInvest :: [Int] -> [Int] -> (Int, Int, Int)
bestInvest [] _ = nil
bestInvest kmin kmax 
			| max_difference > 0 = (minimum_idx, maximum_idx, max_difference) 
			| otherwise = nil
			where
				kzip = (zip kmin kmax)
				minimum_idx = minimumIndex kzip
				difference = kzip !! minimum_idx
				max_difference = calcDiff difference
				maximum_idx = maximumIndex kzip minimum_idx difference
			

calcDiff :: (Int, Int) -> Int
calcDiff x = (snd x) - (fst x)


minimumIndex :: [(Int, Int)] -> Int
minimumIndex [] = nil_elem
minimumIndex (x:xs) = midx' x (x:xs) 0 0
		where
			midx' _ [] idx max_idx = max_idx
			midx' y (z:zs) idx max_idx
				| calcDiff y >= calcDiff z = midx' y zs (idx + 1) max_idx
				| otherwise =  midx' z zs (idx + 1) idx

maximumIndex :: [(Int, Int)] -> Int -> (Int, Int) -> Int
maximumIndex [] _ _ = nil_elem
maximumIndex xs min_idx max_diff = max_offset + min_idx - 1
		where
			k_from_min = drop min_idx xs
			max_offset = length $ takeWhile (==max_diff) k_from_min


minimumList :: [Int] -> [Int]
minimumList [] = []
minimumList (x:xs) = mlist' min x (x:xs)


maximumList :: [Int] -> [Int]
maximumList [] = []
maximumList xs = reverse $ mlist' max (last xs) (reverse xs)


mlist' :: (Int -> Int -> Int) -> Int -> [Int] -> [Int]
mlist' _ _ [] = []
mlist' f x (y:ys) =  applied : mlist' f applied ys
		where
			applied = f x y


{- TESTS -}
-- Positive Tests
positive_lists = 
	[
		[2,5,2,9,3,4,0,2], 
		[3,5,7,9,4,4,7,20], 
		[3,19,7,9,4,2,7,20], 
		[1,2], 
		[1,10,2,2,1,1,0,0], 
		[5,3,7,5,6,2,8,5,1], 
		[1,2,3,4,10,6,7,8,9,10] 
	]

positive_results = 
	[
		(0,3,7), 
		(0,7,17), 
		(5,7,18), 
		(0,1,1), 
		(0,1,9), 
		(5,6,6), 
		(0,9,9) 
	]

positive_zip = zip positive_lists positive_results
print_test_positive = show $ map (\x -> (bestInvestment (fst x), snd x)) $ positive_zip
positive_test_success = all (\x -> (bestInvestment (fst x)) == snd x) $ positive_zip

-- Negative Tests
negative_lists = 
	[
		[2,1], 
		[2,2], 
		[3,3,2,2,1,1,0,0]
	]

print_test_negative = show $ map (\x -> (bestInvestment x, nil)) $ negative_lists
positive_test_negative = all (\x -> (bestInvestment x) == nil) $ negative_lists

-- All Tests Correct?
all_success = positive_test_success && positive_test_negative


initial = [2,5,2,9,3,4,0,2]
kmin = minimumList initial
kmax = maximumList initial
kzip = zip kmin kmax
