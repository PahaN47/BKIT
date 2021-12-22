import urllib.request
import json
import field
import gen_random
import unique
import print_result
import cm_timer

data_url = 'https://raw.githubusercontent.com/ugapanyuk/BKIT_2021/main/notebooks/fp/files/data_light.json'

@print_result.print_result
def f1(data):
    return sorted(unique.unique(list(field.field(data, 'job-name')), ignore_case= True))

@print_result.print_result
def f2(data):
    return list(filter(lambda name: name.lower().find('программист') == 0, data))

@print_result.print_result
def f3(data):
    return list(map(lambda word: word + ' с опытом Python', data))

@print_result.print_result
def f4(data):
    salaries = gen_random.gen_random(100000, 200000, len(data))
    result = [job_name + ', зарплата ' + str(salary) + 'руб.' for job_name, salary in zip(data, salaries)]
    return result

if __name__ == '__main__':
    data = json.load(urllib.request.urlopen(data_url))
    with cm_timer.cm_timer_2():
        f4(f3(f2(f1(data))))
