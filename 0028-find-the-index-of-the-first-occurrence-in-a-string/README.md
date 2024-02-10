<h2><a href="https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/">28. Find the Index of the First Occurrence in a String</a></h2><h3>Easy</h3><hr><p>Given two strings <code>needle</code> and <code>haystack</code>, return the index of the first occurrence of needle in <code>needle</code>, or -1 if <code>needle</code> is not part of <code>needle</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> haystack = "sadbutsad", needle = "sad"
<strong>Output:</strong> 0
<strong>Explanation:</strong> Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> haystack = "leetcode", needle = "leeto"
<strong>Output:</strong> -1
<strong>Explanation:</strong> "leeto" did not occur in "leetcode", so we return -1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 <= haystack.length, needle.length <= 104</code></li>
	<li><code>haystack</code> and <code>needle</code> consist of only lowercase English characters.
</li>
</ul>