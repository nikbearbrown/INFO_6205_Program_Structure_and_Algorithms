
# TODO: Part 1 - Filter Out Non-Compatible Pairs
def filter_compatible_pairs(mentors, interns):
    """
    TODO: Filter out non-compatible mentor-intern pairs based on their skills.
    
    Input:
    - mentors: List of dictionaries, each containing 'name' and a list of 'skills'
    - interns: List of dictionaries, each containing 'name' and a list of 'skills'
    
    Output:
    - A list of compatible mentor-intern pairs represented as tuples (mentor_name, intern_name)
    """
    # TODO: Write your code here
    pass

# TODO: Part 2 - Identify Initially Stable Pairs Based on Skills
def find_initial_stable_pairs(compatible_pairs):
    """
    TODO: Identify a subset of pairs that could be considered "initially stable" based on skills alone.
    
    Input:
    - A list of compatible mentor-intern pairs represented as tuples (mentor_name, intern_name)
    
    Output:
    - A list of initially stable pairs represented as tuples (mentor_name, intern_name)
    """
    # TODO: Write your code here
    pass

# Example Usage
if __name__ == "__main__":
    mentors = [
        {'name': 'Alice', 'skills': ['Python', 'Machine Learning']},
        {'name': 'Bob', 'skills': ['Web Development', 'JavaScript']},
        {'name': 'Carol', 'skills': ['Data Analysis', 'Python']}
    ]

    interns = [
        {'name': 'Dave', 'skills': ['Python', 'Data Analysis']},
        {'name': 'Eve', 'skills': ['Machine Learning', 'Python']},
        {'name': 'Frank', 'skills': ['JavaScript', 'Web Development']}
    ]

    # First, find the compatible pairs (Part 1)
    compatible_pairs = filter_compatible_pairs(mentors, interns)
    print("Compatible Pairs:", compatible_pairs)  # Output should be calculated based on your implementation

    # Then, identify initially stable pairs based on skills (Part 2)
    initially_stable_pairs = find_initial_stable_pairs(compatible_pairs)
    print("Initially Stable Pairs:", initially_stable_pairs)  # Output should be calculated based on your implementation
