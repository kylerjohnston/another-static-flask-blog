title: "What makes a bestseller? Modeling literary prestige in the 19th and 20th centuries"
date: 08 February 2016
tags:
  - text-mining
  - literary-studies

For the last semester, I’ve been working as a research assistant for [Ted Underwood](http://tedunderwood.com) on a project aiming to model one form of literary prestige.[^novel] This is part of a larger project Ted has been working on along with another research assistant, Jordan Sellers. In a [blog post from May last year](http://tedunderwood.com/2015/05/18/how-quickly-do-literary-standards-change/) (and a forthcoming article in *MLQ*), Ted and Jordan ran a model on two samples of 19th-century poetry---one a sample of works which had been reviewed in prominent literary magazines, and one a sample of works randomly selected from the [HathiTrust Digital Library](http://hathitrust.org)---to see if the prestige of the reviewed volumes would be evident in the texts of the works themselves (spoiler: it is).

I’ve been working with Ted to construct a model that would predict whether or not a work of fiction would be a bestseller in the nineteenth and twentieth centuries. Andrew Piper has been doing [similar](http://txtlab.org/?p=596) [work](http://txtlab.org/?p=608) at McGill University. Is “bestsellerliness” a purely social feature, or something we can identify in a text? How stable are the textual features that predict bestsellerliness over time? Can the same features that predict bestsellerliness in 1840 predict bestsellerliness in 1900 and 1960?

To answer these questions, we first needed to build a sample of bestselling works of fiction in America from the nineteenth and twentieth centuries. For information on twentieth-century bestsellers, we relied on John Unsworth’s [20th-Century American Bestsellers database](http://unsworth.unet.brandeis.edu/courses/bestsellers/). While Unsworth gives us clean lists of the top ten bestsellers by year in the twentieth century, information on nineteenth-century bestsellers is less comprehensive. I drew from a list of works compiled by Jordan, who had selected titles based on their inclusion in bibliographies by Richard Altick, Q. D. Leavis, and Alice Payne Hackett.[^1] Hackett notes that for works published before 1895, data on total sales is scarce and unreliable, not only because the systematic recording of bestsellers had not yet begun but also because each book was issued by several publishers, many no longer in existence and with inaccurate or incomplete sales records (Hackett 221).[^2] As such, pre-1895 bestsellers are not rigorously defined, nor is it possible to compile a "top ten" per year. Rather, we get a sampling of works published across the century which were known to have sold well. Leavis chooses works which are "representative of the popular fiction" of their time (331). Hackett identifies pre-1895 bestsellers as works "which have without question sold a total of a million copies or more through the years" (221).  In sum, we need to bear in mind that our nineteenth-century sample is less comprehensive than our twentieth-century sample and that it represents a sample of well-known, popular works more than a sample of bestsellers.

We sampled bestsellers from two databases of texts: the HathiTrust Digital Library and [the Chicago Text Lab](https://lucian.uchicago.edu/blogs/literarynetworks/). For each bestseller, we also sampled a random volume from the same database, published in the same year, by an author who did not appear anywhere on our bestseller list. All together we sampled 1316 works of fiction from the nineteenth and twentieth centuries.

Modeling this sample we get the following plot:

![Figure 1. HathiTrust and Chicago Text Lab samples, 1800&ndash;1990]({{ url_for('static', filename='img/model-2-1.png') }})

In the plot above, the y-axis represents the probability that a work is a bestseller. Actual bestsellers are plotted in red dots; randomly sampled works are grey +s.

There are a couple interesting things going on in this plot. First of all, we see that our model is particularly good at predicting the bestsellerliness of works from the first half of the twentieth century. We also see a significant upward trend in bestsellerliness across both centuries. This seems to suggest not only that at least some of the same textual qualities that can predict whether or not something will be a bestseller in the early nineteenth century can also predict whether or not something will be a bestseller in the twentieth century, but that, over time, these features become more common in fiction. This could be evidence for a kind of literary natural selection.

We have to interpret this plot cautiously, though. There are some important differences in the datasets the works we're modeling come from that complicate our results. We relied on HathiTrust for our nineteenth-century works and the Chicago Text Lab for our twentieth-century works. HathiTrust has a wide range of texts, ranging from the very popular to the *very* obscure. Chicago has fewer obscure works---most things in Chicago, while not necessarily bestsellers, sold well enough. The trend we are seeing in this plot, then, is most likely a difference in the obscurity of texts we're modeling in the nineteenth and twentieth centuries: our twentieth century sample contains fewer obscure, more popular texts.

To test this interpretation, I modeled the Chicago Text Lab texts on their own:

![Figure 2. Chicago Text Lab sample, 1898&ndash;1990]({{ url_for('static', filename='img/chicago_only_whole_20thc.png') }})

When we model only works drawn from the Chicago Text Lab, we see a *reverse trend* from what we saw in our whole model. Over the course of the twentieth century, works tend to contain *fewer* of the features that would mark them as bestsellers. This is weird stuff! It suggests a definite stylistic shift over the course of the twentieth century; what's popular in 1990 would not have been as popular in 1900.

![Figure 3. Chicago Text Lab sample, 1898&ndash;1949]({{ url_for('static', filename='img/chicago1900-1949.png') }})

If we break our model down into smaller, half-century segments, we can still see the downward trend continuing over the first half of the twentieth century. (Also interestingly, the model seems to be better at predicting bestsellerliness after about 1920.)

![Figure 4. Chicago Text Lab sample, 1950&ndash;1990]({{ url_for('static', filename='img/chicago1950-1990.png') }})

The trend flattens out over the latter half of the twentieth century, however. Whatever stylistic shifts were happening in the twentieth century, by 1950 they were mostly complete and things had mostly stabilized again. 

What does this all represent in terms of literary history? My initial hunch was that we were seeing modernism's (and post-modernism's) break with Victorian, Edwardian, or Naturalist style. With the exception of (a very small) handful of Woolf, Hemingway, and Nabokov novels, though, our dataset of popular literature remains mostly void of what we'd consider canonical modernist or postmodernist fiction. This doesn't rule out the possibility that modernist and postmodernist aesthetics influenced popular culture, though---I think it's undeniable they have. Another possibility is that these trends represent a shift in post-War American feeling or imagination. These are just some ideas I'm throwing out there. Something interesting is clearly going on based on these trends: it will take a lot more (rigorous) study to make some more solid hypotheses.

[^novel]: The research described here was funded by [the NovelTM project](http://novel-tm.ca).

[^1]: Altick, Richard D. *The English Common Reader: A Social History of the Mass Reading Public 1800-1900*. Chicago: University of Chicago Press, 1957.<br /><br />
Hackett, Alice Payne and James Henry Burke. *80 Years of Best Sellers 1895--1975*. New York: R. R. Bowker Company, 1977.<br /><br />
Leavis, Q. D. *Fiction and the Reading Public*. 1935. New York: Russell & Russell, 1965.

[^2]: Thanks to Jordan for his thorough notes which highlighted Hackett's, Leavis's, and Altick's own descriptions of their projects.
