import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

csv = pd.read_csv('national-history.csv')
pd = pd.DataFrame(csv)
# print(pd)

fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(x=pd['date'],
                         y=pd['hospitalizedCurrently'],
                         mode='lines',
                         name='Current Patients in Hospital'))
fig.add_trace(go.Scatter(x=pd['date'],
                         y=pd['inIcuCurrently'],
                         mode='lines',
                         name='Amount of Patients in Hospital ICU'))
fig.add_trace(go.Scatter(x=pd['date'],
                         y=pd['onVentilatorCurrently'],
                         mode='lines',
                         name='ICU Patients on Ventilators'))
fig.update_layout(
    title='Covid Patients in Hospitals vs ICU vs Patients on Ventilators from March 2020 to March 2021'
)



fig.show()
