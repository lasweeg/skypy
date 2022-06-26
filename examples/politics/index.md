# Examples for the politics method

## Setup
An API Key is not required for this Tutorial.
## First steps: Getting the current election results
### What you need
- A copy of skypy-api, preferrable installed via pypi (Version 1.X.X)
- A plae where you can execute code
- Basic python knowlege
- An internet connection
### Motivation
We want to make a simple script, which gives us the current election results. It should preferably be displayed in a nice way.

### Tutorial
We must import the module first:
```python
import skypy
skypyapi = skypy.skypy() # If you would have to use an API Key, it would be in the brackets "()"
```
This will import the skypy-api wrapper. Then, to call the subfunctions of the politics-method we type this:
```python
politicsapi = skypy.politics()
```
This tells the script that the variable `politicsapi` equals the `politics` method of the skypy class.

We can use this to call the `getElectionResults()` method, which returns an dictionary with the names of the canidates and their respective votes, what we can print out right after: 
```python
currentResults = politicsapi.getElectionResults()
print(currentResults)
```
This will print us something like this:
```json
{ "Marina": 109163, "Paul": 18863, "Diaz": 23142, "Barry": 17636, "Cole": 275875 }
```
But we can do it better! If we use an for-loop to loop through the elements, we can print them out nicely. Delete the lasteline and add this instead:
```python
for element in currentResults:
  print(element + ": " + str(currentResults[element]))
```
Note that we get the value of the element from the currentResults tuple, and then conver it to a string, because you can't add numbers to a string.

The output should look something like this:
```
Marina: 109163
Paul: 18863
Diaz: 23142
Barry: 17636
Cole: 275875
```
And this is it! Here is an overview of the code, which we have written in this tutorial:
_[(Or use the GitHub Gist)](https://gist.github.com/FuchsCrafter/ddfcdfdeda290910ba305bb24de9d518)_
```python
import skypy

skypyapi = skypy.skypy()

politicsapi = skypyapi.politics()

currentResults = politicsapi.getElectionResults()

for element in currentResults:
  print(element + ": " + str(currentResults[element]))
```


