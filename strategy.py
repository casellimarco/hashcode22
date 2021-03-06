from base_class import all_possible_assignments, Solution


def method(contributors, projects):
    solution = Solution()
    new_projects = []
    projects = list(projects.values())
    counter = 0
    while projects and counter < 10:
        for proj in projects:
            new_assignment = None
            for assignment in all_possible_assignments(proj, list(contributors.values())):
                new_assignment = {skill_name: contributor.name for skill_name, contributor in assignment.items()}
                continue
            if new_assignment is not None:
                solution.list_of_projects.append(proj.name)
                solution.proj_to_contr[proj.name] = new_assignment
                # mentoring
                for skill, contributor in assignment.items():
                    contributor.improve(skill, proj.skills_required[skill])
            else:
                new_projects.append(proj)
        counter += 1
        print(counter)
        projects = new_projects 
        new_projects = []
    
    return solution

def method_2(contributors, projects):
    solution = Solution()
    new_projects = []
    projects = list(projects.values())
    projects.sort(key=lambda x: x.num_contributors)
    counter = 0
    while projects and counter < 10:
        for proj in projects:
            new_assignment = None
            for assignment in all_possible_assignments(proj, list(contributors.values()), max_tries=10):
                new_assignment = {skill_name: contributor.name for skill_name, contributor in assignment.items()}
                continue
            if new_assignment is not None:
                solution.list_of_projects.append(proj.name)
                solution.proj_to_contr[proj.name] = new_assignment
                # mentoring
                for skill, contributor in assignment.items():
                    contributor.improve(skill, proj.skills_required[skill])
            else:
                new_projects.append(proj)
        counter += 1
        print(counter)
        projects = new_projects 
        new_projects = []
    
    return solution

import random

def method_3(contributors, projects):
    solution = Solution()
    new_projects = []
    projects = list(projects.values())
    projects.sort(key=lambda x: sum([v[1] for v in x.skills_required]))
    counter = 0
    while projects and counter < 10:
        for proj in projects:
            new_assignment = None
            random_contributors = list(contributors.values())
            random.shuffle(random_contributors)
            for assignment in all_possible_assignments(proj, random_contributors, max_tries=100):
                new_assignment = [c.name for c in assignment]
                continue
            if new_assignment is not None:
                solution.list_of_projects.append(proj.name)
                solution.proj_to_contr[proj.name] = new_assignment
                # mentoring
                for i, contributor in enumerate(assignment):
                    contributor.improve(*proj.skills_required[i])
            else:
                new_projects.append(proj)
        counter += 1
        print(counter)
        projects = new_projects 
        new_projects = []
    
    return solution
        
def method_4(contributors, projects):
    solution = Solution()
    new_projects = []
    projects = list(projects.values())
    projects.sort(key=lambda x: sum([v[1] for v in x.skills_required]))
    projects.sort(key=lambda x: x.last_day)
    counter = 0
    while projects and counter < 10:
        for proj in projects:
            new_assignment = None
            random_contributors = list(contributors.values())
            random.shuffle(random_contributors)
            for assignment in all_possible_assignments(proj, random_contributors, max_tries=1000):
                new_assignment = [c.name for c in assignment]
                continue
            if new_assignment is not None:
                solution.list_of_projects.append(proj.name)
                solution.proj_to_contr[proj.name] = new_assignment
                # mentoring
                for i, contributor in enumerate(assignment):
                    contributor.improve(*proj.skills_required[i])
            else:
                new_projects.append(proj)
        counter += 1
        print(counter)
        projects = new_projects 
        new_projects = []
    
    return solution

def random_method(base_classes):
    pass


if __name__ == "__main__":
    pass