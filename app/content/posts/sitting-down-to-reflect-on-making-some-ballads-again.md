title: Sitting Down to Reflect on Making Some Ballads Again
date: 01 January 2015
tags:
- shakespeare
- early-modern-literature
- ballads
- markov-chains
- python
- flask

Last semester I took a seminar on the materiality of early modern English books. I’m a Victorianist, but I was drawn to the course by the promise of spending lots of time in the Rare Book and Manuscript library.

Our main focus in the seminar was on the ways Shakespeare’s plays and early modern ballads interact: how Shakespeare’s plays rely upon, use, and remediate ballads and how ballads rely upon, use, and remediate Shakespeare’s plays. As a class, we developed our own ballad adaptations of Shakespeare’s plays in order to explore some aspect of the materiality remediation. For my project, I wrote a web app, [Balladmonger](http://balladmonger.kylerjohnston.com), which generates ballads based on the text of *King Lear* and its remediations&mdash;texts that influenced it or that it influenced.

My initial purpose for the project was threefold. First, *Balladmonger* literally re-mediates (puts into a new medium) words and phrases lifted directly from some other work. But can we call the texts *Balladmonger* produces a “remediation” of that work? Can we call a semi-random collection of words and phrases from *King Lear* a version of *King Lear*? It’s an ontological question about what a play or a ballad or a text is. What relation does text as such, stripped of context, have to “the text” of *Lear*?

I was also interested in engaging with the performative aspect of early modern plays and ballads and the performative aspect of *reading* plays and ballads. That’s why I have *Balladmonger* generate the poems dynamically each time a user visits the site, rather than archiving them to a blog or something: it’s my attempt to translate the perceived “immediacy,” “presence,” and singularity of watching and listening to a performance of a ballad or a play into a digital, web-native aesthetic object. When you navigate away from the page, the ballad is gone forever. 

In addition to remediating performance as such, this ephemeralizing behavior also puts the reader in a powerful position that breaks down an opposition between producer and consumer: the reader controls when a new ballad will be created and when a ballad will vanish into the aether of the internet. If the reader wants to preserve a poem, it’s their responsibility to copy and paste it&mdash;and remediate it&mdash;into a Tumblr post or whatever. This calls attention not only to the power of reading as such&mdash;readers’ power to make meaning from any text&mdash;but also to the social and communal aspects of reading specific to early modern ballad transmission and production. Margaret Spufford, in [*Small Books and Pleasant Histories*](https://books.google.com/books?id=KEjQvnsbgUcC&lpg=PP1&dq=small%20books%20and%20pleasant%20histories%20spufford&pg=PP1#v=onepage&q=small%20books%20and%20pleasant%20histories%20spufford&f=false), describes the case of the eighteenth-century ballad singer Anna Gordon who recited ballads she had learned from her aunt as a child, ballads which she “recreated afresh on each occasion she sang them. She had no concept of fidelity to one text or to one set of words; she remade her ballads afresh, changing characters, words and even rhymes and sounds, yet retaining fidelity to the story” (13). Gordon’s ballad singing practices destabilize textual authority in much the same way as *Balladmonger*. Gordon is at once a producer and consumer of texts, generating new texts with new meanings from a collage-like assemblage of older texts, new texts which can then be recombined and remediated in turn by a new set of readers. It’s a model that makes “authority,” in the sense of authorship, seem like an outmoded concept.


What coding tells us about the process of remediation
----------------------------------------------------------------

Writing a program to create digital poems out of digital versions of seventeenth-, eighteenth-, nineteenth, twentieth-, and twenty-first-century texts turns out to be a really effective way of to understand the material process of remedation. A program is a series of explicit instructions for actions a computer must take: the choices you make as a programmer in designing this kind of program define both the to-be-remediated object and the final post-remediation object. This is not as simple as it sounds: you can’t just tell the computer to turn *King Lear* into a poem. The computer doesn’t know what *King Lear* or plays or poems or words are: you have to define those things&mdash;and define them in terms a computer can understand, i.e. very specifically, with explicit limitations. Computers don’t do ambiguity. This same problem, the problem of defining limits, seems to be behind the difficulties many scholars, such as [Patricia Fumerton](https://books.google.com/books?id=aXX8dev1xj0C&lpg=PA22&dq=studies%20in%20ephemera%20patricia%20fumerton&pg=PA55#v=onepage&q&f=false) and [Diana Kichuk](http://llc.oxfordjournals.org/content/22/3/291.abstract), have written about in regards to large-scale digital archival projects like [Early English Books Online](http://eebo.chadwyck.com/home) and [the English Broadside Ballad Archive](http://ebba.english.ucsb.edu).

The first thing *Balladmonger* does is “clean” the training texts by removing things like chapter headings, running titles, page numbers, front and end matter, subtitle metadata, and speaker indicators in drama. One way to think about these things is as a kind of metadata, surplus information which helps us to make sense of but is ultimately extraneous to our data, “the text” as such. Indeed, that way of thinking has been one common (and dominant) trend in literary studies in the twentieth century, and that’s also how you have to think of those things in order to write this kind of program: I had to make *Balladmonger* discard the extraneous “stuff” in order to get at the text I want. As book historians would remind us, though, these things&mdash;chapter headings, running titles, front and end matter and the like&mdash;are all key components of the meaning-making process when a reader reads a book, shaping readers’ expectations of the text and signifying where it sits generically, geographically, socially, and politically. These components are also integrally bound to their media. Running titles and page numbers signify print, just as hyperlinks signify digital media. In effect, *Balladmonger* can only work by erasing all signifiers of previous mediation in the text, but this also effaces all of the meaning bound up with those signifiers and those media. *Balladmonger* draws its text from twenty-six sources. The generic, social, historical, and political difference of these source texts, texts which range in publication date from the seventeenth through the twenty-first centuries, if effaced; they all blend together to signify a new social, historical, political, and generic reality.

While *Balladmonger* masks the signs of its source texts’ previous mediations and locates itself in a new social reality, it still succeeds&mdash;I think, at least&mdash;in capturing the ephemeral qualities of early modern ballads and their coinciding decentering of authorship. Reading the ballads&mdash;both early modern and the ones produced by *Balladmonger*&mdash;is a unique interpretive task. *Balladmonger*’s ballads almost read like modernist poetry: adjacent fractured images; the gravitational significance of the randomly chosen “woodcut” image; certain lines&mdash;lines you’re familiar with, lines that will differ for each individual reader&mdash;demand you recall aspects of their former works. From all this jumbled mess the reader has to construct some sort of narrative, to make some sort of unifying sense, just as Anna Gordon made new sense out of her patchwork ballads.