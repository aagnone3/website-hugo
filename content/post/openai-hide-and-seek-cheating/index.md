---
title: "OpenAI's Hide-and-Seek Findings: The Systems Perspective"
subtitle: The agents cheated, but what does that mean for the system
summary: The agents cheated, but what does that mean for the system
publication: Towards Data Science
authors:
- anthonyagnone

date: "2019-09-20T09:15:05Z"
featured: false
draft: false
slug: /openai-hide-and-seek-cheating

categories:
  - data

tags:
  - machine-learning
  - reinforcement-learning
  - incentives
  - systems
  - MARL

image:
  placement: 2
  caption: ""
  focal_point: ""
  preview_only: false
  
---

OpenAI released a [fantastic piece](https://openai.com/blog/emergent-tool-use/) on some results obtained in a multi-agent hide-and-seek simulation, in which multiple hiders and multiple seekers play the popular children's game.

![openai-hide-and-seek](/img/openai-hide-and-seek.gif)

The simulation had some interesting aspects to it, such as tools (boxes, ramps, walls) that the agents could use to aid them in achieving their objective of effective hiding/seeking.
However, the more notable result is that extended simulation of the environment led to _emergent behavior_; that is, behavior that is fundamentally unplanned or unexpected.

For example, some of the expected behavior is that the hiders would eventually learn to build an enclosure with the walls and/or boxes that hides the ramps from the seekers.
This way, the ramps cannot be used to go over the walls and into the built enclosure from above.
Now, what the environment designers did not expect (the emergent behavior) is that the seekers would learn that they could use the ramp to get on top of a box, and then use a running motion to essentially "surf" the box anywhere they pleased!

![openai-box-surfing](/img/openai-box-surfing.png)

Using this method, the seekers found a way to access the hider-built enclosures from above that was not intended by the designers of the system!

> The seekers had gamed the system.

Now, what do you think the hiders did in response to this behavior? Some of you may think that, since the seekers had learned, to some extent, undefined behavior of the system, that the hiders might respond with some ridiculous action, since the system was now in a state of disarray.

But think about it. The system was not in any sort of unknown state.

While it may be in a state that the designers did not explicitly intend to create, the agents were continuing to operate in a manner in which they saw as optimal for their desired outcomes.

Thus, the hiders learned to paralyze the seekers' ability to surf boxes!

![openai-surf-defense](/img/openai-surf-defense.png)

They did this by using the pre-allocated initial time in which the seekers are frozen to _lock all of the boxes and ramps_.
Then, they use any time left to construct a quick enclosure with the movable walls and then lock the walls.
This way, the seekers now, once again, have no way to get inside the enclosure (at least, that's the thought...).
Well played, guys.

I think that is fascinating, but on a different level than most of OpenAI's analysis focuses on. 
They do mention that the agents find out how to game their way to a system:

> "[...] agents build [...] strategies and counterstrategies, some of which we did not know our environment supported"

However, they then dive into detail only about the scenarios that the agents learned, and completely ignored the environmental design flaws themselves. I think the latter is the more interesting phenomenon!
I'd like to turn the analysis on its head -- let's now hold the agent designs constant, and vary the environment's state structure and reward system.
Analyze how different incentive/response systems _induce_ different agent strategies.
The field of reinforcement learning is progressing wonderfully, especially in recent years. We've gone from checkers solvers to a Go champion in just a few decades -- our _agent modeling_ is getting pretty dang good.
Now, how about our _multi-agent environment modeling?_

# Multi-Agent Environment Design
OpenAI has certainly thought about it. Per their final paragraph,

> Building environments is not easy and it is quite often the case that agents find a way to exploit the environment you build or the physics engine in an unintended way.

A great [article on reward function design](https://medium.com/@BonsaiAI/deep-reinforcement-learning-models-tips-tricks-for-writing-reward-functions-a84fe525e8e0)
written by [@BonsaiAI](https://medium.com/@BonsaiAI) on Medium mentions that "you get what you incentivize, not [necessarily] what you intend."
That beautifully summarizes the inherent dilemma in designing a reward system for a certain outcome.
You certainly have your mental picture of how your system of incentives will lead to the system as a whole reaching the desired state(s), but have you considered all of the minute ways in which your system may have some "cracks" in it?
Obviously, this is easier said than done. This divergence of "intent vs outcome" is readily seen in our daily lives, whether professionally or not:
- software engineers intend to turn documented specifications into functional software that is a faithful rendition of the documented change.
- company executives intend to compensate employees appropriately, based on how much value they provide to the company as a whole.
- sports team managers intend to apply game plans and player lineups that will bring victory over each successive opposing team.
- etc...

> The unwavering and succinct truth for all of these situations is that the system behaves _exactly_ as it is designed; there are not _undesigned_ consequences, only _unintended_ ones.

To make this idea clear, let's take the compensation scenario a little further.
Say there are employees near the middle of the corporate hierarchy who are unhappy with their compensation, and are taking issue
with the overall design of the compensation structure (assume the structure is readily known across the organization).
Statements these employees may make will go along the lines of "this system is broken" or "what's happening here is _wrong_".
However, what cannot be said in these circumstances (assuming a compassionate and fair designer) is "this system is not doing what it is designed to."

Of course it is! It is doing exactly what it is instructed to do!
If it should be doing something different than what it is now, then it should be changed as such.
Now, we may have _intended_ for the system to be doing one thing, but that may or may not actually be the final design.
However, regardless of intent, what is happening is a _perfect rendition of the system that was chosen_.

# A New Frontier
I'm excited to see more theory develop around effective design of environmental incentive systems, especially in multi-agent scenarios.
The applications for theory like this are littered in our daily lives, and are even among the most important questions we seek to answer with regard to living amongst each other.
Here are some examples:
- what's the best way for us to govern ourselves and others? [^1]
- what's the best way to organize how we define and exchange value between each other?
- what's the best way to collaborate with each other towards a common end product or creation?

It should only take one or two of those examples to get you sufficiently motivated for this. And that's great...because this area of research is just getting started in some respects.
For example, I imagine there is a plethora of historical publication on system-level analysis of things like governments, economic systems, and managerial hierarchies.
However, all of this precedence is going to soon be married with the recent advances in multi-agent RL.
The important similarities and differences between these theory families has the potential to lead to an explosion of knowledge and application in topics of human systems and computer-agent systems alike.

# Conclusion
Systems will always be gamed, whether the agents are human or digital.

What are your thoughts on effective ways to prevent/detect/fight the exploitation of incentive systems?

What are some interesting "timeless" academic works you know of, which analyze human/agent systems at large?

How about the same for reward design in multi-agent RL?

What other applications do you see here that I didn't touch on?

[^1]: I'm looking forward to the day where an electoral candiate's proposed policies can be evaluated by simulation, rendering the circus of televised debates useless
