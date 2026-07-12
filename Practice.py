import random
patterns = ["https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/"]

basicMaths =[
	"https://takeuforward.org/data-structure/count-digits-in-a-number/",
	"https://takeuforward.org/maths/reverse-digits-of-a-number",
	"https://takeuforward.org/data-structure/check-if-a-number-is-palindrome-or-not/",
	"https://takeuforward.org/data-structure/find-gcd-of-two-numbers/",
	"https://takeuforward.org/maths/check-if-a-number-is-armstrong-number-or-not/",
	"https://takeuforward.org/data-structure/print-all-divisors-of-a-given-number/",
	"https://takeuforward.org/data-structure/check-if-a-number-is-prime-or-not/"]

recursion =[
	"https://takeuforward.org/recursion/print-name-n-times-using-recursion/",
	"https://takeuforward.org/recursion/print-1-to-n-using-recursion/",
	"https://takeuforward.org/recursion/print-n-to-1-using-recursion/",
	"https://takeuforward.org/data-structure/sum-of-first-n-natural-numbers/",
	"https://takeuforward.org/data-structure/factorial-of-a-number-iterative-and-recursive/",
	"https://takeuforward.org/data-structure/reverse-a-given-array/",
	"https://takeuforward.org/data-structure/check-if-the-given-string-is-palindrome-or-not/",
	"https://takeuforward.org/arrays/print-fibonacci-series-up-to-nth-term/"]

hashing = [
	"https://takeuforward.org/data-structure/count-frequency-of-each-element-in-the-array/",
	"https://takeuforward.org/arrays/find-the-highest-lowest-frequency-element/"]

sorting = [
	"https://takeuforward.org/sorting/selection-sort-algorithm/",
	"https://takeuforward.org/data-structure/bubble-sort-algorithm/",
	"https://takeuforward.org/data-structure/insertion-sort-algorithm/",
	"https://takeuforward.org/data-structure/merge-sort-algorithm/",
	"https://takeuforward.org/arrays/recursive-bubble-sort-algorithm/",
	"https://takeuforward.org/arrays/recursive-insertion-sort-algorithm/",
	"https://takeuforward.org/data-structure/quick-sort-algorithm/"
]
easyArrays = [
	"https://takeuforward.org/data-structure/find-the-largest-element-in-an-array/",
	"https://takeuforward.org/data-structure/find-second-smallest-and-second-largest-element-in-an-array/",
	"https://takeuforward.org/data-structure/check-if-an-array-is-sorted/",
	"https://takeuforward.org/data-structure/remove-duplicates-in-place-from-sorted-array/",
	"https://takeuforward.org/data-structure/left-rotate-the-array-by-one/",
	"https://takeuforward.org/data-structure/rotate-array-by-k-elements/",
	"https://takeuforward.org/data-structure/move-all-zeros-to-the-end-of-the-array/",
	"https://takeuforward.org/data-structure/linear-search-in-c/",
	"https://takeuforward.org/data-structure/union-of-two-sorted-arrays/",
	"https://takeuforward.org/arrays/find-the-missing-number-in-an-array/",
	"https://takeuforward.org/data-structure/count-maximum-consecutive-ones-in-the-array/",
	"https://takeuforward.org/arrays/find-the-number-that-appears-once-and-the-other-numbers-twice/",
	"https://takeuforward.org/data-structure/longest-subarray-with-given-sum-k/",
	"https://takeuforward.org/arrays/longest-subarray-with-sum-k-postives-and-negatives/"]

mediumArrays =[
	"https://takeuforward.org/data-structure/two-sum-check-if-a-pair-with-given-sum-exists-in-array/",
	"https://takeuforward.org/data-structure/sort-an-array-of-0s-1s-and-2s/",
	"https://takeuforward.org/data-structure/find-the-majority-element-that-occurs-more-than-n-2-times/",
	"https://takeuforward.org/data-structure/kadanes-algorithm-maximum-subarray-sum-in-an-array/",
	"https://takeuforward.org/data-structure/kadanes-algorithm-maximum-subarray-sum-in-an-array/",
    "https://takeuforward.org/data-structure/stock-buy-and-sell",
    "https://takeuforward.org/arrays/rearrange-array-elements-by-sign",
    "https://takeuforward.org/data-structure/next_permutation-find-next-lexicographically-greater-permutation",
    "https://takeuforward.org/data-structure/leaders-in-an-array",
    "https://takeuforward.org/data-structure/longest-consecutive-sequence-in-an-array",
    "https://takeuforward.org/arrays/count-subarray-sum-equals-k",
    "https://takeuforward.org/data-structure/spiral-traversal-of-matrix"]

modules = [
	basicMaths,
	recursion,
	hashing,
    sorting,
	easyArrays,
    mediumArrays
]

def main():
    print(random.randint(1,22), patterns)
    for i in modules:
        print(random.choice(i))

if __name__ == "__main__":
    main()
# 1 ['https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/']
# https://takeuforward.org/data-structure/print-all-divisors-of-a-given-number/
# https://takeuforward.org/data-structure/check-if-the-given-string-is-palindrome-or-not/
# https://takeuforward.org/data-structure/count-frequency-of-each-element-in-the-array/
# https://takeuforward.org/data-structure/quick-sort-algorithm/
# https://takeuforward.org/data-structure/find-second-smallest-and-second-largest-element-in-an-array/
# https://takeuforward.org/data-structure/kadanes-algorithm-maximum-subarray-sum-in-an-array/