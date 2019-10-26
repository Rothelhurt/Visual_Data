import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LC

my_style = LC('#336699', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Phyton Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value': 43532, 'label': 'Description of httpie.'},
    {'value': 44802, 'label': 'Description of django.'},
    {'value': 47123, 'label': 'Description of flask.'}
]

chart.add('', plot_dicts)
chart.render_to_file('bar_description.svg')
