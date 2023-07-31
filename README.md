# Readme - Code Overview and Explanation

This program calculates the molecular mass of a given chemical formula. It fetches the atomic masses of chemical elements from the Wikipedia page "Liste des éléments chimiques" and then allows the user to enter a chemical formula. The program uses regular expressions and the fetched data to determine the molecular mass and displays the result in grams per mole (g/mol).

## Prerequisites
- *Python* 3.x
- *requests* library
- *beautifulsoup4* library

## Installation
1. Make sure you have Python 3.x installed on your system.
2. Install the required libraries using pip:
```bash
pip install requests
pip install beautifulsoup4
```

## Usage
1. Run the Python script.
2. When prompted, enter the chemical formula for which you want to calculate the molecular mass.

## How It Works
1. The program fetches atomic masses of chemical elements from the Wikipedia page "Liste des éléments chimiques."
2. It then prompts the user to enter a chemical formula (e.g., H2O, C6H12O6, CH4, etc.).
3. The program uses regular expressions to parse the chemical formula into individual elements and their respective counts.
4. It calculates the molecular mass by summing up the atomic masses of all the elements present in the formula, accounting for their counts.
5. The result is displayed in grams per mole (g/mol).

## Example
```bash
quel est ta molécule
C6H12O6
180 g/mol
```

## Disclaimer
This program uses data from a specific Wikipedia page to fetch atomic masses. While it provides accurate results for most chemical formulas, it may not cover all elements or edge cases. Therefore, it is essential to validate the output with reliable sources in critical applications.



Please note that this README is meant to provide an overview and explanation of the program. For a complete working version of the program, ensure that the required libraries are installed and the Python script is executed correctly. Modify and customize the program as needed to suit your specific use case.

Feel free to use this markdown as a template for your README. You can further tailor the content and format to meet your project's specific requirements.

Remember that this project is for educational purposes only.
The author is not responsible for any future errors or accidents
