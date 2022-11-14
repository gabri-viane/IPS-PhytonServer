# IPS-PhytonServer

**web.py**

UDP(2522 port) reader. 
Receive bytes and automtically decodes them for the elaboration.



**modulo_tag.py**

TAG(class):
Automatically divides data received by the antennas in different lists to easily elaborates those in a future moment.


`add_antenna(antenna, valore)`
Can add an infinite amount of antennas to store values appropriately. 
**Will need an initial value to create the list and the antenna name**


`add_value(antenna, valore)`
Add a value to a specific antenna.
Will check automatically if the antenna is already created(if not it automatically creates and add the value):
```
index = self.search_dict(antenna)
if isinstance(index, int):
        self.antenne[index]["valori"][self.orario()] = valore
else:
        self.add_antenna(antenna,valore)
```


`search_dict(antenna)`
Search if the specified antenna is in the db or not. 
**Returns the index(INT) if present. If not, returns the string "NON_PRESENTE"**


`print_antenne()`
Print in an user-friendly way all the data. 
>This will probably be removed when the pandas dataframe is 100% active.



**TAGS(class):**
Static class. Will store all the tags inside the list "lista"


`add_tag(tag_n)`
Add a tag to the list.
**WILL CREATE THE OBJECT TAG. NEEDS THE TAG NUMBER TO WORK.**


`search_tag(codice)`
Search if the specified tag number is already inside the list or not.
**Returns the index(INT) if present. If not, returns the string "NON_PRESENTE"**


`add_value(codice, value, antenna)`
**ALL THOSE VALUES GOTTA BE INTS.**
Used by the `elaborate_data(data)` function to add values to the received tag. This just search if the tag exists(and creates it if it doesn't) and calls the `add_value(antenna, valore)` of the TAG class.


`print_tags()`
Prints every tag value formatted by the `print_antenne()' function.


***`elaborate_data(data)`***
***

THIS FUNCTION NEEDS A SPECIFIC LIST TO WORK:
>First value--> Antenna ID sending the data<br>
>Second value--> Number of tags found by the antenna<br>
BASED ON THE SECOND VALUE, THE FUNCTION WILL CHECK FOR EVERY TAG TWO VALUES:<br>
>tag ID, rssi value.
***
![value list](https://user-images.githubusercontent.com/34715958/201696677-6bab8f60-6641-4456-ac7d-d5df707b5d49.png)
Calls the TAGS function `add_value` to add the data received

