from jinja2 import Template


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#
# per1 = Person("Sanch", 37)
# tm = Template("My name is {{p.get_name()}} and I am {{p.get_age()}} years old")
# msg = tm.render(p=per1)
# print(msg)

# cities = [{'id': 5, 'city': 'Bagdad'},
#           {'id': 15, 'city': 'Minsk'},
#           {'id': 8, 'city': 'Moskva'},
#           {'id': 2, 'city': 'Kiev'},
#           {'id': 6, 'city': 'Stambul'}]
#
#
# link = """<select name="cities">
# {% for c in cities -%}
#     <option value="{{c['id']}}">{{c['city']}}</option>
# {% endfor -%}
# </select>"""
#
# tm = Template(link)
# msg = tm.render(cities=cities)
# print(msg)

