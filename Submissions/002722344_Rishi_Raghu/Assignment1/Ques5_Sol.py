def create_skill_based_preferences(mentors, interns):
    mentor_pref = {}
    intern_pref = {}
    
    # Loop through mentors to create their preference lists
    for mentor in mentors:
        mentor_name = mentor['name']
        mentor_skills = set(mentor['skills'])
        mentor_pref[mentor_name] = []
        
        # Sort interns based on the number of matching skills
        for intern in sorted(interns, key=lambda x: len(mentor_skills.intersection(set(x['skills']))), reverse=True):
            intern_name = intern['name']
            if len(mentor_skills.intersection(set(intern['skills']))) > 0:
                mentor_pref[mentor_name].append(intern_name)

    # Loop through interns to create their preference lists
    for intern in interns:
        intern_name = intern['name']
        intern_skills = set(intern['skills'])
        intern_pref[intern_name] = []
        
        # Sort mentors based on the number of matching skills
        for mentor in sorted(mentors, key=lambda x: len(intern_skills.intersection(set(x['skills']))), reverse=True):
            mentor_name = mentor['name']
            if len(intern_skills.intersection(set(mentor['skills']))) > 0:
                intern_pref[intern_name].append(mentor_name)
    
    # Formatting output
    formatted_mentor_pref = "\n".join([f"{mentor}: {prefs}" for mentor, prefs in mentor_pref.items()])
    formatted_intern_pref = "\n".join([f"{intern}: {prefs}" for intern, prefs in intern_pref.items()])

    print(f"Mentor Preferences:\n{formatted_mentor_pref}")
    print(f"Intern Preferences:\n{formatted_intern_pref}")

    return mentor_pref, intern_pref

def find_stable_matching(mentor_preferences, intern_preferences):
    unassigned_interns = list(intern_preferences.keys())
    mentor_current = {}  # Current matchings for mentors
    intern_current = {}  # Current matchings for interns
    mentor_next_proposal = {mentor: 0 for mentor in mentor_preferences}  # Next proposal index for each mentor

    while unassigned_interns:
        intern = unassigned_interns.pop(0)
        preferred_mentors = intern_preferences[intern]
        
        for mentor in preferred_mentors:
            if mentor not in mentor_current:  # Mentor is unassigned
                mentor_current[mentor] = intern
                intern_current[intern] = mentor
                break
            else:  # Mentor is already assigned
                current_intern = mentor_current[mentor]
                if mentor_preferences[mentor].index(intern) < mentor_preferences[mentor].index(current_intern):  # New intern is preferred
                    mentor_current[mentor] = intern
                    intern_current[intern] = mentor
                    if current_intern in intern_current:
                        del intern_current[current_intern]
                    unassigned_interns.append(current_intern)  # Reassign previous intern
                    break

    return mentor_current

def remove_unstable_pairs(stable_pairs, unhappy_mentors, unhappy_interns):
    new_stable_pairs = {}
    
    for mentor, intern in stable_pairs.items():
        if mentor not in unhappy_mentors and intern not in unhappy_interns:
            new_stable_pairs[mentor] = intern
    
    return new_stable_pairs


mentors = [
    {'name': 'Mentor_A', 'skills': ['Python', 'ML', 'Data Science', 'NLP']},
    {'name': 'Mentor_B', 'skills': ['Web Development', 'JavaScript', 'React', 'Angular']},
    {'name': 'Mentor_C', 'skills': ['Python', 'Flask', 'Web Development', 'React']},
    {'name': 'Mentor_D', 'skills': ['ML', 'Python', 'NLP', 'Data Science']},
    {'name': 'Mentor_E', 'skills': ['Web Development', 'HTML', 'CSS']}
]

interns = [
    {'name': 'Intern_A', 'skills': ['Python', 'ML', 'NLP']},
    {'name': 'Intern_B', 'skills': ['JavaScript', 'React', 'Angular']},
    {'name': 'Intern_C', 'skills': ['Python', 'Flask']},
    {'name': 'Intern_D', 'skills': ['ML', 'Data Science', 'Python']},
    {'name': 'Intern_E', 'skills': ['HTML', 'CSS', 'JavaScript']},
    {'name': 'Intern_F', 'skills': ['Python', 'Flask', 'React']}
]

unhappy_mentors = ['Mentor_A']
unhappy_interns = ['Intern_A', 'Intern_F']

mentor_preferences, intern_preferences = create_skill_based_preferences(mentors, interns)
stable_pairs = find_stable_matching(mentor_preferences, intern_preferences)
print("Stable Matches:", stable_pairs)
new_stable_pairs = remove_unstable_pairs(stable_pairs, unhappy_mentors, unhappy_interns)
print("New Stable Pairs:", new_stable_pairs)
