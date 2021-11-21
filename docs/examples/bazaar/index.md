# Bazaar Examples
## Setup
You should start by importing the module and then creating the skypyapi-object:

```python
import skypy
skypyapi = skypy.skypy("YOUR-TOKEN") # The token is optional
```
Then add this code to create an bazaar object:

```python
bazaarapi = skypyapi.bazaar()
```
The Code should look now like this:

```python
import skypy
skypyapi = skypy.skypy("YOUR-TOKEN") # The token is optional
bazaarapi = skypyapi.bazaar()
```
## Basic functions
### Getting all Products of the bazaar
This works with the `fetchAllProducts()`-Function. This will get the server response of `https://api.hypixel.net/skyblock/bazaar`and return them as JSON.

```python
print(bazaarapi.fetchAllProducts())
```
