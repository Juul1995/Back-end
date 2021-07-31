# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

Prevalent_language_Spain = 'Castilian Spanish'
Prevalent_language_Switzerland = 'German' 

Prevalent_religion_Spain = 'Roman Catholic'
Prevalent_religion_Switzerland = 'Roman Catholic'

Length_capital_Spain = len('Madrid')
Length_capital_Switzerland = len('Bern')

GDP_Spain = 1.778 * 10**12
GDP_Switzerland = 580 * 10**9

Population_growth_Spain = 0.67
Population_growth_Switzerland = 0.66

Population_Spain = 50 * 10**6
Population_Switzerland = 8.4 * 10**6
ten_million = 10*6

Most_spoken_language = Prevalent_language_Spain == Prevalent_language_Switzerland
print(Most_spoken_language)

Prevalent_religion = Prevalent_religion_Spain == Prevalent_religion_Switzerland
print(Prevalent_religion)

Capital_length = Length_capital_Switzerland != Length_capital_Spain
print(Capital_length)

print(GDP_Switzerland>GDP_Spain) #not yet correct:Switzerland's GDP is greater than Spain's GDP

print(Population_growth_Switzerland and Population_growth_Spain < 1.0) 
#The population growth is less than 1% in Switzerland and Spain.

print (Population_Spain>ten_million or Population_Switzerland>ten_million)
#Exactly one of the two countries has a population count of over 10 million

print (Population_Spain>ten_million and Population_Switzerland>ten_million)

