#  Create a function named most_classes that takes a dictionary of teachers.
#  Each key is a teacher's name and their value is a list of classes they've
#  taught. most_classes should return the teacher with the most classes

teachers = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
'Kenneth Love': ['Python Basics', 'Python Collections'],
"Dan Morse": ["Public Speaking", "Being fun"],
"Captain Rainbow": ["Problem Solving"]}


def most_classes(my_dict):
    teachers_dict = {}
    for teacher in my_dict:
        teachers_dict[teacher] = len(my_dict[teacher])
    return max(teachers_dict, key=teachers_dict.get)
print(most_classes(teachers))


# anoter way to get it
# def most_classes(teacher_dict):
#     max_count = 3
#     for teacher in teacher_dict:
#         temp_list = []
#         temp_list.append(teacher)
#         temp_list.append(len(teacher_dict[teacher]))
#         if len(teacher_dict[teacher]) >= max_count:
#             return teacher
# print(most_classes(teachers))
