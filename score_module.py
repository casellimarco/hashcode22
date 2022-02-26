from collections import defaultdict
from copy import deepcopy
from io_manager import read_input
import numpy as np

def get_score(solution, projects, contributors):
    day = 0
    score = 0

    days_to_complete = {p.name: p.length for p in projects.values()}
    assigned = {c.name: None for c in contributors.values()}

    while len(days_to_complete):
        to_be_unassigned = []

        for p in solution.list_of_projects:
            if p in days_to_complete:

                all_c_available = True
                for c in solution.proj_to_contr[p]:
                    if assigned[c] is None: # required contributor is free
                        assigned[c] = p
                    elif assigned[c] != p: # required contributor is assigned on other project
                        all_c_available = False

                if all_c_available:
                    days_to_complete[p] -= 1
                    if days_to_complete[p] == 0: # project finished
                        p_penalty = max(0, day + 1 - projects[p].last_day)
                        p_score = max(0, projects[p].score - p_penalty)
                        score += p_score
                        del days_to_complete[p]
                        to_be_unassigned += [c for c in assigned if assigned[c] == p]

        for c in to_be_unassigned:
            assigned[c] = None
        day += 1

    return score


def get_proxy_score(solution, projects, contributors):
    '''
    Returns a lower bound of the score. If the solution has been constructed using 
    a queue system it should return the exact score.
    '''
    solution = deepcopy(solution)
    last_worth_day = np.max([p.last_day + p.score for p in projects.values()])
    available_contributors = {c.name for c in contributors.values()} 
    running_projects = defaultdict(list)
    score = 0
    day = 0
    next_project_name = None
    while day < last_worth_day and (solution.list_of_projects or running_projects or next_project_name):
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
    proxy_score = get_proxy_score(solution, projects, contributors)
    print(f"{proxy_score=}")
    score = get_score(solution, projects, contributors)
    print(f"{score=}")
    
    import pickle
    
    with open("f_score_15275", "rb") as f:
        solution = pickle.load(f)
    contributors, projects = read_input("f")
    proxy_score = get_proxy_score(solution, projects, contributors)
    print(f"{proxy_score=}")
    score = get_score(solution, projects, contributors)
    print(f"{score=}")
    

