---
layout: post
title: "The Making of a Markov Chain"
date: 2014-07-19
tags: [Statistics, Markov-chains, Python]
---

Before getting into how to make Markov Chains, lets quickly get a refresh on what a Markov Chain is. A Markov Chain is a set of states and state transition which are selected based on an assigned probability of occurring. The goal of a Markov chain is to model complex dependent statistical systems, for an in-depth introduction to Markov Chains see the post [An Introduction to Markov Chains]({% post_url 2014-06-07-an-introduction-to-markov-chains %}).

The goal of this project is to generate text that approximates the statistical properties of written English text, and to build the text using a Markov Chain working on individual character. For this project I will be using the Python programming language. If you are unfamiliar with Python you can checkout [Python.org](https://www.python.org/) for more information.

The program will operate in three steps. First, load text to analyze, and perform some initial formatting. Second, step through the formatted text and enumerate the occurrences of each n-gram. Once all n-gram have been counted the frequencies are normalized. Third, an initial seed n-gram is used to start the Markov Chain, and a string of text is generated and returned.

The following pseudocode describes how the Markov Chains will be generated, and how the text is produced from them.

{% highlight python %}
gentext(n)
    #n is the order of the Markov chain
    #white list the allowed characters 
    chars = ['a', 'b', 'c', ...]

    #create transition array, it should have
    #n dimensions, with each dimension having
    #an index for each of the characters in
    #the list chars. The array should be
    #initialized to zeros
    transition = [len(chars)]...[len(chars)]

    #read raw text from file
    raw_text = load("file.txt")

    #apply any required formatting
    text = format_text(raw_text)

    #count occurrences of each n-gram
    for i in (0, len(text) - (n - 1))
        n-gram = text[i:i + n]
        #map n-gram to an index in the array 
        #transitions
        indices = index(n-gram)
        transition[indices] += 1

    transition = normalize(transitions)
    seed = "..." #some seed text
    length = 100 #length of the final output
    output = seed
    while(len(output) < length)
        #get the last n - 1 characters from
        #the output
        context = output[-(n - 1):]
        indices = index(context)
        #select the next character and
        #append to output
        output += choose(chars, transition[indices])
    return output

normalize(array)
    if is_array(array)
        for sub_array in array
            sub_array = normalize(sub_array)
    else
        #total number of counts for n-grams
        #with the same first n - 1 characters
        sum = sum(array)
        if sum != 0
            for element in array
                element /= sum

choose(chars, array)
    #get a random float in the range [0, 1)
    X = rand(0,1)
    x = 0.0
    #find the char that Corresponds to X
    for char, value in (chars, array)
        x += value
        if X < x
            return char
{% endhighlight %}

The full python source code is available at the GitHub repository [Iprocess-Projects: TextGen v1.1](https://github.com/lsiemens/iprocess-projects/tree/master/TextGen_1.1).

Overall this first version is working. Currently the maximum value I can use for the order of the Markov Chain is 5, any thing larger and the algorithm tries to allocate more memory than is installed on my computer. But even with only a fifth order Markov Chain the program is able to produce text where the majority of the works are spelled correctly. For example I trained the algorithm on the book "The Mysterious Island" by Jules Verne, an excerpt from the output of the algorithm is as follows.

> times the heart in inflated himself in pencroft nodded to passed that blockhouse pronounced and it. that was not a satisfactor to granite house. they would care oven found damp. the larged. think anything continued. they had nothing the safety. this matter whether ladder. the interval being built by the ruffian. never rested to the he handling on the more cover anything to abandoning several or navigated by a more sprang for this left thus subjectglassmaker side. he west was convey it was still it had extract on ayrton. in the engineer having and the explorers like a sort of new landing his simply for and inspect heights of granite house an appearing centrance which reflection of the nature it even days set of falls the could not have notto the roast time the island had received by a few crater hand for design was soon apparent. its privation. they had not exclaiming magnificent. yes and industry.

Although with low order chains there is almost no relation between the individual words, still the Markov Chain produces text with the same vocabulary as the original even though each character in the text is randomly chosen. And if the order of the Markov Chain could be increased then it could possibly produce legible sentences and readable text, but that would require a major reduction in memory usage. For now it is limited to producing words.
