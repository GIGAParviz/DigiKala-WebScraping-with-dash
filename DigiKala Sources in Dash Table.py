from dash import Dash,dcc , Output, Input # pip install dash
import dash_bootstrap_components as dbc # pip install dash-bootstrap-components
import dash_html_components as html # pip install dash-html-components
import os
import dash_table # pip install dash-table
import  plotly.graph_objects as go # pip install plotly
app = Dash(__name__,external_stylesheets=[dbc.themes.CYBORG])
# columns=[{'name':i,'id':i} for i in ['قیمت','عنوان' ] ]
my_div = html.Div()


my_btn = dbc.Button('نمایش جدول',style={'margin-top':'20px'})

@app.callback(
    Output(my_div,component_property='children'),
    Output(my_btn,component_property='n_clicks'),
    Input(my_btn,component_property='n_clicks')
)
def create_table(n_clicks):
    if n_clicks>0:
        rows = [html.Tr([html.Th('تصویر'),html.Th('قیمت'),html.Th('عنوان'),])]
       
        with open('Titles.txt',encoding='utf-8') as f:
            titles = f.read().split('\n')
        with open('Prices.txt' , encoding='utf-8') as f:
            prices = f.read().split('\n')
        with open('Links.txt' , encoding='utf-8') as f:
            links = f.read().split('\n')
        image_list = os.listdir(r'C:\Users\ASUS\OneDrive\Desktop\boot_camp\W')

        for t,p,l,image_name in zip(titles,prices,links,image_list):
            img = html.Img(src=app.get_asset_url(f'images/{image_name}'),width='100px',height='100px')
            d = html.Tr([html.Td(img),html.Td(p),html.A(t,href=l),])
            rows.append(d)
        children = [html.Table(rows,style={'width':'100%'})]
        return children , n_clicks

app.layout = dbc.Container(
    
    [
        dbc.Row([my_div,my_btn],className='text-center')      
        ])
if __name__=='__main__':
    app.run_server(port='8000')