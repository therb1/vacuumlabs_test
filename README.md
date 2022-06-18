# Childspeak
My little daughter is learning how to talk. Talking is a hard challenge though. Especially the consonants give her a hard time! Therefore, she creates her own childspeak. After some time, we started to notice some rules of it:

- She uses exactly one unique consonant in the word—​once she comes to the first consonants, she replaces all the subsequent consonants with the first one. Example: instead of "mapa", she says "mama".
- If the word starts with a vowel, she puts the first consonant to the very beginning, so instead of "alibaba" she says "lalilala".
- If there is a group of consecutive consonants, she replaces the whole group with just a single consonant. For example instead of "lampa", she says "lala", instead of "bratislava' she says "babibaba".
- If there is a group of consecutive vowels, she replaces that group with the last vowel from the group. So instead of "naomi" she says "noni", instead of "aikido" she says "kikiko" ("ai" was replaced by "i" and prepended by "k", because of the 2nd rule)
- She ignores all the consonants after the last vowel, so instead of "ahoj" she says "haho".

Understanding such a childspeak is a demanding task, especially because many words' pronunciation is the same.

In this task, you’ll be given a dictionary of all the words that matter. Your job is for each word to calculate, how many other words (from the same dictionary) have the same pronunciation in my daughter’s childspeak.

The input contains the dictionary, one word per line. For every word, produce a `word n` line in the output file, where `n` is a number of words from the dictionary having the same pronunciation as `word`.
Alternatively, you can use a JSON input file with an array of words.

You can assume, that the dictionary has less than 100,000 words. It consists only of lowercase words, using the 26-letter English alphabet: "abcdefghijklmnopqrstuvwxyz". You can also assume that each word in the dictionary contains at least one consonant and one of the vowels: "aeiouy".

Sample input:

```commandline
mapa
island
lampa
lajdak
alan
mama
```

Sample output:
```commandline
mapa 1
island 0
lampa 2
lajdak 2
alan 2
mama 1
```

Explanation: "mama" and "mapa" both pronounce as "mama", for each of these words, there is exactly one other word with the same pronunciation. Similarly, "lampa", "lajdak" and "alan" have the same pronunciation. Finally, there is no other word in a dictionary with a pronunciation such as "island".