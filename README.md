# Old MacDonald Had a Farm Nursery Rhyme Program

This project is a Python implementation of the nursery rhyme **"Old MacDonald Had a Farm"**, showcasing both polymorphism and data-driven approaches. 
The program prints verses for different animals and allows users to add their own animals and sounds.

## Features

- **Two Approaches**: 
  1. Polymorphism-based solution with predefined animals.
  2. Data-driven solution using arrays for animals and their sounds.
- **Custom Animal Input**: Users can add their own animals and sounds.
- **Automatic Update**: If a user adds an animal not in the predefined list, it automatically adds the animal and its sound to the array to minimize errors.

## Project Structure

├── main.py # Main entry point for the program  
├── animal.py # Animal class for polymorphism  
├── predefined_animals.py # Predefined animals and their sounds  
├── polymorphism_solution.py # Polymorphism-based solution  
├── data_driven_solution.py # Data-driven solution using arrays  

### Files Description

- **`main.py`**: The main script where the user chooses which approach to use (polymorphism, data-driven, or custom animals).
- **`animal.py`**: Contains the `Animal` class used in the polymorphism solution.
- **`predefined_animals.py`**: Contains the predefined list of animals and sounds for the polymorphism approach.
- **`polymorphism_solution.py`**: Implements the polymorphism solution.
- **`data_driven_solution.py`**: Implements the data-driven solution.

## How to Run the Project

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Running the Program
To run the program, use:
```bash
python main.py
```

You will be prompted to choose between three options:  

1. Predefined animals (polymorphism-based solution).  
2. Data-driven approach.  
3. Enter your own animals.
   
Example Output (Predefined Animals):  
```bash
Old MacDonald had a farm, E I E I O,
And on his farm, he had a cow, E I E I O.
With a moo moo here and a moo moo there,
Here a moo, there a moo, everywhere a moo moo.
Old MacDonald had a farm, E I E I O.
```

Adding Your Own Animals
```bash
Enter the name of an animal: giraffe
Enter the sound that a giraffe makes: hum
```

### Notes  
The project includes input validation for both animal names and sounds.  
The program is designed to minimize errors and provide a seamless experience for users.  

### Requirements  
Python 3.x
