---
title: "Advent of Code: Your New Holiday Season Routine!"
subtitle: "Harden up your problem solving and coding proficiency while celebrating the holidays"
summary: "Harden up your problem solving and coding proficiency while celebrating the holidays"
publication:
platforms:
    - medium
    - dev
authors:
    - anthonyagnone

# date +\%FT\%TZ 
date : "2019-11-24T14:00:18Z"
featured: false
draft: false
slug: /advent-of-code-2019

categories:
    - algorithms

tags:
    - algorithms
    - software
    - routine
    - learning

image:
    placement: 2
    caption: "Photo by Mourad Saadi on Unsplash"
    focal_point: ""
    preview_only: false
---

# The Gist
> Man, I really need to brush up on <language/skill>.

> I should check out <language/skill>. I'm seeing it appear more and more, and it will become important for me to be proficient in.

How many times have you recently had some of these conversations with yourself? Chances are, you have at least a few times, and most of us will also readily admit that we also haven't done much of anything about it. Well, here's a fun holiday season routine for you that can help you out: [Advent of Code](https://adventofcode.com/2019/about)!

---
# What it is
Advent of Code is an annual series of daily coding challenges that happens during the year-end holiday season. 
While its name alludes to Christian traditions, it is a simple pun choice meant to convey the 25-day nature of the series (come one, come all!). 
Each day, between the 1st and 25th of December, a new puzzle is published. The puzzles usually string along a wonderfully-constructed storyline, keeping you entertained as you are challenged. 
Here's an example from last year:

## Example Puzzle (Day 1 2018)
After feeling like you've been falling for a few minutes, you look at the device's tiny screen. "Error: Device must be calibrated before first use. Frequency drift detected. Cannot maintain destination lock." Below the message, the device shows a sequence of changes in frequency (your puzzle input). A value like +6 means the current frequency increases by 6; a value like -3 means the current frequency decreases by 3.

For example, if the device displays frequency changes of +1, -2, +3, +1, then starting from a frequency of zero, the following changes would occur:

Current frequency  0, change of +1; resulting frequency  1.
Current frequency  1, change of -2; resulting frequency -1.
Current frequency -1, change of +3; resulting frequency  2.
Current frequency  2, change of +1; resulting frequency  3.
In this example, the resulting frequency is 3.

Here are other example situations:

+1, +1, +1 results in  3
+1, +1, -2 results in  0
-1, -2, -3 results in -6
Starting with a frequency of zero, what is the resulting frequency after all of the changes in frequency have been applied?
---

At this point, a link is available on the page for you to obtain the full input sequence (about a thousand inputs) as a text file. 
This is where the rubber meets the road between your problem solving skills and software implementation know-how. 

Be careful! Most people will happily _nose dive_ into regurgitating code that reads the input, and then face-plant when they realize it's time to implement the core algorithm. 
Take the time first to make sure you fully understand the problem at hand, and (at least mentally) form the algorithmic solution before rushing to the I/O code.

---
# Why you should do it

You need not use any sort of significant computing hardware to participate in these challenges -- feel free to leave your cloud-computing mindset to the side, and get yourself back into the single machine, single problem mindset of your first data structures and algorithms endeavor 😉. 
The puzzles, designed personally by [Eric](http://was.tl/) 👏, are designed such that solving the problem in brute-force fashion will take entirely too long, but solving in a more intelligent fashion will solve the puzzle in at most 15 seconds on commodity hardware. 

You need not use any sort of super duper optimized programming language, either. Note that, since the correct approach to the puzzle will give you the answer in seconds, the true differentiator in solutions is _development time_. 
Thus, an appropriate approach in an interpreted language (Python, R, etc) will prevail over a naive approach written in a compiled language (C, Rust, Go, etc). 
I love this aspect. Some folks love to gripe about how <insert favorite language here> is the best because you can always optimize it to run faster and closer to the bare metal etc etc etc. 
However, how fast your algorithm runs on hardware is usually not the bottleneck in your end system:

> The more expensive factors of an algorithmic solution tend to be things like developer time-to-solution, lack of parallelism, or I/O congestion, as opposed to compiler-enabled program optimization.

When was the last time you were in an interview for an established software company, and they constrained you to a language of choice? [^1] 
Usually, you were instead constrained to (either explicitly, or implicitly via a failed interview!) providing a solution that was modular, efficient, and scalable. 
All of these things are capable in any Turing-complete language. So forget about language wars for this series, and focus on the real intellectual meat of the problem.

Indeed, many dispose of competition altogether here, and use Advent of Code as an opportunity to learn a new language. 
Personally, I plan to do my first pass in Python, and then follow up in either Go or Javascript (gotta stay future-proof 🧐). 
Whether you are looking for intense competition, a learning opportunity, or a chance to establish a good habit this holiday season, consider finding it in Advent of Code!

---
# Ready to Go?
Start by reviewing some puzzles from [past years](https://adventofcode.com/2019/events).
Feeling your more competitive side? Join the private leaderboard [here](https://adventofcode.com/2019/leaderboard/private) with code `498713-51f0c909` to see how you match up with other participants. 

---
# Share your opinion
Why are you planning or not planning to participate in this? If you are not, what would change your mind?

Do you have tried-and-tested ways to ensure the habit of completing daily tasks like this for extended periods of time?

What else would you like to share?

[^1]: I hope there aren't too many of you that have been a part of such an interview 😬.
