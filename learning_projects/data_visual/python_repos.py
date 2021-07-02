# utf-8
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)  # 爬取链接，获取网页内容
print('状态码：', r.status_code)  # 请求状态码
response_dict = r.json()  # 返回json格式信息，存储在字典中
print('仓库总数：', response_dict['total_count'])

repo_dicts = response_dict['items']  # 获取‘items’仓库列表
# 获取仓库中‘name’、‘stargazers_count’信息，存储在列表中
names, plot_dicts = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        }
    plot_dicts.append(plot_dict)

# 图表配置
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

# 绘制条形图
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
