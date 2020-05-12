---
layout: post
title: "An Introduction to Markov Chains"
date: 2014-06-07
tags: [Statistics, Markov-chains]
---

Markov chains are a statistical tool invented by Andrey Markov to model dependent statistical phenomenon. A Markov Chain is made from two components a discrete set of states and a set of stochastic state transitions. The idea is that if there are two states **A** and **B** and the state transitions **AA**, **AB**, **BA** and **BB** where the first letter is the starting state and the second letter is the final state, each one of these state transitions will have a probability of occurring associated with it. To compute this process an initial state is selected, then one of the valid state transitions is randomly chosen based on its probability of occurring, the current state is replaced by the new state as determined by the transition. This process now is a model of a system where the probability of the states **A** or **B** occurring is dependent on the current state.

The example given was quite simple and would not show much complexity, but it is possible to extend a Markov Chain to model more complex systems. If the state transitions of a Markov Chain where to take into account more than the most recent state. Then the chain could model more complexity system. Using the same example as before if an initial sequence of two states where chosen and the state transitions where replaced by the new set of transitions; **AAA**, **AAB**, **ABA**, **ABB**, **BAA**, **BAB**, **BBA** and **BBB** then this process could model more complicated systems. So the complexity of the resulting sequence is determined by the number of previous states accounted for in the state transitions, this is called the order of the Markov Chain. The first example was a first order chain, the second was a second order chain. So the simplest Markov Chain is a zeroth order chain where none of the previous states are taken into account and the probability of a state is equal regardless of what came before.

To demonstrate how the complexity of a Markov chain is related to the order of the chain I wrote a program to generate Markov chains. This program uses all of the lower case letters in the English alphabet and the space and period characters as states of the system. A set of state transitions is generated from the text supplied to the program, then the program generates a string of characters using the state transitions and an initial state. For this example I used some of the books and collections of stories written by H. G. Wells including; *The First Men in the Moon*, *The Island of Doctor Moreau*, *The Time Machine*, *The War of The Worlds*, and *The Food of The Gods and How it came to Earth*. These books were downloaded for free from the [Gutenberg Project](http://www.gutenberg.org/).

After running four tests using zeroth, first, second and fifth order Markov chains the resulting text output was as follows. The zeroth order Markov chain produced the text,

> icehciotsi b n o e ble plwdenvehtp axeuiod a oeoht a ue utf u mmn aauuea rptge tn hd mo ehd. hial aald.ued p rliuryudwfoepulc .aoyvnhimwomo m e aeaiyofeof rtah i ode rar yk otss ogtghhdglawmeet e hreetcoedd a ms.r u ochcirp e rodihfrca whocroegglnneeos .sahr hwi ttliepcn liso mou tdn eaaoaifeno.fkeeoeaaii f nl t eh s eil a tblanlo ahseuefeuor tomgtsivhesnrdh yoeiate edwotd hpoago uha been rafey.l wl yh oeebaumdihlouctrtos afcso th rkgpttwgnsneeerai inhreeh nneenh pifee

In this sample text the characters appear at a frequency that is consistent with the books written by H. G. Wells, but it looks nothing like English and has no structure. The first order Markov chain produces the text,

> atht gsond sly ig. of tiroveratustu tl s as thengrd wif ly by s . thoulel s therdad coaneree ithend cthe i ct w ltr agar mathe f ot ds o abos sor ild witlf ano wit ovesth he the trhercange acuang bof thed intos. hroge ayenxther o st bera wisem lyotherictouringa og ve bevuledrsers f creled. t bowhe woruan wead tind mm sury blay her qut k the frk theye ananererol tongheatracon wit impulacotre basoubyngereasthe ir apawain aikls ld evevelny iseee tiloved athap histhaneg ime ffatenacte waf t ve thu

This text still does not look like English, but the Markov chain is starting to produce some digraphs that are common to the English language. The second order Markov chain produces the text,

> as turn the selted thavere led buse clisely daw an. yelivertyfor full begaidebroblaming mattle ber dark of havou. thatintliver her sand abot he shore sund tows i. to hunnouse. i doneou attless any dissittely a monse. and ungsto mand he iten thery sper obweed wit ang ups at cord frome ingethick of fract win th mulf hown selpeople th budd old. he the dance go to rome. to hemand bitiough thin had. talf therses vand thanceenes on threat at sidido ift lon othe re he sudden mysta must couccum.

The second order Markov chain is starting to produce some words and produce some basic structure such as ensuring that periods are followed by spaces. Finally the fifth order Markov chain produces the text,

> as i have died a snakes already to freedom of desire beginning until so furniture staghound with people in it. . . they would heap of human by readingrejoicing done bogota that the fit to answer to and knew to carried to me strange orchid. its what all was dying and more that said. why the explanation absolutely up their eyes for us. graham was unaccustomersfor sheds it a being course was impossibilities and whistle and probably free other in the opposition but of the sunlightfall over i thing

This text is clearly unintelligible but at first glance it looks like English, also the trend of the text from the zeroth order to the fifth order chain appears to indicate that the order of the chain is directly related to the complexity of the Markov chain and its ability to mimic complicated systems such as the English language.
