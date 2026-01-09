"""
================================================================================
TIME & SPACE COMPLEXITY – DEEP REVISION NOTES (CONVERSATIONAL STYLE)
================================================================================

Think of Time Complexity as:
👉 "How does the running time of an algorithm grow when input size grows?"

Think of Space Complexity as:
👉 "How much extra memory does an algorithm need as input size grows?"

IMPORTANT:
We do NOT calculate exact seconds or memory in MB.
We analyze GROWTH PATTERNS.

--------------------------------------------------------------------------------
WHY COMPLEXITY MATTERS (REAL TALK)
--------------------------------------------------------------------------------
Imagine you wrote a program that works perfectly for 10 inputs,
but crashes or becomes slow for 1,00,000 inputs.

In interviews and real systems:
✔ Fast code
✔ Memory-efficient code
✔ Scalable code

= Good engineer.

Complexity analysis helps us compare algorithms BEFORE running them.

--------------------------------------------------------------------------------
TIME COMPLEXITY (TC)
--------------------------------------------------------------------------------

Time Complexity describes:
How many basic operations an algorithm performs as input size (n) increases.

We express it using:
BIG-O NOTATION → O(...)

Big-O focuses on:
✔ Worst case
✔ Upper bound
✔ Growth trend (not exact count)

--------------------------------------------------------------------------------
COMMON TIME COMPLEXITIES (FROM BEST TO WORST)
--------------------------------------------------------------------------------

O(1)     → Constant Time
O(log n) → Logarithmic Time
O(n)     → Linear Time
O(n log n)
O(n^2)   → Quadratic Time
O(2^n)   → Exponential Time
O(n!)    → Factorial Time (danger zone ☠️)

--------------------------------------------------------------------------------
O(1) – CONSTANT TIME
--------------------------------------------------------------------------------
No matter how big input becomes, time stays the same.

Example:
Accessing an array element by index.

Key thought:
"Input size changes, but number of steps does not."

--------------------------------------------------------------------------------
O(log n) – LOGARITHMIC TIME
--------------------------------------------------------------------------------
Input size reduces by half every step.

Classic example:
Binary Search

Mental model:
You are dividing the problem repeatedly.

log₂(8) = 3 → Only 3 steps needed.

Very efficient for large inputs.

--------------------------------------------------------------------------------
O(n) – LINEAR TIME
--------------------------------------------------------------------------------
Time grows directly with input size.

Example:
Looping through an array once.

If n doubles → time doubles.

Very common and acceptable.

--------------------------------------------------------------------------------
O(n log n)
--------------------------------------------------------------------------------
Combination of:
✔ Divide (log n)
✔ Process each element (n)

Examples:
Merge Sort
Quick Sort (average case)

This is usually the BEST possible for sorting.

--------------------------------------------------------------------------------
O(n²) – QUADRATIC TIME
--------------------------------------------------------------------------------
Nested loops.

Example:
Comparing every element with every other element.

If n = 1000 → operations ≈ 1,000,000

⚠️ Dangerous for large inputs.

--------------------------------------------------------------------------------
O(2ⁿ) & O(n!)
--------------------------------------------------------------------------------
Exponential and factorial growth.

Examples:
Brute force recursion
Generating all subsets / permutations

Works only for VERY small inputs.

Avoid unless constraints are tiny.

--------------------------------------------------------------------------------
IMPORTANT INTERVIEW RULES (TIME COMPLEXITY)
--------------------------------------------------------------------------------
1. Drop constants
   O(2n) → O(n)

2. Drop lower order terms
   O(n² + n) → O(n²)

3. Focus on worst case unless specified

--------------------------------------------------------------------------------
SPACE COMPLEXITY (SC)
--------------------------------------------------------------------------------

Space Complexity measures:
✔ Extra memory used by algorithm
✔ NOT input storage
✔ NOT output storage (usually)

Includes:
✔ Variables
✔ Data structures
✔ Recursion stack

--------------------------------------------------------------------------------
O(1) SPACE – CONSTANT SPACE
--------------------------------------------------------------------------------
Uses fixed amount of memory.

Example:
Using few variables regardless of input size.

Best possible.

--------------------------------------------------------------------------------
O(n) SPACE – LINEAR SPACE
--------------------------------------------------------------------------------
Memory grows with input size.

Examples:
Extra array
HashMap
List storing n elements

--------------------------------------------------------------------------------
RECURSION & SPACE COMPLEXITY
--------------------------------------------------------------------------------
Each recursive call consumes stack memory.

Example:
Recursive function called n times → O(n) space

Important interview trap:
Even if no extra data structure is used,
recursion STILL uses space.

--------------------------------------------------------------------------------
IN-PLACE ALGORITHMS
--------------------------------------------------------------------------------
Algorithms that use:
✔ O(1) extra space

Example:
Two-pointer techniques
Swapping elements inside array

Highly valued in interviews.

--------------------------------------------------------------------------------
TIME vs SPACE TRADE-OFF
--------------------------------------------------------------------------------
You can:
✔ Use more memory to save time
✔ Use more time to save memory

Example:
Hashing improves time but increases space.

Good engineers choose balance based on problem constraints.

--------------------------------------------------------------------------------
HOW TO ANALYZE COMPLEXITY IN INTERVIEWS
--------------------------------------------------------------------------------
1. Look for loops → Time
2. Nested loops → Multiply
3. Recursion → Draw recursion tree
4. Data structures → Space
5. Ask constraints before optimizing

--------------------------------------------------------------------------------
FINAL MINDSET
--------------------------------------------------------------------------------
✔ Don't memorize blindly
✔ Understand growth patterns
✔ Practice explaining aloud
✔ Think like input size = 1,00,000+

If your algorithm survives that,
it's probably good.

================================================================================
END OF REVISION NOTES
================================================================================
"""
