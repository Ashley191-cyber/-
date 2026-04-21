def read_quadruples(filename):
    quadruples = []

    with open(filename, 'r') as file:
        for line in file:
            # 使用逗号分隔每个四元式的字段
            quadruple = line.strip().split(', ')

            # 将四元式添加到列表中
            quadruples.append(quadruple)

    return quadruples

def is_number(s):
    return s.isdigit()

def get_index_by_label(quadruples, label):
    for i, quadruple in enumerate(quadruples):
        if quadruple[0] == label :
            return i
    return None

def execute_quadruples(quadruples):
    i = get_index_by_label(quadruples,'main')
    variables = {}
    call_stack = []  # 用于保存函数调用的执行上下文
    parameter = {}
    parameter_num = 0
    parameter_record = 0

    while i < len(quadruples) - 1:
        #测试用，查看四元式运行顺序
        # print(i)
        quadruple = quadruples[i]
        if quadruple[0] == ':=':  # 赋值操作
            if is_number(quadruple[1]):
                variables[quadruple[3]] = int(quadruple[1])
            elif quadruple[1] == '_':
                variables[quadruple[3]] = parameter[parameter_record]
                parameter_record += 1
                if parameter_num == parameter_record:
                    parameter_record = 0
                    parameter_num = 0
                #测试用，查看是否成功参数传递
                # print(variables)
            else:
                variables[quadruple[3]] = variables.get(quadruple[1])
            i += 1
        elif quadruple[0] == '<':  # 小于比较
            if is_number(quadruple[1]):
                t1 = int(quadruple[1])
            else:
                t1 = variables.get(quadruple[1])
            if is_number(quadruple[2]):
                t2 = int(quadruple[2])
            else:
                t2 = variables.get(quadruple[2])
            if t1 < t2:
                variables[quadruple[3]] = 1
            else:
                variables[quadruple[3]] = 0
            i += 1
        elif quadruple[0] == '>':  # 大于比较
            if is_number(quadruple[1]):
                t1 = int(quadruple[1])
            else:
                t1 = variables.get(quadruple[1])
            if is_number(quadruple[2]):
                t2 = int(quadruple[2])
            else:
                t2 = variables.get(quadruple[2])
            if t1 > t2:
                variables[quadruple[3]] = 1
            else:
                variables[quadruple[3]] = 0
            i += 1
        elif quadruple[0] == '==':  # 等于比较
            if is_number(quadruple[1]):
                t1 = int(quadruple[1])
            else:
                t1 = variables.get(quadruple[1])
            if is_number(quadruple[2]):
                t2 = int(quadruple[2])
            else:
                t2 = variables.get(quadruple[2])
            if t1 == t2:
                variables[quadruple[3]] = 1
            else:
                variables[quadruple[3]] = 0
            i += 1
        elif quadruple[0] == '!=':  # 不等于比较
            if is_number(quadruple[1]):
                t1 = int(quadruple[1])
            else:
                t1 = variables.get(quadruple[1])
            if is_number(quadruple[2]):
                t2 = int(quadruple[2])
            else:
                t2 = variables.get(quadruple[2])
            if t1 != t2:
                variables[quadruple[3]] = 1
            else:
                variables[quadruple[3]] = 0
            i += 1
        elif quadruple[0] == '+':  # 加法
            if is_number(quadruple[1]):
                t1 = int(quadruple[1])
            else:
                t1 = variables.get(quadruple[1])
            if is_number(quadruple[2]):
                t2 = int(quadruple[2])
            else:
                t2 = variables.get(quadruple[2])
            t3 = t1 + t2
            variables[quadruple[3]] = t3
            i += 1
        elif quadruple[0] == '-':  # 减法
            if is_number(quadruple[1]):
                t1 = int(quadruple[1])
            else:
                t1 = variables.get(quadruple[1])
            if is_number(quadruple[2]):
                t2 = int(quadruple[2])
            else:
                t2 = variables.get(quadruple[2])
            t3 = t1 - t2
            variables[quadruple[3]] = t3
            i += 1
        elif quadruple[0] == '*':  # 乘法
            if is_number(quadruple[1]):
                t1 = int(quadruple[1])
            else:
                t1 = variables.get(quadruple[1])
            if is_number(quadruple[2]):
                t2 = int(quadruple[2])
            else:
                t2 = variables.get(quadruple[2])
            t3 = t1 * t2
            variables[quadruple[3]] = t3
            i += 1
        elif quadruple[0] == '/':  # 除法
            if is_number(quadruple[1]):
                t1 = int(quadruple[1])
            else:
                t1 = variables.get(quadruple[1])
            if is_number(quadruple[2]):
                t2 = int(quadruple[2])
            else:
                t2 = variables.get(quadruple[2])
            t3 = t1 / t2
            variables[quadruple[3]] = t3
            i += 1
        elif quadruple[0] == 'j>':  # 小于比较
            if is_number(quadruple[1]):
                t1 = int(quadruple[1])
            else:
                t1 = variables.get(quadruple[1])
            if is_number(quadruple[2]):
                t2 = int(quadruple[2])
            else:
                t2 = variables.get(quadruple[2])
            if t1 > t2:
                i = get_index_by_label(quadruples,quadruple[3])
            else:
                i += 1

        elif quadruple[0] == 'j':
            i = get_index_by_label(quadruples, quadruple[3])





        elif quadruple[0] == 'Par':  # 参数传递

            if is_number(quadruple[3]):

                parameter[parameter_num] = int(quadruple[3])

            else:

                parameter[parameter_num] = variables.get(quadruple[3])
            parameter_num += 1
            i += 1


        elif quadruple[0] == 'call':  # 函数调用

            function_name = quadruple[2]
            # parameter_num = int(quadruple[3])

            # 获取参数值

            # 保存当前执行上下文
            call_stack.append({'i': i + 1, 'variables': variables.copy()})
            # 跳转到函数定义的位置
            i = get_index_by_label(quadruples, function_name)




        elif quadruple[0] == 'return':  # 函数返回

            # 恢复上一层调用函数的执行上下文
            print(variables)
            if variables['v0']:
                temp=variables.get('v0')

            if call_stack:

                context = call_stack.pop()

                i = context['i']

                variables = context['variables']
                if temp:
                    variables['v0'] = temp
            else:

                break  # 如果没有调用栈，表示程序执行结束



        else:
            i += 1

    # print(variables)
    return variables

# 示例用法
# filename = 'middleCodeFile.txt'
# quadruples_sequence = read_quadruples(filename)
# execute_quadruples(quadruples_sequence)
# 打印存储的四元式序列
# for quadruple in quadruples_sequence:
#     print(quadruple)
