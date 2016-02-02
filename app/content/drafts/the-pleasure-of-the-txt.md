title: "The pleasure of the TXT: Why humanists should ditch Word"
date: 30 January 2016
tags:
- academia
- humanities
- writing
- vim

Microsoft Word is the de facto standard application for writing in the humanities. We write, collaborate, and disseminate our works in `.docx` format. There are lots of things I dislike about Word: its lack of portability, for one, and how it forces you to be tied into the Microsoft ecosystem, especially now that Office works on a subscription model and my subscription is going to end once I end my affiliation with my university; its unnecessary bloat that still manages to *lack* the functionality I need (have you ever used one of Word’s default templates?); how easily the whole formatting of a document can get messed up by dropping in a single figure or table (have you ever had to copy and paste a whole Word document into a new document to fix broken formatting?). The biggest problem with Word, though, is that it just doesn’t match up with the way we write. Drafting, editing, and typesetting are all different, distinct parts of the writing process, but in Word they are all combined into one task. As we write we must also always be formatting, thinking not just about our words but about how they will appear on the paper. We fiddle with fonts and line spacing and ligatures when we should be getting down words.

This is a really *weird* writing ecosystem. For years our colleagues on the opposite side of campus&mdash;the scientists and the engineers and the mathematicians&mdash;have been typesetting their papers using a free program called [LaTeX](https://latex-project.org). LaTeX lets you write your papers in plain text files that you can edit with any text editor and then, when you’re done writing, typeset the plain text file into a nice-looking document that you can proofread and send off to review in any number of formats. LaTeX is especially good at typesetting complex-looking mathematical expressions that are beyond the scope of Word’s formatting capabilities, which is why it’s so popular with the STEM crowd. We don’t generally need mathematical expressions in the humanities, but we can learn a lot from this compose first, then format ecosystem.

LaTeX is overkill for most of what we write in the humanities. Instead, we can write in the simpler [Markdown](https://daringfireball.net/projects/markdown/syntax) markup language and save our documents as plain text files. Even if you’ve never heard the term “Markdown,” you probably recognize its syntax from emails or internet message board posts: a word or phrase wrapped in `*single asterisks*` is *italicized*; `**double asterisks**` make text **bold**. You can find a more detailed guide to the syntax elsewhere, but realistically you shouldn’t be using too much beyond just plain text words in your humanities papers.

How I write
-----------

The rest of this document will explain my particular setup for writing papers in plain text. It involves a lot of small components working together and at first may seem much more complicated than simply throwing a Word document together. If you’re only writing one paper, it *is* more complicated and it’s not worth your time. But if you’re an undergraduate or a grad student in the humanities&mdash;or even a researcher&mdash;, if you’re writing lots of papers and formatting them all the same way, or the same one or two ways, I guarantee you this set up, or one like it, will save you a lot of time (and prevent some headaches) in the long run.

### Prerequisites 

* **A plain text editor**. This can be something as simple as TextEdit on a Mac or Notepad on Windows. More advanced options like Atom, Sublime Text, Emacs, and vim will be more customizable and support advanced features like syntax highlighting and autocompletion. There are also, at least for OS X, several editors made specifically for editing markdown and targeted at writers, such as ByWord, iA Writer, and WriteRoom. For my particular needs, vim and MacVim work best. I’ll give some tips on making vim work well with prose writing below, but you should feel free to try out several editors&mdash;vim has a steep (but rewarding!) learning curve, and you should use whatever editor works best for you.

![Editing this post in markdown using MacVim]({{ url_for('static', filename='img/macvim_markdown.png') }})

* **Installations of LaTeX and pandoc**. 
