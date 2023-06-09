import os

PROBLEM_DIR = "problems"

task_list = {}

subject_matcher = {
    "math": "Математика",
    "phys": "Физика",
    "info": "Информатика",
}

for dir in sorted(os.listdir(PROBLEM_DIR)):
    if dir not in task_list:
        task_list[dir] = {}
    full_dir = os.path.join(PROBLEM_DIR, dir)

    if os.path.isdir(full_dir):
        for problem in sorted(os.listdir(full_dir)):
            if problem[0] in ['m', 'p', 'i']:
                subject, number = problem.split('_')
                number = int(number)
                if subject not in task_list[dir]:
                    task_list[dir][subject] = []

                with open(os.path.join(full_dir, problem), 'r') as f:
                    task_list[dir][subject].append((number, f.read()))

file_content = []              
with open("README.md", 'r') as f:
    cur_files = {}
    for row in f.readlines():
        if row != "-----\n":
            file_content.append(row)
        elif row == "-----\n":
            file_content.append(row)
            break

for name in task_list.keys():
    file_content.append("# " + name + "\n\n")

    for subject in task_list[name].keys():
        file_content.append("## " + subject_matcher[subject] + "\n\n")
        task_list[name][subject] = sorted(task_list[name][subject], key=lambda x: x[0])
        
        for number, task_content in task_list[name][subject]:
            file_content.append(f"### Задача №{number}\n\n")

            performed = task_content#"$$".join(task_content.split("TEX"))
            file_content.append(f"\n{performed}\n")

with open("README.md", 'w') as f:
    f.write(''.join(file_content))