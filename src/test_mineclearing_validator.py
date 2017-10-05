from mineclearing_validator import evaluate
from os import listdir

if __name__ == '__main__':
    folder_prefix = '../example-runs/'
    fields = listdir(folder_prefix + 'fields')
    scripts = listdir(folder_prefix + 'scripts')
    solutions = listdir(folder_prefix + 'solutions')
    for test_index in range(0, len(fields)):
        field = folder_prefix + "fields/" + fields[test_index]
        script = folder_prefix + "scripts/" + scripts[test_index]
        solution_lines = open(folder_prefix + "solutions/" + solutions[test_index]).readlines()
        result = evaluate(field, script).split("\n")

        did_test_pass = True
        for line_index in range(0, len(solution_lines)):
            solution_line = solution_lines[line_index].strip()
            result_line = result[line_index].strip()
            if solution_line != result_line:
                did_test_pass = False
                break

        print("Test " + str(test_index) + " completed: " + str(did_test_pass))
