title: "The pleasure of the TXT: Why humanists should ditch Word"
date: 15 February 2016
tags:
- academia
- humanities
- writing
- vim

Microsoft Word is the de facto standard application for writing in the humanities. We write, collaborate, and disseminate our works in `.docx` format. There are lots of things I dislike about Word: its lack of portability, for one, and how it forces you to be tied into the Microsoft ecosystem, or how easily the formatting of an entire document can get messed up by dropping in a single figure or table. The biggest problem with Word, though, is that it just doesn’t match up with the way we write. Writing and typesetting are different, distinct parts of the writing process, but in Word they are combined into one task. As we write we must also always be formatting, thinking not just about our words but about how they will appear on the paper. We fiddle with fonts and line spacing and ligatures when we should be getting down words.

This is a really *weird* writing ecosystem. For years our colleagues on the opposite side of campus&mdash;the scientists and the engineers and the mathematicians&mdash;have been typesetting their papers using a free program called [LaTeX](https://en.wikipedia.org/wiki/LaTeX). LaTeX is a markup language---like HTML---that lets you write your papers in plain text files that you can edit with any text editor. Then, when you’re done writing, you can typeset document into any number of nice-looking templates that you can proofread and send off to review in any number of formats. This makes it really easy to quickly produce differently formatted versions of your paper: a version to turn into your seminar professor, a version to submit to journals, a version to post on your blog, whatever. LaTeX is especially good at typesetting complex-looking mathematical expressions that are beyond the scope of Word’s formatting capabilities, which is why it’s so popular with the STEM crowd. We don’t generally need mathematical expressions in the humanities, but we can learn a lot from this compose first, then format ecosystem.

LaTeX is overkill for most of what we write in the humanities. LaTeX is great if you want to typset complex-looking mathematical equations---that’s why  STEM people love it---but its syntax is overly complex the kinds of things we typically write in the humanities. Instead, we can write in the simpler [Markdown](https://daringfireball.net/projects/markdown/syntax) markup language and save our documents as plain text files. Even if you’ve never heard the term “Markdown,” you probably recognize its syntax from emails or internet message board posts: a word or phrase wrapped in `*single asterisks*` is *italicized*; `**double asterisks**` make text **bold**. You can find a more detailed guide to the syntax elsewhere, but realistically you probably won’t be using too much beyond what I just demonstrated in your humanities papers.

How I write
-----------

For the rest of this post, I’m going to describe my particular set up for writing in the humanities. I write *everything* in Markdown---from seminar papers and syllabi to lesson plans, notes, and this blog post---and rely on the powerful [Pandoc](http://pandoc.org) utility to convert my Markdown files into formatted documents---mostly PDFs and HTML files.

### Prerequisites

I write on a mid-2012 Macbook Pro. My instructions below are specific to OS X, but all of the tools I mention are cross-platform and a similar set up could be configured on any system.

* **A plain text editor**. This can be something as simple as TextEdit on a Mac or Notepad on Windows. There are also, at least for OS X, several editors made specifically for editing markdown and targeted at writers, such as ByWord, iA Writer, and WriteRoom. If you don’t write code, these might be your best bets---I’ve had good results with ByWord in the past. More advanced options like Atom, Sublime Text, Emacs, and Vim will be more customizable and support advanced features like syntax highlighting and autocompletion.  I use Vim and MacVim. I’ll give some tips on making Vim work well with prose writing below, but you should feel free to try out several editors---Vim has a steep (but rewarding!) learning curve, and you should use whatever editor works best for you.

* **Pandoc**. [Pandoc](http://pandoc.org) is a utility that can convert Markdown documents to basically any other format you want. 

* **A LaTeX installation**. Pandoc needs a LaTeX installation to convert your files to PDFs. If you’re on OS X, [MacTeX](http://tug.org/mactex/) is what you want. The BasicTex package will suffice, but I’d recommend installing the [TeX Live Utility](http://amaxwell.github.io/tlutility/) too if you go that route (it’s included with the full MacTeX package). After installing your TeX package, open the TeX Live Utility and update all packages.
