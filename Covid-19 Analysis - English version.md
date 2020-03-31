# Introduction

The following document aims to analyze the trend of the COVID-19 pandemic in Italy, drawing on the data that the net data provides to now, 31-March-2020.

The phases that I will analyze will be the following:

1. Understanding the problem

2. Data acquisition
    * Data cleaning
    * Data exploration & Feature Engineering
3. Predictive Modeling
4. Data Visualization
5. Conclusions

# Understanding the problem

The situation is complex as it is rich in variables, therefore the analysis of the spread of this pathology requires an understanding of:

* reliability of the data provided and on which it is necessary to operate;
* type of disease.

#### Are the data reliable?

This point must take into consideration two aspects:

1. the data collection protocol between different States;

2. on  the other hand with the same protocol (ie within the same country) the data collected which percentage of cases are able to cover (ie many people pass the disease alone at home, many are asymptomatic);

The answer to these two questions is likely to invalidate any analysis, or give results that are not credible or usable, comparable to a dice roll.

> 1. The data I have collected so far, based on the information received from the official media, lead me to think that the protocols between the various States are not uniform, as the attribution of a death for COVID-19 is not is equal, the number of swabs performed are not proportionally equal. For this reason I believe it is not possible to treat two States within the same analysis, and I will limit my case study to the Italian State only.
> 2. As for the amount of data collected, not having the possibility of knowing whether the data provided is adequate, I take it for good that it is, and I will operate on the data provided by the official national sources.

#### The illness

Viral agent that aggressively attacks the respiratory system, causing within a certain percentage, an aggravation of the therapeutic situation, changing into an interstitial pneumonia, up to, in the most serious cases, the death of the patient.

> Even if the analysis of the problem is limited to the Italian State only, the evolution of the pandemic is very different. This leads me to think that a different evolution, with the same care, containment and recognition protocols, is caused by different situations between the various Italian regions. Pathogens proliferate in situations suitable for their reproduction, if the diffusion is different in two population groups, perhaps one should not look for the virus but for the population.
>
> A starting point for this consideration was provided by these two photos:
>
> ![](Images/PM25-COVID19.png)
>
> 