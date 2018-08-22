Most Common Sequences Finder Thingy
===================================

Crash Course
------------
Outputs the 100 most common three-word sequences in the text, along with a count of how many times each occurred in the text. The program ignores punctuation, line endings, and is case insensitive.

Usage
-----
The script accepts input from either stdin or as a list of arguments:

`cat some-utf-8-encoded-textfile.txt | ./most_common_sequences.py`

OR

`./most_common_sequences.py some-file.txt another-file.txt`

Environment
-----------
1) Clone the repository:

<pre><code>$ git clone https://github.com/kaewarren/most-common-sequences.git</code></pre>

2) Create and activate a virtual environment in the same directory: 

<pre><code>$ pip install virtualenv
$ virtualenv env
$ source env/bin/activate 
</code></pre>

3) Install the required packages using pip:

<pre><code>(env)$ pip install -r requirements.txt
</code></pre>
