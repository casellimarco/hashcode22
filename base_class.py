import typing as t
from dataclasses import dataclass, field
from itertools import combinations, permutations

@dataclass
class Contributor:
    name: str
    skills: dict 

    def improve(self, skill, lvl):
        if lvl >= self.skills[skill]:
            self.skills[skill] += 1

    


@dataclass
class Project:
    name: str
    length: int
    score: int
    last_day: int
    num_contributors: int
    skills_required: list
    
    def get_score(self, day:int) -> int:
        return max(self.score - max(day - self.last_day, 0), 0)

@dataclass
class Solution:
    list_of_projects: list = field(default_factory=list)
    proj_to_contr: dict = field(default_factory=dict)


def all_possible_assignments(project: Project, contributors: t.List[Contributor], max_tries:int=100):
    tries = 0
    for subset in combinations(contributors, project.num_contributors):
        for permutation in permutations(subset):
            if is_valid_assignment(project, permutation):
                yield permutation
            tries+=1
            if tries >= max_tries:
                break
        if tries >= max_tries:
            break
    


def is_valid_assignment(
    constraints: Project,
    assignments: t.List[Contributor]
) -> bool:

    if len(constraints.skills_required) != len(assignments):
        False
    
    mentoring = []

    for i, (skill_name, required_level) in enumerate(constraints.skills_required):
        contributor_level = assignments[i].skills[skill_name]
        if contributor_level == required_level - 1:
            mentoring.append((skill_name, required_level))
            
        elif contributor_level < required_level:
            return False
    
    for skill_name, required_level in mentoring:
        found = False
        for contributor in assignments:
            contributor_level = contributor.skills[skill_name]
            if contributor_level >= required_level:
                found = True
                continue
        if not found:
            return False 

    return True

if __name__ == "__main__":
    example_solution = [
        {
            "Logging": {
                "C++": "Anna",
            },
        },
        {
            "WebServer": {
                "HTML": "Anna",
                "C++": "Bob",
            }
        }, # project 2
        {
            "WebChat": {
                "Python": "Anna",
                "HTML": "Bob",
            }
        }, # project 3
    ]
    example_mapping = dict()
    example_projects = []
    for proj in example_solution:
        example_mapping.update(proj)
        example_projects.append(list(proj.keys())[0])

    example_sol = Solution(example_projects, example_mapping)
    
    