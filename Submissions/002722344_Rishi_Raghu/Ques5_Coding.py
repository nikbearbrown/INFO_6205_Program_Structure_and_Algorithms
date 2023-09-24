def create_skill_based_preferences(mentors, interns):
    mentor_pref = {}
    intern_pref = {}

    #TODO: Implement this function to create skill-based preferences for mentors and interns

    return mentor_pref, intern_pref

def find_stable_matching(mentor_preferences, intern_preferences):
    unassigned_interns = list(intern_preferences.keys())
    mentor_current = {}  # Current matchings for mentors
    intern_current = {}  # Current matchings for interns

    #TODO: Implement this function to find stable matching between mentors and interns

    return mentor_current

def remove_unstable_pairs(stable_pairs, unhappy_mentors, unhappy_interns):
    new_stable_pairs = {}

    #TODO: Implement this function to remove unstable pairs from stable_pairs
    
    return new_stable_pairs

# Example usage:
# mentors = [
#     {'name': 'Mentor_A', 'skills': ['Python', 'ML', 'Data Science', 'NLP']},
#     {'name': 'Mentor_B', 'skills': ['Web Development', 'JavaScript', 'React', 'Angular']},
#     {'name': 'Mentor_C', 'skills': ['Python', 'Flask', 'Web Development', 'React']},
#     {'name': 'Mentor_D', 'skills': ['ML', 'Python', 'NLP', 'Data Science']},
#     {'name': 'Mentor_E', 'skills': ['Web Development', 'HTML', 'CSS']}
# ]

# interns = [
#     {'name': 'Intern_A', 'skills': ['Python', 'ML', 'NLP']},
#     {'name': 'Intern_B', 'skills': ['JavaScript', 'React', 'Angular']},
#     {'name': 'Intern_C', 'skills': ['Python', 'Flask']},
#     {'name': 'Intern_D', 'skills': ['ML', 'Data Science', 'Python']},
#     {'name': 'Intern_E', 'skills': ['HTML', 'CSS', 'JavaScript']},
#     {'name': 'Intern_F', 'skills': ['Python', 'Flask', 'React']}
# ]
