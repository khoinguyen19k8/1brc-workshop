# One billion row challnge

Your mission, should you choose to accept it, is to write a program that retrieves temperature measurement values from a text file and calculates the min, mean, and max temperature per weather station. There's just one caveat: the file has 1,000,000,000 rows! That's more than 10 GB of data! 😱

The text file has a simple structure with one measurement value per row:


```
Hamburg;12.0
Bulawayo;8.9
Palembang;38.8
Hamburg;34.2
St. John's;15.2
Cracow;12.6
... etc. ...
```

The program should print out the min, mean, and max values per station, alphabetically ordered. The format that is expected varies slightly from language to language, but the following example shows the expected output for the first three stations:

```
Hamburg;12.0;23.1;34.2
Bulawayo;8.9;22.1;35.2
Palembang;38.8;39.9;41.0
```

## Rules and Limits

No external library dependencies may be used. That means no lodash, no numpy, no Boost, no nothing. You're limited to the standard library of your language.

The computation must happen at application runtime; you cannot process the measurements file at build time

Input value ranges are as follows:

Station name: non null UTF-8 string of min length 1 character and max length 100 bytes (i.e. this could be 100 one-byte characters, or 50 two-byte characters, etc.)
Temperature value: non null double between -99.9 (inclusive) and 99.9 (inclusive), always with one fractional digit
There is a maximum of 10,000 unique station names.

Implementations must not rely on specifics of a given data set. Any valid station name as per the constraints above and any data distribution (number of measurements per station) must be supported.

## Getting started

1. **Set up development environment**: In VS Code, reopen the folder in a container using the Dev Containers extension. This ensures you have a consistent development environment with all necessary tools.

2. **Generate test data**: Create test data files by running the data generator:
   ```bash
   python create_measurements.py <number_of_rows>
   ```
   For example, to start with 1 million rows for testing:
   ```bash
   python create_measurements.py 1_000_000
   ```
   Note: The ultimate goal is to handle 1 billion rows, but start smaller for development and testing.

3. **Set up your solution file**: Rename the `entries/RENAME_ME.py` file to `entries/firstname_lastname.py` using your actual first and last name.

   Note: If you want to create multiple versions of your solution you can do so by adding a `_v1/_v2/..` suffix. 

4. **Implement your solution**: Start implementing the logic in your renamed file. The file should read the measurements and output the min, mean, and max temperature per station.

5. **Test your implementation**: Run your solution using:
   ```bash
   python entries/your_file.py measurements/path_to_measurements_file
   ```
   For example:
   ```bash
   python entries/firstname_lastname.py measurements/measurements-1_000_000.txt
   ```

6. **Python interpreters available**:
   - CPython v3.12 is available as `python3.12`
   - PyPy 3.9 is available as `pypy3.9`
   
   You can test performance differences between interpreters by running your solution with different Python versions.

7. **Submit your solution**: Once you're satisfied with your implementation, submit your solution by pushing your changes to the repository.

Remember to test with progressively larger datasets as you optimize your solution, working your way up to the ultimate goal of processing 1 billion rows efficiently!
