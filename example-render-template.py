import yaml
from jinja2 import Template

with open("templates/bgp-crpd01.yaml") as f:
        vars = yaml.load(f)
        t_file = open("templates/bgp.j2")
        t =  Template(t_file.read())
        print(t.render(vars))
        t_file.close()
