import csv
import os


# ==================== Task 3: Functions ====================
def calculate_total(dataset):
    """Calculate the sum of all values in the dataset."""
    total = 0
    for value in dataset:
        total = total + value  # Using arithmetic operator +
    return total


def calculate_average(dataset):
    """Calculate the average of all values in the dataset."""
    if len(dataset) == 0:
        return 0
    total = calculate_total(dataset)
    avg = total / len(dataset)  # Using arithmetic operator /
    return avg


def calculate_minimum(dataset):
    """Find the minimum value in the dataset."""
    if len(dataset) == 0:
        return None
    
    min_value = dataset[0]
    for value in dataset:
        if value < min_value:
            min_value = value
    return min_value


def calculate_maximum(dataset):
    """Find the maximum value in the dataset."""
    if len(dataset) == 0:
        return None
    
    max_value = dataset[0]
    for value in dataset:
        if value > max_value:
            max_value = value
    return max_value


# ==================== Task 6: Sets for Unique Categories ====================
def extract_unique_categories(filename):
    """Extract unique categories from a file using sets."""
    categories = set()  # Using set to store unique values
    
    try:
        with open(filename, 'r') as file:
            # Check if file is CSV or text
            if filename.endswith('.csv'):
                reader = csv.reader(file)
                next(reader, None)  # Skip header if present
                for row in reader:
                    if row:  # Check if row is not empty
                        categories.add(row[0].strip())
            else:
                for line in file:
                    line = line.strip()
                    if line:
                        categories.add(line)
        
        return categories
    
    except FileNotFoundError:
        print(f"Category file '{filename}' not found.")
        return set()
    except Exception as e:
        print(f"Error reading category file: {e}")
        return set()


# ==================== Task 7: Object-Oriented Programming ====================
class DataSet:
    """A class to manage and analyze numerical datasets."""
    
    def __init__(self, data_filename, category_filename=None, threshold=50):
        """
        Initialize the DataSet object.
        
        Parameters:
        - data_filename: File containing numerical data
        - category_filename: File containing categorical data (optional)
        - threshold: Performance threshold for conditional check
        """
        self.data_filename = data_filename
        self.category_filename = category_filename
        self.threshold = threshold
        self.data = []
        self.categories = set()
        self.statistics = {}
    
    def load_data(self):
        """Load numerical data from file with error handling."""
        print(f"\n{'='*60}")
        print(f"Loading data from '{self.data_filename}'...")
        print(f"{'='*60}")
        
        # Task 2a: Handle file not found
        try:
            with open(self.data_filename, 'r') as file:
                lines = file.readlines()
                
                # Task 2b: Handle empty file
                if not lines:
                    print("ERROR: The file is empty!")
                    return False
                
                # Determine if it's a CSV file
                is_csv = self.data_filename.endswith('.csv')
                
                if is_csv:
                    reader = csv.reader(lines)
                    rows = list(reader)
                    
                    # Skip header row if present
                    start_index = 1 if rows and not self._is_numeric(rows[0][0]) else 0
                    
                    # Task 4b: Using loop to traverse dataset
                    for i in range(start_index, len(rows)):
                        row = rows[i]
                        if row:  # Check if row is not empty
                            try:
                                # Task 2b: Handle invalid (non-numeric) values
                                value = float(row[0].strip())
                                self.data.append(value)
                            except ValueError:
                                print(f"Warning: Skipping invalid value '{row[0]}' on line {i+1}")
                else:
                    # Handle text file
                    for i, line in enumerate(lines, 1):
                        line = line.strip()
                        if line:
                            try:
                                value = float(line)
                                self.data.append(value)
                            except ValueError:
                                print(f"Warning: Skipping invalid value '{line}' on line {i}")
                
                # Check if we loaded any valid data
                if not self.data:
                    print("ERROR: No valid numeric data found in file!")
                    return False
                
                print(f"✓ Successfully loaded {len(self.data)} data points")
                return True
        
        except FileNotFoundError:
            print(f"ERROR: File '{self.data_filename}' not found!")
            return False
        except Exception as e:
            print(f"ERROR: An unexpected error occurred: {e}")
            return False
    
    def _is_numeric(self, value):
        """Helper method to check if a value is numeric."""
        try:
            float(value)
            return True
        except ValueError:
            return False
    
    def calculate_statistics(self):
        """Calculate all statistics for the dataset."""
        if not self.data:
            print("No data available for calculation.")
            return
        
        print(f"\n{'='*60}")
        print("Calculating statistics...")
        print(f"{'='*60}")
        
        # Task 4a & 4b: Using operators and loops
        total = calculate_total(self.data)
        average = calculate_average(self.data)
        minimum = calculate_minimum(self.data)
        maximum = calculate_maximum(self.data)
        
        # Task 1b: Store data in appropriate variables
        self.statistics = {
            'total': total,
            'average': average,
            'minimum': minimum,
            'maximum': maximum,
            'count': len(self.data)
        }
        
        # Task 5: Conditional statements for performance evaluation
        if average > self.threshold:
            self.statistics['performance'] = "High Performance"
        else:
            self.statistics['performance'] = "Needs Improvement"
        
        # Task 6: Load and process categories if file provided
        if self.category_filename:
            self.categories = extract_unique_categories(self.category_filename)
            self.statistics['unique_categories'] = len(self.categories)
        
        print("✓ Statistics calculated successfully")
    
    def display_results(self):
        """Display the calculated statistics."""
        if not self.statistics:
            print("No statistics available. Please calculate statistics first.")
            return
        
        print(f"\n{'='*60}")
        print("ANALYSIS RESULTS")
        print(f"{'='*60}")
        print(f"Total:                {self.statistics['total']:.2f}")
        print(f"Average:              {self.statistics['average']:.2f}")
        print(f"Minimum:              {self.statistics['minimum']:.2f}")
        print(f"Maximum:              {self.statistics['maximum']:.2f}")
        print(f"Count:                {self.statistics['count']}")
        print(f"Performance:          {self.statistics['performance']}")
        print(f"Threshold:            {self.threshold}")
        
        if self.categories:
            print(f"\n{'='*60}")
            print("CATEGORY ANALYSIS")
            print(f"{'='*60}")
            print(f"Unique Categories:    {self.statistics['unique_categories']}")
            print(f"Categories:           {', '.join(sorted(self.categories))}")
        
        print(f"{'='*60}\n")
    
    def save_report(self, report_filename="analysis_report.txt"):
        """Save the analysis results to a file."""
        try:
            with open(report_filename, 'w') as file:
                file.write("="*60 + "\n")
                file.write("DATASET ANALYSIS REPORT\n")
                file.write("="*60 + "\n\n")
                
                file.write(f"Source File: {self.data_filename}\n")
                file.write(f"Analysis Date: {self._get_current_date()}\n\n")
                
                file.write("STATISTICAL SUMMARY\n")
                file.write("-"*60 + "\n")
                file.write(f"Total:                {self.statistics['total']:.2f}\n")
                file.write(f"Average:              {self.statistics['average']:.2f}\n")
                file.write(f"Minimum:              {self.statistics['minimum']:.2f}\n")
                file.write(f"Maximum:              {self.statistics['maximum']:.2f}\n")
                file.write(f"Count:                {self.statistics['count']}\n")
                file.write(f"Performance:          {self.statistics['performance']}\n")
                file.write(f"Threshold:            {self.threshold}\n\n")
                
                if self.categories:
                    file.write("CATEGORY ANALYSIS\n")
                    file.write("-"*60 + "\n")
                    file.write(f"Unique Categories:    {self.statistics['unique_categories']}\n")
                    file.write(f"Categories:           {', '.join(sorted(self.categories))}\n\n")
                
                file.write("="*60 + "\n")
                file.write("END OF REPORT\n")
                file.write("="*60 + "\n")
            
            print(f"✓ Report saved to '{report_filename}'")
            return True
        
        except Exception as e:
            print(f"ERROR: Failed to save report: {e}")
            return False
    
    def _get_current_date(self):
        """Helper method to get current date."""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ==================== Main Program ====================
def create_sample_files():
    """Create sample data files for testing."""
    # Create sample numerical data file (CSV)
    with open('student_marks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Marks'])  # Header
        marks = [85, 92, 78, 95, 88, 76, 91, 84, 89, 93]
        for mark in marks:
            writer.writerow([mark])
    
    # Create sample category file
    with open('courses.txt', 'w') as file:
        courses = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 
                   'Mathematics', 'Physics', 'Computer Science', 'Mathematics']
        for course in courses:
            file.write(course + '\n')
    
    print("✓ Sample files created: 'student_marks.csv' and 'courses.txt'")


def main():
    """Main function to run the dataset analysis system."""
    print("\n" + "="*60)
    print("DATASET MANAGEMENT AND ANALYSIS SYSTEM")
    print("="*60)
    
    # Create sample files for demonstration
    create_sample_files()
    
    # Task 7: Create an object of DataSet class
    dataset = DataSet(
        data_filename='student_marks.csv',
        category_filename='courses.txt',
        threshold=85
    )
    
    # Run the analysis
    if dataset.load_data():
        dataset.calculate_statistics()
        dataset.display_results()
        dataset.save_report('student_analysis_report.txt')
    
    print("\n" + "="*60)
    print("Analysis complete!")
    print("="*60 + "\n")


# Run the program
if __name__ == "__main__":
    main()