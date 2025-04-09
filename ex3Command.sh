who -a > who_is_logged.txt
echo "The answer is 24" > fact.txt
cat who_is_logged.txt >> fact.txt
grep "Alice" alice.txt
grep -ci "Why" alice.txt
grep "^CHAPTER" alice.txt > chapters.txt
cat alice.txt | tr 'e' 'o'
nl alice.txt | grep "Alice" > numbered_alice.txt
grep -v 'fear' alice.txt | grep -v 'rabbit'
grep '*' alice.txt | sort | uniq


