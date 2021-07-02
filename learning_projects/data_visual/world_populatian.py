import json
import pygal_maps_world.maps
from contry_codes import get_country_code
from pygal.style import RotateStyle
# 加载json文件
filename = './json/population_data.json'
with open (filename) as f:
    pop_data = json.load(f)
# 提取各国家国别码以及对应人口数，存储在字典中
cc_population = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        contry_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(contry_name)
        if code:
            cc_population[code] = population
# 根据人口数对各国家分组
cc_pops_1,cc_pops_2,cc_pops_3 = {},{},{}
for cc, pop in cc_population.items():
    if pop <10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
# 绘制世界人口地图，并创建不同颜色
world_map_style = RotateStyle('#336699')
world_map = pygal_maps_world.maps.World(style=world_map_style)
world_map.title = 'World Population in 2010, by Country'
world_map.add('0-10m',cc_pops_1)
world_map.add('10m-1bn',cc_pops_2)
world_map.add('>10bn',cc_pops_3)
world_map.render_to_file('world_population.svg')
