# Vocabulary

A script that forms a well formatted WhatsApp message for vocabulary. This message is copied to the clipboard which can be sent to a Vocabulary group created among your friends.

Current working version is version 3.

The input to the script is 7 lines

* **Example**

1

example

egzaampala

Something that represents a whole.

udaaharana

example rhymes with SAMPLE

Our Science teacher gives good real life examples to explain the concept.

* **Output**

\*1. example\*

\*Pronounciation:\*
एग्ज़ाम्पल

\*Definition:\*
Something that represents a whole.

\*Self Definition:\*
उदाहरन

\*Mnemonic:\*
example rhymes with SAMPLE

\*Example Sentence:\*
Our Science teacher gives good real life examples to explain the concept.

* **Output in WhatsApp**

**1. example**

**Pronounciation:**
एग्ज़ाम्पल

**Definition:**
Something that represents a whole.

**Self Definition:**
उदाहरन

**Mnemonic:**
example rhymes with SAMPLE

**Example Sentence:**
Our Science teacher gives good real life examples to explain the concept.

* **Meaning of the inputs**

1st input is word count which can be any number

2nd input is the word

3rd input is the pronounciation which would be converted to Devanagari script*

4th input is the short meaning of the word

5th input is the Hindi meaning of the word which would be converted to Devanagari script*

6th input is the mnemonic to remember the word

7th input is the example sentence.


\* The mapping from English to Devanagari script can be found in https://github.com/AdityaShenoy/Vocabulary/blob/master/version3/eng_to_hin_map.txt

* **Previous works**

In the previous versions I tried to automatically scrape the meanings of the word recursively to create the whole dictionary in the format we want. The format in the source website was very hard to generalize for all words so went with manual approach.
