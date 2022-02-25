from collections import defaultdict
from copy import deepcopy
from io_manager import read_input
import numpy as np



def get_score(solution, projects, contributors):
    solution = deepcopy(solution)
    last_worth_day = np.max([p.last_day + p.score for p in projects.values()])
    available_contributors = {c.name for c in contributors.values()} 
    running_projects = defaultdict(list)
    score = 0
    day = 0
    next_project_name = None
    while day < last_worth_day and (solution.list_of_projects or running_projects):
        for completed_proj in running_projects.pop(0, []):
            score += completed_proj.get_score(day)
            available_contributors.update(solution.proj_to_contr[completed_proj.name])
        if next_project_name is None:
            if solution.list_of_projects:
                next_project_name = solution.list_of_projects.pop(0)
            else:
                running_projects = defaultdict(list, {day_left-1: projs for day_left, projs in running_projects.items()})
                day +=1
                continue

        next_project = projects[next_project_name]
        next_contributors = set(solution.proj_to_contr[next_project_name])
        if next_contributors.issubset(available_contributors):
            available_contributors -= next_contributors
            running_projects[next_project.length].append(next_project)
            next_project_name = None
        else:
            running_projects = defaultdict(list, {day_left-1: projs for day_left, projs in running_projects.items()})
            day +=1
    return score
    

if __name__ == "__main__":
    from io_manager import read_input, write_output
    from base_class import Solution 
    solution = Solution(
        list_of_projects=['WebServer', 'WebChat', 'Logging'],
        proj_to_contr={
            'WebServer': ['Bob', 'Anna'],
            'WebChat': ['Maria', 'Bob'],
            'Logging': ['Anna'],
        }
    )
    contributors, projects = read_input("a")
    score = get_score(solution, projects, contributors)
    print(score)
