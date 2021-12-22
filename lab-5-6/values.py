from enum import Enum

class state(Enum):
    DEFAULT = 1
    PICTURE = 2
    PLOT = 3

current_state = state.DEFAULT
prog_path = 'C:/Users/pahan/python_prog/lab-5-6'
fig_filename = 'fig.png'
kovyrshintoken = '5077381184:AAE5d6etfiLN8K7SbPwabfuGAXYG6xuPla4'
commands = ['start', 'help', 'options', 'pics']
pic1_url = 'https://ichef.bbci.co.uk/news/640/cpsprodpb/14236/production/_104368428_gettyimages-543560762.jpg'
pic2_url = 'https://www.belnovosti.by/sites/default/files/2020-02/ezh_0.jpg'
first_pic = 'первая картинка'
second_pic = 'вторая картинка'
eitherpic_r = ('(^' + first_pic + ')|(^' + second_pic + ')')
pics_r = r'^картинк[аиу]'
plot_r = r'(((по)?стро[ий]).*(графи[кч]))|((графи[кч]).*((по)?стро[ий]))'
plotted_func_r = r'^.x.'
