import matplotlib.pyplot as plt
import numpy as np
import csv

# Data for the total population, female population, and male population for each year
years = list(range(2001, 2022))
total_population = [1078970907,1098313039,1117415123,1136264583,1154638713,1172373788,1189691809,1206734806,1223640160,1240613620,1257621191,1274487215,1291132063,1307246509,1322866505,1338636340,1354195680,1369003306,1383112050,1396387127,1407563842]
female_population = [429978166, 539178882, 548274218, 557161047, 565762395, 574185530,582492785, 590747758, 599047591, 607376801, 615647779, 623809180,631697152, 639323292, 647012921, 654607791, 661854076, 668786993,675389679, 681060412, 685992675]
male_population = [430135579, 578236241, 587990365, 597477666, 606611392, 615506279,624242020, 632892402, 641566029, 650244390, 658839435, 667322883,675549357, 683543213, 691623419, 699587889, 707149230, 714325057,720997448, 726503429, 731180498]


# Create subplots for side-by-side bar charts
fig, ax = plt.subplots(figsize=(12, 6))
# Set the width of each bar
bar_width = 0.25
# Set the x-axis positions for the bars
x = np.arange(len(years))
# Plot the total population
ax.bar(x - bar_width, total_population, bar_width, label='Total Population', color='b')
# Plot the female population
ax.bar(x, female_population, bar_width, label='Female Population', color='g')
# Plot the male population
ax.bar(x + bar_width, male_population, bar_width, label='Male Population', color='r')

# Set labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Population(In Billions)')
ax.set_title('Population Distribution in India (2001-2021)')

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(years, rotation=45)

# Add a legend
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()
